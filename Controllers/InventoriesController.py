from flask import Flask, json, jsonify, request
from pymongo import MongoClient
from dotenv.main import load_dotenv
from bson import ObjectId
import os

load_dotenv()
MONGO_URI = os.environ['MONGO_URI']

client = MongoClient(MONGO_URI)

# Select the database and collection
db = client['sample_inventory']
collection = db['Inventory_Count']

def get_inventories_by_user(user_id):
    inventories = list(collection.find({"created_by.user_id": user_id}))

    # Convert ObjectId to string representation
    for inventory in inventories:
        inventory['_id'] = str(inventory['_id'])

    # Serialize the inventories to JSON
    inventories_json = json.dumps(inventories)

    return jsonify(inventories_json)

