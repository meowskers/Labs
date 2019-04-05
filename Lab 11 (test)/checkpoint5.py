from pymongo import MongoClient
from pprint import pprint
from bson.objectid import ObjectId
import random
import datetime
client = MongoClient("mongodb://localhost:27017")


def random_word_requester():
    db = client.mongo_db_lab
    temp = db['definitions']
    words = []
    words = list(temp.find())
    word = random.choice(words)
    temp.update({'word' : word['word']}, {'$push': {"set": datetime.datetime.utcnow()}})
    return word


if __name__ == '__main__':
    print random_word_requester()
