from datetime import datetime
import json
from flask import Flask, jsonify, request
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

# Custom JSONEncoder to handle serialization of ObjectId and datetime objects
class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        elif isinstance(o, datetime):
            return o.isoformat()
        return super().default(o)


# Retrieve inventories by user_id
def get_inventories_by_user(user_id):
    inventories = list(collection.find({"created_by.user_id": user_id}))

    # Serialize inventories to JSON with the custom encoder
    inventories_json = json.dumps(inventories, cls=CustomEncoder)
    return inventories_json

# Update inventory status by inventory_id and status value
def update_inventory_status():

     # Get the inventory ID from the query parameters
    inventory_id = request.args.get('inventory_id')

    # Get the new status from the request body
    new_status = request.json.get('status')

    # Update the status field of the inventory document
    result = collection.update_one(
        {"inventory_id": inventory_id},
        {"$set": {"status": new_status}}
    )

    if result.matched_count == 1:
        return jsonify({'message': 'Inventory status updated successfully'})
    else:
        return jsonify({'message': 'Inventory not found'}), 404
