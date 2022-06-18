import yaml
import logging
import os.path as path

class configHandler:
    
    def __init__(self) -> None:
        
        config_dir = "config/"
        config_file = "config.yaml"

        self.config_path = path.join(config_dir,config_file)
        if(path.isfile(self.config_path)):
            self.config = self.read_yaml(self.config_path)
        else:
            raise Exception("Failed to found and load file")

    def section(self,section):
        if(self.config is not None):
            return self.config[section]
        else: 
            raise Exception("Config data not found")

    def read_yaml(self,path_to_yaml) -> dict:
        try:
            logging.info(f"yaml file: {path_to_yaml} loading...")
            with open(path_to_yaml) as yaml_file:
                content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully")
            return content
        except Exception as e:
            raise Exception("Failed to safe load config file ",e)