from src.datascienceproject.config.configuration import ConfigurationManager
from src.datascienceproject.components.data_transformation import DataTransformation
from src.datascienceproject import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):  
        try:
            with open("artifacts/data_validation/status.txt", "r") as f:
                status = f.read().split(" ")[-1]
                print(f"Status = {status}")
                if status.strip() == "True":
                    config=ConfigurationManager()
                    data_transformation_config = config.get_data_transformation_config()
                    data_transformation = DataTransformation(config=data_transformation_config)
                    data_transformation.train_test_spliting()
                else:
                    raise Exception("Your data schema is not valid")
 
        except Exception as e:
            logger.exception(e)
            raise e


     