import json
import random
import nltk
import string
import numpy as np
import pickle
import tensorflow as tf
from database import get_collection
from nltk.stem import WordNetLemmatizer
from tensorflow import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences

global responses, lemmatizer, tokenizer, le, model, input_shape
input_shape = 47

# import dataset answer
def load_response():
    global responses
    responses = {}
    col,coll = get_collection()
    
    for intent in col.find():
        for intent in coll.find():
            responses[intent["tag"]]=[intent["responses"]]

# import model dan download nltk file
def preparation():
    load_response()
    global lemmatizer, tokenizer, le, model
    tokenizer = pickle.load(open('model/tokenizer.pkl', 'rb'))
    le = pickle.load(open('model/le.pkl', 'rb'))
    model = keras.models.load_model('model/chatbot_model.h5')
    lemmatizer = WordNetLemmatizer()
    nltk.download('punkt', quiet=True)
    nltk.download('wordnet', quiet=True)
    nltk.download('omw-1.4', quiet=True)

# hapus tanda baca
def remove_punctuation(text):
    texts_p = []
    text = [letters.lower() for letters in text 
                            if letters not in string.punctuation]
    text = ''.join(text)
    texts_p.append(text)
    return texts_p

# mengubah text menjadi vector
def vectorization(texts_p):
    vector = tokenizer.texts_to_sequences(texts_p)
    vector = np.array(vector).reshape(-1)
    vector = pad_sequences([vector], input_shape)
    return vector

# klasifikasi pertanyaan user
def predict(vector):
    output = model.predict(vector)
    output = output.argmax()
    response_tag = le.inverse_transform([output])[0]
    return response_tag

# menghasilkan jawaban berdasarkan pertanyaan user
def generate_response(text):
    texts_p = remove_punctuation(text)
    vector = vectorization(texts_p)
    response_tag = predict(vector)
    answer = random.choice(responses[response_tag])
    return answer


# model = tf.keras.Sequential()
# opt = keras.optimizers.Adam()
# callback = EarlyStopping(monitor = 'loss', patience = 1, mode = 'min', restore_best_weights = True)
# model.compile(optimizer=opt, loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# model.fit(vector, response_tag, epochs = 100, callbacks=[callback], verbose=0)
# model.save('model/chatbot_model.h5')