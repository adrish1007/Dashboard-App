import pymongo
import json
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb+srv://adrishadhikari2003:test1234@clusterdjango.asw8aih.mongodb.net/?retryWrites=true&w=majority")
db = client.DjangoDB
collection = db.JSONData
requesting = []

with open("jsondata.json", encoding='utf-8') as f:
    file_data = json.load(f)
    
collection.insert_many(file_data)

print("Data inserted successfully")
client.close()


########## Testing ##################
# read data from mongodb database based on given query

# for i in collection.find({"name": "Adrishadhikari2003"}):
#     print(i)
    
# print(collection.count_documents({}))


########################### File used to create database in mongodb ###############################