from flask import Flask, jsonify
from pymongo import MongoClient
from dotenv.main import load_dotenv
import os
# from .Controllers import InventoriesController

load_dotenv()
MONGO_URI = os.environ['MONGO_URI']

client = MongoClient(MONGO_URI)

db = client['sample_inventory']

inventory_count = db['Inventory_Count']

print(MONGO_URI)

app = Flask(__name__)

@app.route("/")
def index():
    return MONGO_URI

@app.route("/inventory/get/<status>", methods=['GET'])
def getInventoryByID(status):
    try:
        doc_toFind = {"status": status}
        inventory = inventory_count.find_one(doc_toFind)
        if inventory:
            print(inventory)
            inventory['_id'] = str(inventory['_id'])
            return jsonify(inventory), 200
        else:
            return jsonify({"error": "An inventory NOT FOUND!"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.debug = True
    app.run()
