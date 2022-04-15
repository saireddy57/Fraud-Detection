import os
import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from app_log.logger import app_log
from feature_engine.imputation import CategoricalImputer
from statistics import mode
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler
from sklearn.preprocessing import StandardScaler

class data_preproccess:

    def __init__(self):
        pass

    def treat_special_char_to_nan(self,good_path):
        try:
            # file_name = os.listdir(good_path)
            # df = pd.read_csv(good_path + file_name[0])
            df = pd.read_csv(good_path)
            # print("CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC",df)
            # list of columns not useful for the prediction
            list_of_col = ['policy_number','policy_bind_date','policy_state','insured_zip','incident_location','incident_date','incident_state','incident_city','insured_hobbies','auto_make','auto_model','auto_year','age','insured_zip']
            df_final = df.drop(list_of_col, axis=1)
            # Replace '?' with np.nan values in dataset
            df_final_data = df_final.replace("'?'", np.nan)
            #list of the columns having the np.nan values
            # list_nan_col = [i for i in df.columns if df[i].isna().sum()>0]
            # print("GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",df_final_data)
            return df_final_data
        except Exception as e:
            print(e)

        # list_col_null = [i for i in df.columns if df[i].isna()]
        # print("lissssssssssst----------------------colllllllllll-----------------null",list_col_null)

    def replacingnull_value(self,df):
        try:
            # print("data&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&Frame",df)
            list_col_null = [i for i in df.columns if df[i].isna().sum()>1]
            self.null_df = pd.DataFrame()
            # print("listUUU*****************************cal",list_col_null)
            for null_col in list_col_null:
                if df.isna().sum()[null_col]>0:
                    self.null_df['Nullvalue_col'] = null_col
                    self.null_df['Null_value_count'] = df.isna().sum()[null_col]
                    self.null_df.to_csv('NullValuesInfo.csv')
                # print("mod------------------------------------repace------------",self.null_df)
                #
                # print("Nullll--------------------------------------Fataframe", null_col, df.isna().sum()[null_col])
                df[null_col] = df[null_col].replace(np.nan,df[null_col].mode()[0])


            return df
        except Exception as e:
            print(e)

    def encode_categorical_to_num(self,dataframe):
        # print("ccvvvvvvvvvvvvvvv00000000000000000000000000000000000000000000000",dataframe)
        try:
            df = dataframe
            num_df = df[[col for col in df.columns if df[col].dtype == 'int64']]
            # print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",[col for col in df.columns if df[col].dtype == 'int64'])
            cat_df = df[[col for col in df.columns if df[col].dtype == 'O']]
            # init the label_encodeing class
            cat_df_list = [col for col in df.columns if df[col].dtype == 'O']
            lb_encode = LabelEncoder()
            # print("lllllllllllllbbbbbbbbbbbbbbb----------------------encode",lb_encode)
            for col in cat_df_list:
                # print("CDVVVVVVVVVVVVVVVVNNNNNNNNNNNNNNN---------------KKKKKKKKKKKKKKKK",col)
                cat_df[col] = lb_encode.fit_transform(cat_df[col])


            # custom mapping for encoding
            # cat_df['policy_csl'] = cat_df['policy_csl'].map({'100/300': 1, '250/500': 2.5, '500/1000': 5})
            # cat_df['insured_education_level'] = cat_df['insured_education_level'].map(
            #     {'JD': 1, 'High School': 2, 'College': 3, 'Masters': 4, 'Associate': 5, 'MD': 6, 'PhD': 7})
            # cat_df['incident_severity'] = cat_df['incident_severity'].map(
            #     {'Trivial Damage': 1, 'Minor Damage': 2, 'Major Damage': 3, 'Total Loss': 4})
            # cat_df['insured_sex'] = cat_df['insured_sex'].map({'FEMALE': 0, 'MALE': 1})
            # cat_df['property_damage'] = cat_df['property_damage'].map({'NO': 0, 'YES': 1})
            # cat_df['police_report_available'] = cat_df['police_report_available'].map({'NO': 0, 'YES': 1})
            # cat_df['fraud_reported'] = cat_df['fraud_reported'].map({'N': 0, 'Y': 1})
            #
            # for i in cat_df.drop(columns=['policy_csl', 'insured_education_level', 'incident_severity', 'insured_sex',
            #                               'property_damage', 'police_report_available', 'fraud_reported']).columns:
            #     cat_df = pd.get_dummies(cat_df, columns=[i])
            # print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",type(cat_df),type(num_df))
            final_df = pd.concat([num_df,cat_df],axis =1)
            # print("KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK",final_df)
            return final_df
        except Exception as e:
            print(e)

    def splitting_data_test_train(self,df,label_col_name):
        try:
            x = df.drop([label_col_name],axis =1)
            y = df[label_col_name]
            # print("YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY",y)
            return x,y
        except Exception as e:
            print(e)

    def treat_imbalanced_data(self,x,y):
        try:
            ov_sam = RandomOverSampler()
            x_sampled,y_sample = ov_sam.fit_resample(x,y)
            # print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL",y_sample.value_counts())
            return x_sampled,y_sample
        except Exception as e:
            print(e)

    def standardise_data(self,data):
        try:
            std_scalar = StandardScaler()
            print("data----------------------------------type",type(data))
            if isinstance(data, pd.core.series.Series):
                # data.drop(['Cluster'])
                data_np = np.array(data).reshape(-1,1)
                std_data = std_scalar.fit_transform(data_np)
                # print("DDaseeeeeeeeeeeeeeeeeeeeeerrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr",std_data)

            else:
                self.data = data
                num_df = self.data[[col for col in self.data.columns if self.data[col].dtypes == 'int64']]
                # print("DDD))))))))))))))))))))))))))))DFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",num_df,num_df.columns)
                std_data = std_scalar.fit_transform(num_df)
                std_df = pd.DataFrame(std_data,columns=num_df.columns,index=num_df.index)
                self.data.drop(columns = num_df.columns,axis =1,inplace = True)
                final_df = pd.concat([self.data,std_df],axis=1)
                # print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",final_df)
            return final_df
        except Exception as e:
            print(e)


