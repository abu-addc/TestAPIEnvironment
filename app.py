from flask import Flask, jsonify, request
from pymongo import MongoClient
from dotenv.main import load_dotenv
from bson import ObjectId
import os

load_dotenv()
MONGO_URI = os.environ['MONGO_URI']

client = MongoClient(MONGO_URI)

db = client['sample_inventory'] #The database_name
inventory_count = db['Inventory_Count'] #The collection_name

print(MONGO_URI)

app = Flask(__name__)

@app.route("/")
def index():
    return MONGO_URI

# ####### To Test the endpoints, please uncomment #########
# ####### I put the endpoints here because I don't know how to import the InventoriesController in app.py #########
    
# #The endpoint to retrive an inventory by _id : ObjectId('645c5a80f601147ce550948a')
# #I used _id because in MongoDB inventory_id has a space "A UUID", and it causes error!
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

# #The endpoint to retrive an item from the inventory by SKU
# @app.route("/inventories/getItem/<sku>", methods=['GET'])
# def getItembySKU(sku):
#     try:
#         item = inventory_count.find_one({"items_counted.sku": sku}, {"items_counted.$": 1})
#         if item:
#             print(item)
#             item['_id'] = str(item['_id'])
#             return jsonify(item['items_counted'][0]), 200
#         else:
#             return jsonify({"error": "An item NOT FOUND!"}), 404
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# #The endpoint to update a quantity counted from the inventory with the specified SKU
# #In this case I used ObjectID instead of inventory to avoid the misstake of 'A UUID' in MongoDB We can change it back later
# @app.route("/inventories/update/<id>", methods=['PUT'])
# def updateQuatityCountedBaseOnSKU(id):
#     try:
#         sku = request.json["sku"]
#         new_quantity = request.json["quantity_counted"]

#         result = inventory_count.update_one(
#             {"_id": ObjectId(id), "items_counted.sku": sku}, 
#             {"$set": {"items_counted.$.quantity_counted": new_quantity}}
#             )
#         if result.modified_count == 1:
#             return "Quantity updated successfully"
#         else:
#             return "Failed to update quantity"
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
    
# #The endpoint to update a quantity counted from the inventory with the specified user_id
# #I tried to use the same endpoint with def updateQuatityCountedBaseOnSKU(id), but it didn't work
# #Therefore, I created a new app.route
# #In this case I use ObjectID instead of inventory to avoid the misstake of 'A UUID' in MongoDB
# #and username instead of user_id: 'A UUID' in MongoDB (We can change it back later)
# @app.route("/inventories/update/specifieduserid/<id>", methods=['PUT'])
# def updateQuatityCountedBaseOnUserID(id):
#     try:
#         username = request.json["username"]
#         new_quantity = request.json["quantity_counted"]

#         result = inventory_count.update_one(
#             {"_id": ObjectId(id), "counted_by.username": username}, 
#             {"$set": {"counted_by.$.quantity_counted": new_quantity}}
#             )
#         if result.modified_count == 1:
#             return "Quantity updated successfully"
#         else:
#             return "Failed to update quantity"
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500



if __name__ == '__main__':
    app.debug = True
    app.run()
