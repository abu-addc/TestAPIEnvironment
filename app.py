from flask import Flask
from pymongo import MongoClient
from dotenv.main import load_dotenv
import os

load_dotenv()
MONGO_URI = os.environ['MONGO_URI']

client = MongoClient(MONGO_URI)

print(MONGO_URI)

app = Flask(__name__)

@app.route("/")
def index():
    return MONGO_URI


