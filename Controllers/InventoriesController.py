from flask import Flask, jsonify, request 
from pymongo import MongoClient
from dotenv.main import load_dotenv
from bson import ObjectId
import os

load_dotenv()
MONGO_URI = os.environ['MONGO_URI']

client = MongoClient(MONGO_URI)

db = client['sample_inventory']

inventory_count = db['Inventory_Count']

app = Flask(__name__)

# ####### To Test the endpoints, please go to app.py and read the brief instruction there #########

#The endpoint to retrive an inventory by inventory ID
@app.route("/inventory/get/<inventory_id>", methods=['GET'])
def getInventoryByID(inventory_id):
    try:
        doc_toFind = {"inventory_id": inventory_id}
        inventory = inventory_count.find_one(doc_toFind)
        if inventory:
            print(inventory)
            inventory['_id'] = str(inventory['_id'])
            return jsonify(inventory), 200
        else:
            return jsonify({"error": "An inventory NOT FOUND!"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# #The endpoint to retrive an inventory by status (Just for testing because of 'A UUID' doesn't work)
# #I used _id instead of inventory_id
# @app.route("/inventory/get/<id>", methods=['GET'])
# def getInventoryByID(id):
#     try:
#         doc_toFind = {"_id": ObjectId(id)}
#         inventory = inventory_count.find_one(doc_toFind)
#         if inventory:
#             print(inventory)
#             inventory['_id'] = str(inventory['_id'])
#             return jsonify(inventory), 200
#         else:
#             return jsonify({"error": "An inventory NOT FOUND!"}), 404
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
    
#The endpoint to retrive an item from the inventory by SKU
@app.route("/inventories/getItem/<sku>", methods=['GET'])
def getItembySKU(sku):
    try:
        item = inventory_count.find_one({"items_counted.sku": sku}, {"items_counted.$": 1})
        if item:
            print(item)
            item['_id'] = str(item['_id'])
            return jsonify(item['items_counted'][0]), 200
        else:
            return jsonify({"error": "An item NOT FOUND!"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# #The endpoint to update a quantity counted from the inventory with the specified SKU
# #In this case I use ObjectID instead of inventory to avoid the misstake of 'A UUID' in MongoDB (We can change it back later)
# #I also import request and from bson import ObjectId on the top of the file
@app.route("/inventories/update/<id>", methods=['PUT'])
def updateQuatityCountedBaseOnSKU(id):
    try:
        sku = request.json["sku"]
        new_quantity = request.json["quantity_counted"]

        result = inventory_count.update_one(
            {"_id": ObjectId(id), "items_counted.sku": sku}, 
            {"$set": {"items_counted.$.quantity_counted": new_quantity}}
            )
        if result.modified_count == 1:
            return "Quantity updated successfully"
        else:
            return "Failed to update quantity"
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# #The endpoint to update a quantity counted from the inventory with the specified user_id
# #I tried to use the same endpoint with def updateQuatityCountedBaseOnSKU(id), but it didn't work
# #In this case I use ObjectID instead of inventory to avoid the misstake of 'A UUID' in MongoDB 
# #and username instead of user_id: 'A UUID' in MongoDB (We can change it back later)
# #I also import request and from bson import ObjectId on the top of the file
@app.route("/inventories/update/specifieduserid/<id>", methods=['PUT'])
def updateQuatityCountedBaseOnUserID(id):
    try:
        username = request.json["username"]
        new_quantity = request.json["quantity_counted"]

        result = inventory_count.update_one(
            {"_id": ObjectId(id), "counted_by.username": username}, 
            {"$set": {"counted_by.$.quantity_counted": new_quantity}}
            )
        if result.modified_count == 1:
            return "Quantity updated successfully"
        else:
            return "Failed to update quantity"
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    


