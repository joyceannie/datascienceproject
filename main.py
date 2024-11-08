from src.datascienceproject import logger
from src.datascienceproject.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascienceproject.pipeline.data_validation_pipeline import DataValidationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>> Starting {STAGE_NAME} <<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>>>> {STAGE_NAME} completed <<<<<<<<<<\n***************************************\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>>> Starting {STAGE_NAME} <<<<<<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.initiate_data_validation()
    logger.info(f">>>>>>> {STAGE_NAME} completed <<<<<<<<<<\n***************************************\n")
except Exception as e:
    logger.exception(e)
    raise e