import argparse
from src.utils.customLogger import customLogger
import os 
import shutil
import pandas as pd
from src.utils.configHandler import configHandler
from src.utils.common import read_schema

STAGE = "DATA_VALIDATION"  #Stage name for logs 
clg = customLogger(appname="TRAINING")
logger = clg.getLogger()
cf = configHandler()
cf.section('BASE_LOG_DIR')

class validate_data():

    def __init__(self,src_data_path) -> None:
        self.src_data_path = src_data_path

        self.NumberofColumns = read_schema("NumberofColumns")

    def validateColumnLength(self):
       
        try:
            logger.log(f,"Column Length Validation Started!!")
            for file in os.listdir(self.src_data_path):
                file_path = os.path.join(self.src_data_path,file)
                logger.log(f"reading file - {file_path}")
                csv = pd.read_csv(file_path)
                if csv.shape[1] == self.NumberofColumns:
                    pass
                else:
                    shutil.move("Training_Raw_files_validated/Good_Raw/" + file, "Training_Raw_files_validated/Bad_Raw")
                    logger.log(f, "Invalid Column Length for the file!! File moved to Bad Raw Folder :: %s" % file)
            logger.log(f, "Column Length Validation Completed!!")
        except OSError:
            f = open("Training_Logs/columnValidationLog.txt", 'a+')
            logger.log(f, "Error Occured while moving the file :: %s" % OSError)
            f.close()
            raise OSError
        except Exception as e:
            f = open("Training_Logs/columnValidationLog.txt", 'a+')
            logger.log(f, "Error Occured:: %s" % e)
            f.close()
            raise e
        f.close()

    def validateMissingValuesInWholeColumn(self):
     
        try:
            f = open("Training_Logs/missingValuesInColumn.txt", 'a+')
            logger.log(f,"Missing Values Validation Started!!")

            for file in os.listdir('Training_Raw_files_validated/Good_Raw/'):
                csv = pd.read_csv("Training_Raw_files_validated/Good_Raw/" + file)
                count = 0
                for columns in csv:
                    if (len(csv[columns]) - csv[columns].count()) == len(csv[columns]):
                        count+=1
                        shutil.move("Training_Raw_files_validated/Good_Raw/" + file,
                                    "Training_Raw_files_validated/Bad_Raw")
                        logger.log(f,"Invalid Column for the file!! File moved to Bad Raw Folder :: %s" % file)
                        break
                if count==0:
                    csv.rename(columns={"Unnamed: 0": "Wafer"}, inplace=True)
                    csv.to_csv("Training_Raw_files_validated/Good_Raw/" + file, index=None, header=True)
        except OSError:
            f = open("Training_Logs/missingValuesInColumn.txt", 'a+')
            logger.log(f, "Error Occured while moving the file :: %s" % OSError)
            f.close()
            raise OSError
        except Exception as e:
            f = open("Training_Logs/missingValuesInColumn.txt", 'a+')
            logger.log(f, "Error Occured:: %s" % e)
            f.close()
            raise e
        f.close()


if(__name__ == "__main__"):
    try:
        logger.info(f">>>> Stage {STAGE} Started <<<<")
        args = argparse.ArgumentParser()
        path = cf.section('DEFAULT_DATA_DIR')
        args.add_argument("--srcpath", "-sp", default=path)
        parsed_args = args.parse_args()

        val = validate_data(src_data_path=parsed_args.srcpath)
        val.validateColumnLength()
        val.validateMissingValuesInWholeColumn()
        logger.info(f">>>> Stage {STAGE} Completed <<<<")

    except Exception as e:
        logger.exception("Data Validation Failed: %s",e)
        raise e