from pymongo import MongoClient
from connection import conn
#“”“
# Python script to find business filterd by category
#”“”
# connect to host and port
client = MongoClient(conn.host, conn.port)
print("Welcome to Yelp!")
print("---------------------------------------")
print("Categories: Mexican, Burgers, Gastropubs")
# get user input
input_cat = input("Choose one category from categories to find businesses: ")
field = input_cat + ", Restaurants"
# use yelp database
db = client["yelp"]
# use business collection
bus_col = db["business"]
query = {"categories": field}
# limit to 10 business as a sample
myquery = bus_col.find(query).limit(10)

print("---------------------------------------")
print("Listing 10 businesses with", input_cat, "food for you: ")
print("---------------------------------------")

# print businesses
for x in myquery:
	print(x["name"])
print("---------------------------------------")