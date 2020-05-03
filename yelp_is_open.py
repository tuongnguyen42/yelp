from pymongo import MongoClient
from connection import conn
#“”“
# Python script for listing open business
#”“”
# connect to host and port
client = MongoClient(conn.host, conn.port)
print("Welcome to Yelp!")
print("---------------------------------------")
print("Find open businesses: 0 1")
# get user input
input_n = int(input("Choose 1 to find open businesses: "))
# use yelp database
db = client["yelp"]
# use business collection
bus_col = db["business"]
query = {"is_open": input_n}
# limit to 5 business as a sample
myquery = bus_col.find(query).limit(10)

# open business
if input_n == 1:
	print("---------------------------------------")
	print("Listing 10 open businesses for you: ")
	print("---------------------------------------")

# closed business
if input_n == 0:
	print("---------------------------------------")
	print("Listing 10 closed businesses for you: ")
	print("---------------------------------------")

# print business
for x in myquery:
	print(x["name"])
print("---------------------------------------")