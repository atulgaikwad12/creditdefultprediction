import argparse
from src.utils.customLogger import customLogger
from src.utils.configHandler import configHandler
import mlflow
import mlflow.sklearn

STAGE = "MAIN"  #Stage name for logs 
clg = customLogger(appname="TRAINING")
logger = clg.getLogger()
cf = configHandler()

class mlflow_train_pipeline:

    def __init__(self,src_data_path) -> None:
        self.src_data_path = src_data_path

    def pipeline_main(self):
    
        with mlflow.start_run() as run:
            run_id = run.info.run_id
            logger.info(f"Run ID ={run_id}")
            mlflow.run(".","validate_data",parameters={"src_path" : self.src_data_path},use_conda="false")
            """
            mlflow.run(".","base_model_creation",use_conda="false")
            mlflow.sklearn.autolog()
            mlflow.run(".","training",use_conda="false")
            """
    
if(__name__ == "__main__"):
    try:
        # Adding default data set location as a default argument for trainning pipeline 
        args = argparse.ArgumentParser()
        path = cf.section('DEFAULT_DATA_DIR')
        args.add_argument("--srcpath", "-sp", default=path)
        parsed_args = args.parse_args()

        logger.info("\n*********MLFlow Credit Default Prediction**********")
        logger.info(f">>>> Stage {STAGE} Started <<<<")
        
        train = mlflow_train_pipeline(src_data_path=parsed_args.srcpath)
        train.pipeline_main()
        logger.info(f">>>> Stage {STAGE} Completed <<<<")
        


    except Exception as e:
        logger.exception("Training Pipeline Failed: %s",e)
        raise e