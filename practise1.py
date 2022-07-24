import pymongo
client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.6px3i.mongodb.net/?retryWrites=true&w=majority")
db = client.test
data = {
    "name" : "sudhanshu",
    "mail id": "abcd@gmail.com",
    "subject": ["data science", "big data", "data analytics" ]
}

data1= {
    "name":"santosh kumar",
    "email id ": "abcd1@gmail.com",
    "subject": ["radio", "5g","4g", "data science"]
}

print(db)

db1=client["my info1"]
coll = db1.colle