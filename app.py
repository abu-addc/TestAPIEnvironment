from flask import Flask
from pymongo import MongoClient
from Controllers.InventoriesController import *


app = Flask(__name__)

@app.route('/inventories/<user_id>', methods=['GET'])
def inventories_route_get_inventories(user_id):
    return get_inventories_by_user(user_id)

@app.route('/updateInventories', methods=['PUT'])
def inventories_route_update_inventory_status():
    return update_inventory_status()


if __name__ == '__main__':
    app.run()



