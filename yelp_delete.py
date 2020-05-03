from pymongo import MongoClient
from connection import conn
#“”“
# Python script to delete a business
#”“”
# connect to host and port
client = MongoClient(conn.host, conn.port)
print("Welcome to Yelp!")
print("---------------------------------------")
# get user input city
input_name = input("Enter a business name: ")
# use yelp database
db = client["yelp"]
# use business collection
bus_col = db["business"]
query = {"name": input_name }
# delete a business
myquery = bus_col.delete_many(query)

print("---------------------------------------")
print("business named", input_name, "had been successfully deleted!")
print("---------------------------------------")
