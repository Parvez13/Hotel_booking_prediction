import pymongo
import pandas as pd 
import json 
from hotel_booking.config import mongo_client

DATA_FILE_PATH = "/config/workspace/Data/hotel_bookings.csv"
DATABASE_NAME = "hotel_database"
COLLECTION_NAME = "hotel_collection"

if __name__ == '__main__':
    df = pd.read_csv(DATA_FILE_PATH) 
    df.reset_index(drop=True, inplace=True)
    json_records=list(json.loads(df.T.to_json()).values())
    mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_records)