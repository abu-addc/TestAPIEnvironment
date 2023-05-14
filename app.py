from flask import Flask
from pymongo import MongoClient
from Controllers.InventoriesController import get_inventories_by_user


app = Flask(__name__)

@app.route('/inventories/<user_id>', methods=['GET'])
def inventories_route(user_id):
    return get_inventories_by_user(user_id)

if __name__ == '__main__':
    app.run()



