import pandas as pd
from MongoDB.dboperations import db_operation

class data_getter:

    def __init__(self):
        pass

    def data_from_db(self):
        try:
            prediction_file_path = 'PredictionFile.csv'
            df = pd.read_csv(prediction_file_path)
            print("data--------------frame", df)
            return df
        except Exception as e:
            print(e)
