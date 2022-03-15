from flask import Flask,request,render_template,redirect
from flask import Response
import os
from app_log import logger
from raw_data_validations import raw_file_validations


app = Flask(__name__)

@app.route("/", methods = ['POST','GET'])
def home():
    return render_template('home.html')

@app.route('/train',methods = ['POST','GET'])
def train():
    if request.method == 'POST':
        file_path = request.form['filepath']
        list_dir = os.listdir(file_path)

        # Object init of raw validations

        train_val_obj = raw_file_validations.raw_validate()

        # Calling function to perform Data Validations

        train_val_obj.train_val(list_dir,file_path)
        # for  i in list_dir:
        #     print(i,type(i))
        #     print("dddddddddddddddduuuuuuuuuuuufggggggggggggggggggggg",i.split('_'),len(i.split('_')[1]),len(i.split('_')[2]))

        # print("tr-----------------------------ain",train_val_obj)

        print("SHai for youuuuuuuuuuuuuuuuul",file_path,list_dir)
    return "ENTERED TRAIN Succesfully"

if __name__ == "__main__" :
    app.run()