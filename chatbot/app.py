import os
from process import preparation, generate_response
from flask import Flask, request, Response
import requests
 
TOKEN = "YOUR_TOKEN_BOT"

# download nltk
preparation()

#Start Chatbot
app = Flask(__name__)

def parse_message(message):
    print("message-->",message)
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    print("chat_id-->", chat_id)
    print("txt-->", txt)
    return chat_id,txt
 
def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
                'chat_id': chat_id,
                'text': text
                }
   
    r = requests.post(url,json=payload)
    return r

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
       
        chat_id,txt = parse_message(msg)
        name = msg['message']['chat']['first_name']

        if txt == '/start':
            resp = tel_send_message(chat_id, f'Selamat datang, {name}! Silahkan kirim pesan sapaan untuk memulai proses wawancara')
            resp

            text_log = f'({chat_id}) {name} : {txt} \nChatbot : Selamat datang, {name}! Silahkan kirim pesan sapaan untuk memulai proses wawancara \n'
            print(text_log)
            filename = f"respon/log_bot_{name}.txt"

            if os.path.exists(filename):
                # file already exists, so open the file in append mode
                with open(filename, "a") as f:
                    f.write(text_log)
                    f.close()
            else:
                # file does not exist, so create a new file
                with open(filename, "w") as f:
                    f.write(text_log)
                    f.close()

        elif txt == '/end':
            tel_send_message(chat_id, f'Terimakasih {name}, Anda telah menyelesaikan tahap wawancara. Mohon untuk tidak membalas pesan ini!')
            text_log = f'({chat_id}) {name} : {txt}\nChatbot : Terimakasih {name}, Anda telah menyelesaikan tahap wawancara. Mohon untuk tidak membalas pesan ini!\n'
            print(text_log)
            filename = f"respon/log_bot_{name}.txt"

            if os.path.exists(filename):
                # file already exists, so open the file in append mode
                with open(filename, "a") as f:
                    f.write(text_log)
                    f.close()
            else:
                # file does not exist, so create a new file
                with open(filename, "w") as f:
                    f.write(text_log)
                    f.close()
            paused = True

        else:
            tel_send_message(chat_id, generate_response(txt))

            text_log = f'({chat_id}) {name} : {txt}\nChatbot : {generate_response(txt)}\n'
            print(text_log)
            filename = f"respon/log_bot_{name}.txt"

            if os.path.exists(filename):
                # file already exists, so open the file in append mode
                with open(filename, "a") as f:
                    f.write(text_log)
                    f.close()
            else:
                # file does not exist, so create a new file
                with open(filename, "w") as f:
                    f.write(text_log)
                    f.close()
            
    else:
        return "<h1>Welcome!</h1>"
    return Response('ok', status=200)
    

if __name__ == "__main__":
    app.run(debug=True)