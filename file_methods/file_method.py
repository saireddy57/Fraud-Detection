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
                print("remove---------------------treemodelsssssssssssssssss",path)
                shutil.rmtree(path)
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

    def find_correct_model(self,cluster_number):
        try:
            self.model_path = 'models/'
            self.cluster_number=cluster_number
            self.list_of_files=os.listdir(self.model_path)

            for self.file in self.list_of_files:
                try:
                    if (self.file.index(str(self.cluster_number)) != -1):
                        self.model_name = self.file
                except:
                    continue
            self.model_name = self.model_name.split('.')[0]

            return self.model_name
        except Exception as e:
            print(e)



