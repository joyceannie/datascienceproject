from src.datascienceproject import logger
from src.datascienceproject.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>> Starting {STAGE_NAME} <<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>>>> {STAGE_NAME} completed <<<<<<<<<<\n***************************************\n")
except Exception as e:
    logger.exception(e)
    raise e