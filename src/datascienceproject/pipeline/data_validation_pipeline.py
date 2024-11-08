from src.datascienceproject.config.configuration import ConfigurationManager
from src.datascienceproject.components.data_validation import DataValidation
from src.datascienceproject import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass


    def initiate_data_validation(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config = data_validation_config)
        data_validation.validate_all_columns()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> Starting {STAGE_NAME} <<<<<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>>>>> {STAGE_NAME} completed <<<<<<<<<<\n***************************************\n")
    except Exception as e:
        logger.exception(e)
        raise e
