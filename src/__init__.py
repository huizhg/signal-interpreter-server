import logging.config
import yaml
import os

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.join(CURRENT_DIR, "..")

LOG_SETTING_PATH = os.path.join(ROOT_DIR, "cfg", "log_config.yaml")

with open(LOG_SETTING_PATH, "r") as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
