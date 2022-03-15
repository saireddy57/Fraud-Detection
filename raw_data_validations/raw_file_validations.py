import os
import json

import pandas as pd

from app_log.logger import app_log
from raw_validation.train_validate import train_main_validation
from MongoDB.dboperations import db_operation



class raw_validate(train_main_validation):
    def __init__(self):
        self.logger = app_log

    def regex_val(self):
        file_obj = open('TrainingLogs/Raw Data Validation.txt', 'a+')
        regex = "['fraudDetection']+['\_'']+[\d_]+[\d]+\.csv"
        log_message = "Entered the regex sub function"
        app_log.log(self,file_obj,log_message)
        file_obj.close()
        return regex

    def load_from_train_schema(self):
        try:
            file = open('training_schema.json')
            dic = json.load(file)
            # print("jso--**************------on",dic)
            lengthofdatestamp = dic['LengthOfDateStampInFile']
            lengthoftimestamp = dic['LengthOfTimeStampInFile']
            no_of_col = dic['NumberofColumns']
            col_name = dic['ColName']
            file.close()
            return lengthofdatestamp,lengthoftimestamp,no_of_col,col_name
        except Exception as e:
            return e

    def train_val(self,list,file_path):
        try:
            regex = self.regex_val()
            lengthofdatestamp,lengthoftimestamp,no_of_col,col_name = self.load_from_train_schema()
            train_main_validation.raw_train_validation(self,lengthofdatestamp,lengthoftimestamp,no_of_col,col_name,regex,list,file_path)
            train_main_validation.columns_validation(self,no_of_col,col_name,list,file_path)
            train_main_validation.handling_missing_values(self,list,file_path)
            good_file_path = 'TrainingFiles\GoodRawData'
            file_name = os.listdir(good_file_path)
            print("file_________________________________name",file_name)
            df = pd.read_csv(good_file_path + '\\''' +file_name[0])

            # COnverting a DataFrame to Dictionary
            df_to_dict = df.to_dict(orient="records")
            # print("list---------------------dict",df_to_dict)
            # print("Data---------------------------------frame",df)
            db_operation.create_db(self,"InsuranceData",'Raw Data',df_to_dict)
            # print("Load-model------------------------------------------DATA VALIDATION",train_main_validation)
        except Exception as e:
            print(e)


