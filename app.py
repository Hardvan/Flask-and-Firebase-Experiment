from flask import Flask, render_template, request, jsonify
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

    if request.method == 'POST':
        name = request.form['name']

        # ? Pushing data to firebase
        db.child("todo").push(name)

        # ? Getting data from firebase
        todo = db.child("todo").get()

        return render_template('index.html', t=todo.val().values())

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
