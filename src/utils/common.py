import os
import shutil
from zipfile import ZipFile
import logging
import json


def create_directories(path_to_directories: list) -> None:
    try:
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            logging.info(f"created directory at: {path}")
    except Exception as e:
        logging.error(f"failed to create directory at {path}")
        raise e

def save_json(path: str, data: dict) -> None:
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)

        logging.info(f"json file saved at: {path}")
    except Exception as e:
        logging.error(f"failed to save json file at {path}")
        raise e


def unzip_file(source: str, dest: str) -> None:
    try:
        logging.info(f"zip extraction started ....")
        
        with ZipFile(source,"r") as zip_f:
            zip_f.extractall(dest)
        
        logging.info(f"zip extracted from {source} to {dest}")
    except Exception as e:
        logging.error(f"zip extraction failed from {source} to {dest}")
        raise e

def remove_directory(path: str,dir_name: str) -> None:
    try:
        logging.info(f"Here to Remove dir {dir_name} from location - {path}")
        full_path = os.path.join(path, dir_name)

        if(os.path.isdir(full_path)):
            #can also use ignore_errors = True to ingnore file not found error 
            shutil.rmtree(full_path) 
            logging.info(f"Removed dir {dir_name} from path - {path}")
    
    except Exception as e:
        logging.error(f"failed to remove directory from location - {full_path}")
        raise e


def read_schema(schema_path: str) -> str:

    try:
        with open(schema_path, 'r') as f:
            dic = json.load(f)
            f.close()

        pattern = dic['SampleFileName']
        LengthOfDateStampInFile = dic['LengthOfDateStampInFile']
        LengthOfTimeStampInFile = dic['LengthOfTimeStampInFile']
        column_names = dic['ColName']
        NumberofColumns = dic['NumberofColumns']

        message ="LengthOfDateStampInFile:: %s" %LengthOfDateStampInFile + "\t" + "LengthOfTimeStampInFile:: %s" % LengthOfTimeStampInFile +"\t " + "NumberofColumns:: %s" % NumberofColumns + "\n"
        logging.log(message)

    except ValueError:
        logging.log("ValueError:Value not found inside schema_training.json")
        raise ValueError

    except KeyError:
        logging.log( "KeyError:Key value error incorrect key passed")
        raise KeyError

    except Exception as e:
        logging.log( str(e))
        raise e

    return LengthOfDateStampInFile, LengthOfTimeStampInFile, column_names, NumberofColumns





