from pymongo import MongoClient
from connection import conn
#“”“
# Python script for listing the businesses filtered by rating stars 
#”“”
# connect to host and port
client = MongoClient(conn.host, conn.port)
print("Welcome to Yelp!")
print("---------------------------------------")
print("Rating stars: 1 2 3 4 5")
# get user input rating of stars
input_star = int(input("Choose a number from rating stars: "))
# use yelp database
db = client["yelp"]
# use business collection
bus_col = db["business"]

# apply rating star filter
if input_star < 5:
	query = {"stars": {"$gt" : input_star }}
elif input_star == 5:
	query = {"stars": 5}

# limit to 10 result for sample result
myquery = bus_col.find(query).limit(10)

print("---------------------------------------")
print("The businesses above", input_star, "rating stars are: ")
print("---------------------------------------")

for x in myquery:
	#print name of the business
	print(x["name"])
print("---------------------------------------")









































