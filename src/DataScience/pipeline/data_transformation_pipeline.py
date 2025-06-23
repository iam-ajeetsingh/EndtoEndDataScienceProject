from src.DataScience.config.configuration import ConfigurationManager
from src.DataScience.components.data_transformation import DataTransformation
from src.DataScience import logger
from src.DataScience.constants import *
from pathlib import Path

STAGE_NAME="Data Trnasformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initialize_data_transformation(self):

        try:
            with open(Path("artifacts/data_validation/status.txt"),'r') as f:
                status=f.read().split(" ")[-1]

            if status=="True":
                config=ConfigurationManager(
                    config_filepath=CONFIG_FILE_PATH,
                    params_filepath=PARAMS_FILE_PATH,
                    schema_filepath=SCHEMA_FILE_PATH
                )
                data_transformation_config=config.get_data_transformation_config()
                data_transformation=DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
                
            else:
                raise Exception("Your data scheme is not valid")
            
        except Exception as e:
            print(e)