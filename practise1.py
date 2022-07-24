import pymongo
client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.6px3i.mongodb.net/?retryWrites=true&w=majority")
db = client.test
data = {
    "name" : "santosh",
    "mail id": "abcd@gmail.com",
    "subject": ["data science", "big data", "data analytics" ]
}

database = client['myinfo1']
collection = database["sant"]
collection.insert_one(data)
