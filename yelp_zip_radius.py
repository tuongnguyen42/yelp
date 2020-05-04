from pymongo import MongoClient
from connection import conn
from math import radians, sin, cos, acos
#“”“
# Python script for listing businesses filtered by zip code and radius
#”“”
# connect to host and port
client = MongoClient(conn.host, conn.port)
print("Welcome to Yelp!")
print("---------------------------------------")
# get user input zip
input_zip = input("Enter a zip code: ")
input_radius = int(input("Enter an integer for radius to look up businesses: "))
# use yelp database
db = client["yelp"]
# use business collection
bus_col = db["business"]
query = {"postal_code": input_zip}
# limit to 10 businesses
myquery = bus_col.find(query).limit(10)

total_latitude = 0
total_longitude = 0
n = 0
for x in myquery:
	total_latitude += x["latitude"]
	total_longitude += x['longitude']
	n += 1

# compute user's location
user_latitude = total_latitude / n
user_longitude = total_longitude / n

second_query = bus_col.find(query).limit(10)

def print_business():
	print("---------------------------------------")
	print("Listing 10 businesses within the radius of", input_radius, "are: ")
	print("---------------------------------------")

def compute_distance(input_radius, user_latitude, user_longitude):
	distance = 0
	R = 6371.01 # earth radius
	# compute distance between two points using latitude and longtitude
	# formula reference: https://www.w3resource.com/python-exercises/math/python-math-exercise-27.php
	for y in second_query:
		end_longitude = radians(float(y["longitude"])) 
		end_latitude = radians(float(y["latitude"]))
		distance = R * acos(sin(user_latitude) * sin(end_latitude) 
			+ cos(user_latitude) * cos(end_latitude) * cos(user_longitude - end_longitude))
		# print("distance between points: ", distance)
		if distance <= input_radius:
			
			print(y["name"])
	print("---------------------------------------")

def main():
	print_business()
	compute_distance(input_radius, user_latitude, user_longitude)
	
if __name__ == "__main__":
	main()




