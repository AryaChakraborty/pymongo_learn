import pymongo as pym
url = "mongodb+srv://aryatito:Tito%40420@cluster0.5viwfw1.mongodb.net/?retryWrites=true&w=majority"
client = pym.MongoClient(url)
db = client['arya_database']
collection_b = db['b']
# prev = {"name" : "Nitin"}
# nextt = {"$set":{"name" : "Amit"}}
# collection_b.update_one(prev, nextt)

updated = collection_b.update_many({"name" : "Arya"}, {"$set":{"marks" : "8"}})
print(updated.modified_count)