# import argparse
from src.utils.customLogger import customLogger
import mlflow
import mlflow.sklearn

STAGE = "MAIN"  #Stage name for logs 
clg = customLogger(appname="TRAINNING")
logger = clg.getLogger()

def main():
 
    with mlflow.start_run() as run:
        run_id = run.info.run_id
        logger.info(f"Run ID ={run_id}")
        #mlflow run . --no-conda
        # mlflow.run(".","get_data",parameters={},use_conda="false") # alternate way to pass parameters
        """
        mlflow.run(".","get_data",use_conda="false")
        mlflow.run(".","base_model_creation",use_conda="false")
        mlflow.sklearn.autolog()
        mlflow.run(".","training",use_conda="false")
        """
    
if(__name__ == "__main__"):
    try:
        logger.info("\n*********MLFlow CNN classifier**********")
        logger.info(f">>>> Stage {STAGE} Started <<<<")
        main()
        logger.info(f">>>> Stage {STAGE} Completed <<<<")
        
        # ML Flow commands -p portnumber is optional
        #mlflow ui -p portnumber
        #mlflow models serve -m runs:/runid/model -p portnumber

    except Exception as e:
        logger.exception("Training Pipeline Failed: %s",e)
        raise e