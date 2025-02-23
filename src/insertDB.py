from pymongo import MongoClient
import json

connection_string = "mongodb+srv://tudorpascaru1:plants5@plants.y138r.mongodb.net/?retryWrites=true&w=majority&appName=Plants"
client = MongoClient(connection_string)
db = client.plant_expert
collection = db.plant

collection.delete_many({})

with open('data/plants.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    plants_list = [{"name": name, **details} for name, details in data['plants'].items()]
    collection.insert_many(plants_list)