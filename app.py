from flask import Flask, jsonify
from pymongo import MongoClient
from dotenv.main import load_dotenv
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

# #The endpoint to retrive an inventory by inventory_id
# @app.route("/inventory/get/<inventory_id>", methods=['GET'])
# def getInventoryByID(inventory_id):
#     try:
#         doc_toFind = {"inventory_id": inventory_id}
#         inventory = inventory_count.find_one(doc_toFind)
#         if inventory:
#             print(inventory)
#             inventory['_id'] = str(inventory['_id'])
#             return jsonify(inventory), 200
#         else:
#             return jsonify({"error": "An inventory NOT FOUND!"}), 404
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
    
# #The endpoint to retrive an inventory by status 
# #(I used status because in MongoDB inventory_id has a space "A UUID", and it causes error!)
# @app.route("/inventory/get/<status>", methods=['GET'])
# def getInventoryByID(status):
#     try:
#         doc_toFind = {"status": status}
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
# @app.route("/inventory/getItem/<sku>", methods=['GET'])
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


if __name__ == '__main__':
    app.debug = True
    app.run()
