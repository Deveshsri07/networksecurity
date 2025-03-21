import os
import sys
import pandas as pd
import numpy as np


'''DEFining common constant variable for training pipeline
'''
TARGET_COLUMN ="Result"
PIPELINE_NAME :str = "NetworkSeurity"
ARTIFACT_DIR: str = "Artifacts"
FILE_NAME: str =  "phisingData.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str ="test.csv"



'''
data ingestion related constant start with data_ingestion var name
'''

DATA_INGESTION_COLLECTION_NAME: str = "NetworkData"
DATA_INGESTION_DATABASE_NAME: str = "DEVESHSRI"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION : float = 0.2
