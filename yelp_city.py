from pymongo import MongoClient
from connection import conn
#“”“
# Python script for listing businesses filtered by city
#”“”
# connect to host and port
client = MongoClient(conn.host, conn.port)
print("Welcome to Yelp!")
print("---------------------------------------")
# get user input city
input_city = input("Enter a city to check businesses: ")
# use yelp database
db = client["yelp"]
# use business collection
bus_col = db["business"]
query = {"city": input_city }
# limit to 10 businesses
myquery = bus_col.find(query).limit(10)

print("---------------------------------------")
print("Listing 10 businesses in", input_city, ": ")
print("---------------------------------------")

# print businesses
for x in myquery:
	print(x["name"])
print("---------------------------------------")