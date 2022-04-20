from flask import Flask,request,render_template,redirect
from flask import Response
import os
from app_log import logger
from raw_data_validations import raw_file_validations
from training_models_dir.training_file import train_model
from predict_data_validations import predict_file_validations
from prediction_model import prediction_from_model


app = Flask(__name__)

@app.route("/", methods = ['POST','GET'])
def home():
    return render_template('home.html')

@app.route('/predict',methods = ['POST'])
def predict_route():
    if request.method == 'POST':
        print("Pre--------------------------------------dictpredictttttttttttttttt",request.form)

        file_path = request.form['filepath']
        list_dir = os.listdir(file_path)
        print("list--------------dirprecdcict",list_dir)

        predict_val_obj = predict_file_validations.predict_validate()

        print("predict------------------------val-------------obj",predict_val_obj)
        predict_val_obj.predict_val(list_dir,file_path)

        predic_model = prediction_from_model.model_predict()

        path = predic_model.data_prediction()

        print("pa--------------------------------th",path)

    return Response("Prediction File created at %s!!!" % path)


@app.route('/train',methods = ['POST','GET'])
def train_route():
    if request.method == 'POST':
        file_path = request.form['filepath']
        list_dir = os.listdir(file_path)
        print("request-----------------------------------------form",request.form)

        # Object init of raw validations

        train_val_obj = raw_file_validations.raw_validate()

        # Calling function to perform Data Validations

        train_val_obj.train_val(list_dir,file_path)

        """Training Started"""

        traning_init = train_model()

        traning_init.training_models()

if __name__ == "__main__" :
    app.run()