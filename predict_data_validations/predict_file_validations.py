import os
import json

import pandas as pd

from app_log.logger import app_log
from predict_validation.predict_validate import predict_main_validation
from MongoDB.dboperations import db_operation
from  DataPreproccesing.datapreproccess import data_preproccess


class predict_validate(predict_main_validation):
    def __init__(self):
        self.logger = app_log

    def regex_val(self):
        # file_obj = open('PredictionLogs/Prediction Data Validation.txt', 'a+')
        regex = "['fraudDetection']+['\_'']+[\d_]+[\d]+\.csv"
        log_message = "Entered the regex sub function"
        # app_log.log(self,file_obj,log_message)
        # file_obj.close()
        print("re---------------------------gex",regex)
        return regex

    def load_from_schema(self):
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

    def predict_val(self,list,file_path):
        try:
            regex = self.regex_val()
            lengthofdatestamp,lengthoftimestamp,no_of_col,col_name = self.load_from_schema()
            print(dir(predict_main_validation))
            predict_main_validation.raw_predict_validation(self,lengthofdatestamp,lengthoftimestamp,no_of_col,col_name,regex,list,file_path)
            predict_main_validation.columns_validation(self,no_of_col,col_name,list,file_path)
            predict_main_validation.handling_missing_values(self,list,file_path)
            good_file_path = 'PredictionFiles\GoodRawData'
            file_name = os.listdir(good_file_path)
            df = pd.read_csv(good_file_path + '\\''' +file_name[0])

            # COnverting a DataFrame to Dictionary
            df_to_dict = df.to_dict(orient="records")
            db_operation.create_db(self,"InsuranceData",'Prediction Data',df_to_dict)
            dataframe = db_operation.find_data_from_db(self,"InsuranceData",'Prediction Data')
            df = pd.DataFrame.from_dict(dataframe)
            df.to_csv('PredictionFile.csv')
            print("df---------------------------------------predict",df)

        except Exception as e:
            print(e)

