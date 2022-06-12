import os
from zipfile import ZipFile
import logging
import json


def create_directories(path_to_directories: list) -> None:
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        logging.info(f"created directory at: {path}")

def save_json(path: str, data: dict) -> None:
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logging.info(f"json file saved at: {path}")


def unzip_file(source: str, dest: str) -> None:
    logging.info(f"zip extraction started ....")
    
    with ZipFile(source,"r") as zip_f:
        zip_f.extractall(dest)
    
    logging.info(f"zip extracted {source} to {dest}")

