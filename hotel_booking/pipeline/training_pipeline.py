import sys, os 
from hotel_booking.logger import logging
from hotel_booking.exception import HotelBookingException
from hotel_booking.utils import get_collection_as_dataframe
from hotel_booking.entity import config_entity
from hotel_booking.components.data_ingestion import DataIngestion 

def start_training_pipeline():
    try:
        training_pipeline_config = config_entity.TrainingPipelineConfig()

        #data ingestion
        data_ingestion_config  = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        print(data_ingestion_config.to_dict())
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
    except Exception as e:
        raise HotelBookingException(error_message=e, error_detail=sys)