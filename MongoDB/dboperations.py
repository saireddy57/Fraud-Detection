import pandas as pd
import pymongo
import urllib
import pandas
from app_log.logger import app_log

class db_operation:

    def __init__(self):
        self.file_obj = app_log()

    pwd = "9526242237"

    def create_db(self,db_name,collection_name,df):
       try:
            # COnnection string from the Mongo DB Atlas
            password = db_operation.pwd
            client = pymongo.MongoClient(
                f"mongodb+srv://insurance:{password}@insurancedata.zfzwk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
            db = client.test
            #Create DataBase in mongoDb
            database_create = client[db_name]
            #Create Collection or tables inside the Database
            collect_name = database_create[collection_name]
            collect_name.delete_many({})
            collect_name.insert_many(df)
       except Exception as e:
           print(e)

    def find_data_from_db(self,db_name,collection_name):
        try:
            password = db_operation.pwd
            client = pymongo.MongoClient(
                f"mongodb+srv://insurance:{password}@insurancedata.zfzwk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

            dict_list =[]
            query = {}
            # database = client.list_database_names()
            print(str(db_name),client.list_database_names())
            database=client.get_database(db_name)
            print("Data------------base",database)
            # if str(db_name) in client.list_database_names():
            #     database = db_name
            coll_name = database[collection_name]
            if query:
                for coll in coll_name.find(query):
                    print(coll)
            else:
                for coll in coll_name.find():
                    # print(coll)
                    dict_list.append(coll)
                # print("lis----------------------------st",dict_list)
                # df = pd.DataFrame.from_dict(dict_list, orient='index')
                # print("Daaaaaaaaaaaaaaaat******************************Frame",df)
            return dict_list
        except Exception as e:
            print(e)




