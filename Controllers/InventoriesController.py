from flask import Flask, jsonify 
from pymongo import MongoClient
from dotenv.main import load_dotenv
import os
#from ..Models.InventoryCount import InventoryCount

load_dotenv()
MONGO_URI = os.environ['MONGO_URI']

client = MongoClient(MONGO_URI)

db = client['sample_inventory']

inventory_count = db['Inventory_Count']

app = Flask(__name__)

#The endpoint to retrive an inventory by inventory ID
# @app.route("/inventory/get/<string:id>", methods=['GET'])
# def getInventoryByID(id):
#     try:
#         doc_toFind = {"inventory_id": id}
#         inventory = inventory_count.find_one(doc_toFind)
#         if inventory:
#             return jsonify(inventory), 200
#         else:
#             return jsonify({"error": "An inventory NOT FOUND!"}), 404
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
    
    

@app.route('/inventory/get/', method=['GET'])
def getInventoryByID():
    result = inventory_count.find()
    respond = jsonify(result)
    return respond

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
    

if __name__ == '__main__':
    app.run()

