from pymongo import MongoClient
client = MongoClient('localhost',27017)

mydb = client['test-database-1']
import datetime
myrecord = {
    "author":"Duke",
    "title":"PyMongo",
    "tags":["MongoDB","PyMongo"],
    "date":datetime.datetime.utcnow()
}

record_id = mydb.mytable.insert(myrecord)
print(record_id)
print(mydb.collection_names())