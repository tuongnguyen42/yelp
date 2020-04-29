from pymongo import MongoClient
from pprint import pprint
from connection import conn


client = MongoClient(conn.host,conn.port)
db = client["usdata"]
collection = db["zipcodes"]

data = {
  "_id": "test_id",
  "city": "TEST CITY",
  "state": "TS",
  "pop": 5574,
  "loc": [
    -74.016323,
    40.710537
  ]
}

updated_data = {
    "city": "NEW TEST CITY"
}

def insert(data):
    result =collection.insert_one(data)
    x = collection.find({'_id': "test_id"})
    for doc in x:
        print(doc)
    return result

#insert(data);

def remove_data(document_id):
    result = collection.delete_one({'_id': document_id})
    x = collection.find({'_id': document_id})
    for doc in x:
        print(doc)
    return result
#remove_data("test_id")

def update_data(document_id, data):
    result = collection.update_one({'_id': document_id}, {"$set": data})
    x = collection.find({'_id': document_id})
    for doc in x:
        print(doc)
    return result.acknowledged
update_data("test_id", updated_data)
