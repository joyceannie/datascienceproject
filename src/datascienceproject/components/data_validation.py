import os
from src.datascienceproject import logger
import pandas as pd
from src.datascienceproject.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    
    def validate_all_columns(self) -> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()
            with open(self.config.STATUS_FILE, "w") as f:
                for col in all_cols:
                    if col not in all_schema:
                        validation_status = False
                        f.write(f"Validation status for column = {col}: {validation_status}\n")
                    else:
                        validation_status = True
                        f.write(f"Validation status for column = {col}: {validation_status}\n")
            return validation_status

        except Exception as e:
            raise e
