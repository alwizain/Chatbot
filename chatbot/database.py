from pymongo import MongoClient

def get_collection():
    client = MongoClient('mongodb+srv://alwizain:kacanggoreng1203@webchatbot.fmkuapj.mongodb.net/?retryWrites=true&w=majority')
    db = client['chatbot']
    col = db['chatbot_respon']
    coll = db['chatbot_responses']
    return col, coll
    