import requests
import uuid

def fetch(url):
    r = requests.get(url, allow_redirects=True)
    filename = r"C:\Users\DELL\Desktop\twilio-bot\static\file.mp3"
    open(filename, 'wb').write(r.content)
    return filename