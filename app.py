from flask import Flask, request, render_template
from flask import Response
import os
import mlflow
from flask_cors import CORS, cross_origin
from src.utils.customLogger import customLogger
from src.utils.configHandler import configHandler
from src.train_pipeline import mlflow_train_pipeline
# from prediction_Validation_Insertion import pred_validation
# from trainingModel import trainModel
# from training_Validation_Insertion import train_validation
# from predictFromModel import prediction

clg = customLogger(appname="TRAINNING")
logger = clg.getLogger()
cf = configHandler()

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

@app.route("/home", methods=['GET'])
@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRouteClient():
    try:
        if request.json is not None:
            path = request.json['filepath']
        elif request.form is not None:
            path = request.form['filepath']

        if path is not None and (os.path.isdir(path) or os.path.isfile(path)):
            # pred_val = pred_validation(path) #object initialization

            # pred_val.prediction_validation() #calling the prediction_validation function

            # pred = prediction(path) #object initialization

            # predicting for dataset present in database
            # path = pred.predictionFromModel()
            
            #Prediction_Output_File/Predictions.csv and few of the predictions are
            return Response("Prediction File created at %s!!!" % path)
        else:
            return Response("Provided path is invalid check once !!")

    except Exception as e:
        return Response("Error Occurred! %s" %e)



@app.route("/train", methods=['POST'])
@cross_origin()
def trainRouteClient():

    try:
        if request.json['filepath'] is not None:
            path = request.json['filepath']

            if(path is None):
                path = cf.section('DEFAULT_DATA_DIR')

            logger.info(f"starting trainning for data at - {path}")
            train = mlflow_train_pipeline(src_data_path=path)
            train.pipeline_main()
            # train_valObj = train_validation(path) #object initialization

            # train_valObj.train_validation() #calling the training_validation function


            # trainModelObj = trainModel() # object initialization
            # trainModelObj.trainingModel() # training the model for the files in the table

    except Exception as e:
        return Response("Error Occurred! %s" % e)

    return Response("Training successfull!!")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

port = int(os.getenv("PORT",5001))
if __name__ == "__main__":
    app.run(port=port,debug=True)
