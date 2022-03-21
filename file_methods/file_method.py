import pickle
import os
import shutil


class file_operations:
    def __init__(self,model_path):
        pass


    def save_model(self,model,file_name):
        self.model_path = 'models/'
        try:
            path = os.path.join(self.model_path,file_name) #create and joins with the model file path and seperate directory for each cluster
            if os.path.isdir(path):
                shutil.rmtree(self.model_path)
                os.makedirs(path)
            else:
                os.makedirs(path)
            with open(path +'/'+file_name + '.sav' ,'wb') as f:
                pickle.dump(model,f) # Save Model To The File
        except Exception as e:
            print(e)

    def load_model(self,file_name):
        self.model_path = 'models/'
        try:
            with open(self.model_path + file_name + '/'+file_name +'.sav','rb') as f:
                self.model_loaded = pickle.load(f)
                return self.model_loaded
        except Exception as e:
            print(e)

