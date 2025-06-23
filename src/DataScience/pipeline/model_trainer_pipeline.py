from src.DataScience.config.configuration import ConfigurationManager
from src.DataScience.components.model_trainer import ModelTrainer
from src.DataScience import logger
from src.DataScience.constants import *

STAGE_NAME = "Model Trainer stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def initialize_model_training(self):
        config = ConfigurationManager(
            config_filepath=CONFIG_FILE_PATH,
            params_filepath=PARAMS_FILE_PATH,
            schema_filepath=SCHEMA_FILE_PATH
        )
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()