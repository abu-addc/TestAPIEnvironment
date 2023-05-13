from flask import Flask, jsonify 
from pymongo import MongoClient
from dotenv.main import load_dotenv
import os

load_dotenv()
MONGO_URI = os.environ['MONGO_URI']

client = MongoClient(MONGO_URI)

db = client['sample_inventory']

inventory_count = db['Inventory_Count']

app = Flask(__name__)

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

# #The endpoint to retrive an inventory by status (Just for example)
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
    
#The endpoint to retrive an item from the inventory by SKU
@app.route("/inventory/getItem/<sku>", methods=['GET'])
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


# doc_toFind = {"inventory_id": "AUUID"}

# result = inventory_count.find_one(doc_toFind)

# pprint.pprint(result)

# @app.route("/inventory", methods=['POST','GET'])
# def data():
#     if request.method == 'POST':
#         body = request.json
#         inventory_id: body['inventory_id']
#         name: body['name']
#         status: body['status']

#         db['Inventory_Count']._insert_one({
#             "inventory_id": inventory_id,
#             "name": name,
#             "status": status
#         })

#         return  jsonify({
#             'status_posted': 'Data is posted',
#             'inventory_id': inventory_id,
#             'name': name,
#             'status': status
#         })
#     if request.method == 'GET':
#         allData = db['Inventory_Count'].find()
#         respond = []
#         for data in allData:
#             inventory_id: data['inventory_id']
#             name: data['name']
#         # inventory_location: data['inventory_location']
#         # created_by: data['created_by']
#         # date_created: data['date_created']
#         # list_of_events: data['list_of_events']
#         # counted_by: data['counted_by']
#         # items_counted: data['items_counted']
#             status: data['status']
            
#             dataDict = {
#                 'inventory_id': inventory_id,
#                 'name': name,
#             # 'inventory_location': inventory_location,
#             # 'created_by': created_by,
#             # 'date_created': date_created,
#             # 'list_of_events': list_of_events,
#             # 'counted_by': counted_by,
#             # 'items_counted': items_counted,
#                 'status': status
#             }
#             respond.append(dataDict)
#             return jsonify(respond)

# @app.route('/inventory/get', methods=['GET'])
# def getInventoryByID():
#     allData = db['Inventory_Count'].find()
#     respond = []
#     for data in allData:
#         inventory_id: data['inventory_id']
#         name: data['name']
#         inventory_location: data['inventory_location']
#         created_by: data['created_by']
#         date_created: data['date_created']
#         list_of_events: data['list_of_events']
#         counted_by: data['counted_by']
#         items_counted: data['items_counted']
#         status: data['status']

#         dataDict = {
#             'inventory_id': inventory_id,
#             'name': name,
#             'inventory_location': inventory_location,
#             'created_by': created_by,
#             'date_created': date_created,
#             'list_of_events': list_of_events,
#             'counted_by': counted_by,
#             'items_counted': items_counted,
#             'status': status
#         }
#         respond.append(dataDict)
#     return jsonify(respond)
    


