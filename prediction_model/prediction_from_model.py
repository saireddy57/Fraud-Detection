import pandas
import pandas as pd
from sklearn.preprocessing import StandardScaler
from file_methods.file_method import file_operations
from DataPreproccesing.clustering import Cluster
from predict_data_from_db.pred_data_db import data_getter
from DataPreproccesing.datapreproccess import data_preproccess

class model_predict:

    def data_prediction(self):
        try:
            dataframe = data_getter.data_from_db(self)
            print("data88888***************************************Frame",dataframe)
            data_frame = data_preproccess.treat_special_char_to_nan(self,dataframe)
            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::",data_frame)
            df= data_preproccess.replacingnull_value(self,data_frame)
            print("d+++++++++++++++++++++++++++++++++++++++++++++++++++++++++f",df)
            dat_fr = data_preproccess.encode_categorical_to_num(self,df)
            print("std------------------------------------------dataaaaaaaaaaaaaaaaaaa",dat_fr)
            df_std = data_preproccess.standardise_data(self,dat_fr)
            print("df_stdddddddddddddddddddddddddddddddddddddddddddd",df_std.columns)

            model = file_operations.load_model(self,'KMeans')
            print("mo----------------------------------------------dels",model)
            cluster = model.predict(df_std)
            print("cliustersssssssssssssssssssssssssssssssssssssss",cluster)
            df_std['Cluster']=cluster
            print("df---------------with------------------------clusterssssssss",df_std,df_std['Cluster'].unique())
            df_std.to_csv("FInalFIleeeeeee.csv")
            predictions =[]
            for i in df_std['Cluster'].unique():
                cluster_data =df_std.drop(['Cluster'],axis=1)
                model_name = 'XGBoost Model'
                model = file_operations.load_model(self,model_name)
                print("Final-------------------------------------Model",model,model_name,cluster_data)
                result = model.predict(cluster_data)
                for res in result:
                    print("ressssssssssssssssssssssssssssssssssssssssss",res)
                    if res ==0:
                        predictions.append('N')
                    else:
                        predictions.append('Y')
                print("Pred-------------------------------ctions",predictions)
                final = pd.DataFrame(list(zip(predictions)),columns=['Predictions'])
                # path = "Prediction_Output_File/Predictions.csv"
                final.to_csv("Prediction_Output_File/Predictions.csv", header=True,
                             mode='a+')  # appends result to prediction file

            return "Prediction_Output_File/Predictions.csv"
        except Exception as e:
            print(e)

