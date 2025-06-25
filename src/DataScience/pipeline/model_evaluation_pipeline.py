from src.DataScience.config.configuration import ConfigurationManager
from src.DataScience.components.model_evaluation import ModelEvaluation
from src.DataScience import logger
from src.DataScience.constants import *


STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def initialize_model_evaluation(self):
        config = ConfigurationManager(
            config_filepath=CONFIG_FILE_PATH,
            params_filepath=PARAMS_FILE_PATH,
            schema_filepath=SCHEMA_FILE_PATH
        )
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()

