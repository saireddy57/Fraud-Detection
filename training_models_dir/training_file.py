import pandas as pd
from DataPreproccesing.datapreproccess import data_preproccess
from MongoDB.dboperations import db_operation
from DataPreproccesing.clustering import Cluster
from sklearn.model_selection import train_test_split
from model_building import model_build
from app_log import logger


class train_model:

    def __init__(self):
        self.log = logger.app_log()
        self.file_obj = open('Training FIle Logs.txt','w')


    def training_models(self):
        try:
            good_path = "TrainingInputFile.csv"
            data_frame = data_preproccess.treat_special_char_to_nan(self, good_path)
            # print("SSSSSSSSSSSSSSEEEEEEEEEEEEEEEEEE----------------------------NNNNNNOnee",data_frame)
            data_set = data_preproccess.replacingnull_value(self, data_frame)

            final_dataframe = data_preproccess.encode_categorical_to_num(self, data_set)

            x,y = data_preproccess.splitting_data_test_train(self,final_dataframe,'fraud_reported')

            x_sample,y_sample = data_preproccess.treat_imbalanced_data(self,x,y)

            final_df_to_dict = final_dataframe.to_dict(orient='records')
            # db_operation.create_collection(self,"InsuranceData","CLeaned Data",final_df_to_dict)
            # print("Load-model------------------------------------------DATA VALIDATION",train_main_validation)
            df_db = db_operation.find_data_from_db(self, "InsuranceData", "CLeaned Data")
            df_from_db = pd.DataFrame.from_dict(df_db)
            print("df-----------------------from_______________db",df_from_db)
            df_from_db.to_csv("FinalCSVFile.csv")
            knee_value = Cluster.elbow_plot(self,x_sample,y_sample)
            Cluster.create_clusters(self,knee_value,x_sample,y_sample)
            x_sample['fraud_reported'] = y_sample
            # print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII",x_sample.columns)

            list_of_cluster = x_sample['Cluster'].unique()
            # print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV",list_of_cluster.sort())
            for cluster in list_of_cluster:
                cluster_df = x_sample[x_sample['Cluster'] ==cluster]
                # print("Cluster------------------------------------------db",cluster_df)
                x_cluster = cluster_df.drop(['Cluster','fraud_reported'],axis=1)
                y_cluster = cluster_df['fraud_reported']
                # print("CLLLLLLLLLLLLLUUUUUUUUUUUUUUUUUUUUUUSSSSSSSSSSSSTTTTTTTTTTERRRRRRRRRRRRRRRRRRR",x_cluster.shape)
                train_x,test_x,train_y,test_y = train_test_split(x_cluster,y_cluster,test_size=1 / 3, random_state=355)
                # print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",train_x,test_x,train_y,test_y)
                x_train = data_preproccess.standardise_data(self,train_x)
                # y_train = data_preproccess.standardise_data(self,train_y)
                x_test = data_preproccess.standardise_data(self,test_x)
                # print("yyyyyyyyyyyyyyyyyyyyyyyyy-----------------------------------train",x_test)
                model_att = model_build.model_creation()
                model_att.find_best_params(x_train,train_y,x_test,test_y)


        except Exception as e:
            print(e)
