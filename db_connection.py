import pymongo

url = "mongodb+srv://adrishadhikari2003:test1234@clusterdjango.asw8aih.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(url)

db = client.DjangoDB


############################### File used to connect to database in mongodb ##################################