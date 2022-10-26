import pymongo as pym
url = "mongodb+srv://aryatito:Tito%40420@cluster0.5viwfw1.mongodb.net/?retryWrites=true&w=majority"
client = pym.MongoClient(url)
db = client['arya_database']
collection_a = db['b']
mydict = { "name": "Ashish", "marks": "10" } # will be deleted
x = collection_a.insert_one(mydict)