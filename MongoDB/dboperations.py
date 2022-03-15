import pymongo
import urllib
import pandas
from app_log.logger import app_log

class db_operation:

    def __init__(self):
        self.file_obj = app_log()

    password = "9526242237"
    client = pymongo.MongoClient(
        f"mongodb+srv://insurance:{password}@insurancedata.zfzwk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.test

    def create_db(self,db_name,collection_name,df):
       try:
            # COnnection string from the Mongo DB Atlas
            # password = "9526242237"
            # client = pymongo.MongoClient(
            #     f"mongodb+srv://insurance:{password}@insurancedata.zfzwk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
            # db = client.test
            client = db_operation.client
            #Create DataBase in mongoDb
            database_create = client[db_name]
            #Create Collection or tables inside the Database
            collect_name = database_create[collection_name]
            collect_name.insert_many(df)
       except Exception as e:
           print(e)

    def find_data_from_db(self,db_name,collection_name):
        try:
            query = {}
            database = db_operation.client[db_name]
            coll_name = database[collection_name]
            if query:
                for coll in coll_name.find(query):
                    print(coll)
            else:
                for coll in coll_name.find():
                    print(coll)
        except Exception as e:
            print(e)




