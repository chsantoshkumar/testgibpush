import pymongo
client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb234@cluster0.6px3i.mongodb.net/?retryWrites=true&w=majority")

db = client.test

d = {
    "name":"sudhanshu",
    "email":"sudhanshu@ineuron.ai",
    "surname":"kumar"
}
db1=client['mongotest1']
coll=db1['test1']
coll.insert_one(d)


