from pymongo import MongoClient
from connection import conn
#“”“
# Python script for listing hours of a business
#”“”
# connect to host and port
client = MongoClient(conn.host, conn.port)
print("Welcome to Yelp!")
print("---------------------------------------")
# get user input the business name
input_name = input("Enter a business name to find hours: ")
# use yelp database
db = client["yelp"]
# use business collection
bus_col = db["business"]
query = {"name": input_name }
# limit to 5 samples since one business may have many locations
myquery = bus_col.find(query).limit(5)

print("---------------------------------------")
print("The hours of", input_name, "are: ")
print("---------------------------------------")

# print hours of the chosen business
i = 1
for x in myquery:
	print("location", i)
	print(x["hours"])
	print("---------------------------------------")
	i += 1

		

	
