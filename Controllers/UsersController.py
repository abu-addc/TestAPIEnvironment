from flask import Flask
from pymongo import MongoClient
from dotenv.main import load_dotenv
import os


load_dotenv()
MONGO_URI = os.environ['MONGO_URI']

client = MongoClient(MONGO_URI)

app = Flask(__name__)

@app.route("/login", methods=['GET'])
def login():
    #### authenticate user
    
    #### return session token
    
    return MONGO_URI





