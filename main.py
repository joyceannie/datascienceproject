from src.datascienceproject import logger
from src.datascienceproject.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascienceproject.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascienceproject.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascienceproject.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.datascienceproject.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline


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

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>>> Starting {STAGE_NAME} <<<<<<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.initiate_data_transformation()
    logger.info(f">>>>>>> {STAGE_NAME} completed <<<<<<<<<<\n***************************************\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training Stage"
try:
    logger.info(f">>>>>>> Starting {STAGE_NAME} <<<<<<<<<<")
    obj = ModelTrainerPipeline()
    obj.initiate_model_trainer()
    logger.info(f">>>>>>> {STAGE_NAME} completed <<<<<<<<<<\n***************************************\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>>>> Starting {STAGE_NAME} <<<<<<<<<<")
    obj = ModelEvaluationPipeline()
    obj.initiate_model_evaluation()
    logger.info(f">>>>>>> {STAGE_NAME} completed <<<<<<<<<<\n***************************************\n")
except Exception as e:
    logger.exception(e)
    raise e