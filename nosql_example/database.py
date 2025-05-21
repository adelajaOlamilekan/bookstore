from pymongo import MongoClient

client = MongoClient()

database = client.bookstore

user_collection = database["users"]