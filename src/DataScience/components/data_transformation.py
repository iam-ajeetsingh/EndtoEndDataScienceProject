import os
from src.DataScience import logger
import pandas as pd
from src.DataScience.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    ## Note: We can add different data transformation techniques such as Scaler, PCA and others.
    # We can perform all kinds of EDA in ML cycle here before passing this data to the model

    # Presently we are just splitting the data into train and test sets, as data is cleaned and ready for training

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data)   # default test_size is 0.25. 

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(f"Training Data Shape is : {train.shape}")
        print(f"Test Data Shape is : {test.shape}")