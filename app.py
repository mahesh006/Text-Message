from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from fetch import fetch
import symbl
from twilio.rest import Client

app = Flask(__name__)


# Your Account SID from twilio.com/console
account_sid = "AC190c279bf696a785bccbef9d676aa496"
# Your Auth Token from twilio.com/console
auth_token  = "de14f7bb9959b4f4593b04ebc0dfaf50"



@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('MediaUrl0', '')
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if incoming_msg:              
        path_to_audio = fetch(incoming_msg)
        print(path_to_audio)
        print(incoming_msg)
        print('success')
        local_path = r'C:\Users\DELL\Desktop\twilio-bot\static\file.mp3'

        # Process audio file
        conversation_object = symbl.Audio.process_file(file_path=local_path)
        data = conversation_object.get_messages().messages
        
        final = ''
        for text in data:
            final += str(text.text)
        print(final)
        msg.body(final)
        responded = True
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to="+917989651824", 
            from_="+1 928 396 1181",
            body=final)       

    if not responded:
        msg.body('I only know about famous quotes and cats, sorry!')
    return str(resp)


if __name__ == '__main__':
    app.run()



