import os
import yaml
import logging
import mlflow
from pathlib import Path
from datetime import datetime

class Base:

    def __init__(self):
        self.config = self._read_config()
        self.log_dir = self.config['paths']['log_dir']
        self.experiment_name = self.config['mlflow']['experiment_name']

        os.makedirs(self.log_dir, exist_ok=True)
        self.logger = self._setup_logger()

    def _read_config(self):
        with open(Path("config.yml"), "r") as file:
            return yaml.safe_load(file)

    def _setup_logger(self):
        current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        logger = logging.getLogger(self.__class__.__name__)
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(os.path.join(self.log_dir, f"{current_date}.log")),
            ]
        )

        return logger

    def setup_mlflow(self, experiment_name="default_experiment"):

        exp_id = mlflow.create_experiment(self.experiment_name).experiment_id
        mlflow.autolog(
            log_input_examples=True, 
            log_model_signatures=True, 
            log_models=True
        )
        return exp_id
"""
if __name__ == '__main__':
    base = Base()
    base.logger.info("Hello")
"""