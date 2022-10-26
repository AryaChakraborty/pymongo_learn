import pymongo as pym
url = "mongodb+srv://aryatito:Tito%40420@cluster0.5viwfw1.mongodb.net/?retryWrites=true&w=majority"
client = pym.MongoClient(url)
db = client['arya_database']
collection_b = db['b']

prev = {"name" : "Ashish"}
# collection_b.delete_one(prev)
deleted = collection_b.delete_many(prev)
print(deleted.deleted_count)