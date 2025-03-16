from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")

# 1. Sukurkite restoranų duomenų rinkinį (pridedamas zip failas)
db = client.restaurants_db
collection = db.restaurant

with open('restaurants.json') as file:
    file_data = [json.loads(line) for line in file]

collection.insert_many(file_data)  

# 2. Parašykite užklausą atvaizduojančią visus dokumentus iš restoranų rinkinio
for restaurant in collection.find():
    print(restaurant)

# 3. Parašykite užklausą, kuri atvaizduotų laukus - restaurant_id, name, borough ir cuisine - visiems dokumentams
for restaurant in collection.find({}, {"restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1}):
    print(restaurant)

# 4. Parašykite užklausą, kuri atvaizduotų laukus - restaurant_id, name, borough ir cuisine -, bet nerodytų lauko _id visiems dokumentams
for restaurant in collection.find({}, {"_id": 0, "restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1}):
    print(restaurant)

# 5. Parašykite užklausą, kuri parodytų visus miestelio Bronx restoranus
for restaurant in collection.find({"borough": "Bronx"}):
    print(restaurant)

# 6. Parašykite užklausą, kuri parodytų restoranus su įvertinimu tarp 80 ir 100 (duomenis gali reikėti agreguoti).
pipeline = [
    {"$unwind": "$grades"},
    {"$match": {"grades.score": {"$gte": 80, "$lte": 100}}},
    {"$group": {"_id": "$restaurant_id", "name": {"$first": "$name"}, "borough": {"$first": "$borough"}, "cuisine": {"$first": "$cuisine"}, "grade": {"$first": "$grades"}}}
]
for restaurant in collection.aggregate(pipeline):
    print(restaurant)

# 7. Parašykite užklausą, kad cuisine būtų išdėstyta didėjimo tvarka, o borough - mažėjimo.
for restaurant in collection.find().sort({"cuisine": 1, "borough": -1}):
    print(restaurant)
