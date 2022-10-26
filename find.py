import pymongo as pym
url = "mongodb+srv://aryatito:Tito%40420@cluster0.5viwfw1.mongodb.net/?retryWrites=true&w=majority"
client = pym.MongoClient(url)
db = client['arya_database']
collection_b = db['b']
# mydict = { "name": "Arya", "marks" : "18"}
# x = collection_a.find_one(mydict)
mydict = { "name": "Arya"}
x = collection_b.find(mydict, {"name" : 1, "_id" : 0, "marks" : 1}).limit(1)

print(collection_b.count_documents(mydict))
for item in x :
    print(item)