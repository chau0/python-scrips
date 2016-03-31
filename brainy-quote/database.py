from pymongo import MongoClient

class MongoConnector:
    def __init__(self,host,port,dbname,collection_name):
        self.client = MongoClient(host,port)
        self.dbname = dbname
        self.collection_name = collection_name

    def insert_quote(self,author,content,topic):
        mydb = self.client[self.dbname]
        new_record = {
           "author":author,
           "content":content,
           "topic":topic
        }
        mydb[self.collection_name].insert(new_record)

