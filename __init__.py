"""init file to config logger"""
import os
import logging.config
import yaml


CURRENT_DIR = os.path.abspath(__file__)
SOURCE_DIR = os.path.join(CURRENT_DIR, "..")
ROOT_DIR = os.path.join(SOURCE_DIR, "..")

LOG_SETTING_PATH = os.path.join(ROOT_DIR, "cfg/log_config.yaml")

with open(LOG_SETTING_PATH,"r") as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
