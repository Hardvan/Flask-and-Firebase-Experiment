from flask import Flask, request, jsonify
import urllib3
import os
from dotenv import load_dotenv
import pyrebase

load_dotenv()

# ? Firebase Config
FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY")
config = {
    "apiKey": FIREBASE_API_KEY,
    "authDomain": "test-1c7ad.firebaseapp.com",
    "databaseURL": "https://test-1c7ad-default-rtdb.firebaseio.com",
    "projectId": "test-1c7ad",
    "storageBucket": "test-1c7ad.appspot.com",
    "messagingSenderId": "399208046542",
    "appId": "1:399208046542:web:de9b7e073aac39e851d59f",
    "measurementId": "G-6R5KXMGXQF"
}

firebase = pyrebase.initialize_app(config)

# ? Database
db = firebase.database()

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    return "Hello, World!"


if __name__ == '__main__':
    app.run(debug=True)
