from src.DSProject.logger import logging
from src.DSProject.exception import CustomException
from src.DSProject.components.data_ingestion import DataIngestion
from src.DSProject.components.data_transformation import DataTransformation
from src.DSProject.components.model_trainer import ModelTrainer

import sys


if __name__ == "__main__":
    logging.info("The execution has started")

    try:
        # Data Ingestion
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        logging.info(f"Train data path: {train_data_path}")
        logging.info(f"Test data path: {test_data_path}")

        # Data Transformation
        data_transformation = DataTransformation()
        train_arr, test_arr, _ = data_transformation.initiate_data_transormation(train_data_path, test_data_path)

        # Model Training
        model_trainer = ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr, test_arr))

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(str(e), sys)