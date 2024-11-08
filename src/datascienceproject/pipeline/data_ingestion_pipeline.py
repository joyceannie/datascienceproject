from src.datascienceproject.config.configuration import ConfigurationManager
from src.datascienceproject.components.data_ingestion import DataIngestion
from src.datascienceproject import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> Starting {STAGE_NAME} <<<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>>> {STAGE_NAME} completed <<<<<<<<<<\n***************************************\n")
    except Exception as e:
        logger.exception(e)
        raise e
