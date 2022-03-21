# from raw_data_validations.raw_file_validations import raw_validate
from app_log.logger import app_log
import os
import re
import shutil
import pandas as pd
# from raw_data_validations.raw_file_validations import r


class train_main_validation:
    def __init__(self):
        self.logger = app_log()
        # self.raw_file_validations = raw_validate()

    def create_good_data_directory(self):
        dir_loc = "TrainingFiles\GoodRawData"
        # print("OOOOOOSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS",os.path.exists(dir_loc))
        # if os.path.exists(dir_loc):
        #     del



    def raw_train_validation(self,lengthofdatestamp,lengthoftimestamp,no_of_col,col_name,regex,list,file_path):
        try:
            self.create_good_data_directory()
            # print("SSSSSSSSEEEEEEEEEEEEELLLLLLLLLLLFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",self)
            # print("result------------------------------------------------------------------lt",lengthofdatestamp,lengthoftimestamp,no_of_col,col_name,regex,list)
            # print("Get-------------------------------------cwd",self.load_from_train_schema())
            # print("li----------------------------st",list,self.regex_val(),self.load_from_train_schema(),os.getcwd())
            for file_name in list:
                if re.match(regex,file_name):
                    # print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV",file_name)
                    list_filename = file_name.split('_')
                    list_dot = list_filename[2].split('.')
                    # print("______________________________________________",list_filename[1],lengthofdatestamp,list_dot[0],lengthoftimestamp,list_dot[1])
                    if len(list_filename[1]) == lengthofdatestamp and len(list_dot[0]) == lengthoftimestamp and list_dot[1] == 'csv':
                        # print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",file_name)
                        shutil.copy(file_path + '\\''' + file_name, 'TrainingFiles\GoodRawData')
                    else:
                        shutil.copy(file_path + '\\''' + file_name,'TrainingFiles\BadRawData')
                else:
                    shutil.copy(file_path + '\\''' + file_name,'TrainingFiles\BadRawData')
        except Exception as e:
            print(e)

    file_location = 'TrainingFiles\GoodRawData'

    def columns_validation(self,no_of_col,col_name,list,file_path):
        file_path = train_main_validation.file_location
        # print("kKKKKKKKKKKKKKkkkkkkkkkkkkkkKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKkkkkKKKKKKKKKKKKKKKKKpppppppppppppppppockmmmmnnnnnnnnnnnnnnnnnn",no_of_col,col_name,list,file_path)
        try:
            for file in os.listdir(file_path):
                # print("CCCCCCCCCCCOOOOOOOOOOOOOPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPIIIIIIIIIIIIIIIIIII",file)
                # print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSXXXXXXXXXXXXXXXSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS",file)
                df = pd.read_csv("TrainingFiles\GoodRawData" + '\\''' + file,encoding='latin1')
                # print("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",df.shape,df.columns)
                # for col in df:
                    # print("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",col,len(df[col]),df[col].count(),(len(df[col])-df[col].count()))
                if df.shape[1] != no_of_col:
                    pass
                    # shutil.move('TrainingFiles\GoodRawData' + '\\''' + file , 'TrainingFiles\BadRawData')

        except Exception as e:
            print(e)
    def handling_missing_values(self,list,file_path):
        file_path = train_main_validation.file_location
        try:
            count = 0
            for file in os.listdir(file_path):
                df = pd.read_csv("TrainingFiles\GoodRawData" + '\\''' + file, encoding='latin1')
                for col in df:
                    if (len(df[col])-df[col].count()) == len(df[col]):
                        # print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
                        shutil.move('TrainingFiles\GoodRawData' + '\\''' + file, 'TrainingFiles\BadRawData')
                    else:
                        # print("eeEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
                        pass
        except Exception as e:
            print(e)













