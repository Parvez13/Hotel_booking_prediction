import pymongo 
import json 
from dataclasses import dataclass 
import os 

@dataclass 
class EnviromentVariable():
    mongo_db_url:str = os.getenv('MONGO_DB_URL')

env_var = EnviromentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
TARGET_COLUMN = "is_canceled"