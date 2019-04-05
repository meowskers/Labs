from pymongo import MongoClient
from pprint import pprint
from bson.objectid import ObjectId
client = MongoClient("mongodb://localhost:27017")

if __name__ == '__main__':
    db = client.mongo_db_lab
    temp = db['definitions']
    for x in temp.find():
        pprint(x)
    pprint(temp.find_one())
    pprint(temp.find_one({"word" : "Capitaland"}))
    pprint(temp.find_one({"_id": ObjectId("56fe9e22bad6b23cde07b8ce")}))
    temp.insert_one({"word": "beirrun"})