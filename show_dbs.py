import pymongo as pym
url = "mongodb+srv://aryatito:Tito%40420@cluster0.5viwfw1.mongodb.net/?retryWrites=true&w=majority"
client = pym.MongoClient(url)
all_dbs = client.list_database_names()
print(all_dbs)

# collections - tables
db = client['arya_database']
print(db.list_collection_names())