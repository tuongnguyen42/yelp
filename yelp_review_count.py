from pymongo import MongoClient
from connection import conn
#“”“
# Python script to find buinesses filtered by review count
#”“”
# connect to host and port
client = MongoClient(conn.host, conn.port)
print("Welcome to Yelp!")
print("---------------------------------------")
print("Review count range: 0 to 10000")
# get user input
input_c = int(input("Choose an integer from count range to find open businesses: "))
# use yelp database
db = client["yelp"]
# use business collection
bus_col = db["business"]
query = {"review_count" : {'$gte': input_c}}
# limit to 10 business as a sample
myquery = bus_col.find(query).limit(10)

print("---------------------------------------")
print("Listing 10 businesses for you with at least", input_c, "reviews: ")
print("---------------------------------------")

# print business
for x in myquery:
	print(x["name"])
print("---------------------------------------")