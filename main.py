from src.logger import logging
from src.exception import CyberException
import os,sys
from src.utils import get_collection_as_dataframe
from src.entity.config_entity import DataIngestionConfig
from src.entity import config_entity
from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluation
from src.components.model_pusher import ModelPusher


if __name__=="__main__":
    try:
        #get_collection_as_dataframe(database_name="IOT_SENSOR_DATA",collection_name="SMOKE_DATA")
        training_pipeline_config = config_entity.TrainingPipelineConfig()
        data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        print(data_ingestion_config.to_dict())

        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion_artifact = data_ingestion.intitate_data_ingestion()



        #DATA Validation

        data_validation_config = config_entity.DataValidationConfig(training_pipeline_config=training_pipeline_config)
        data_validation = DataValidation(data_validation_config=data_validation_config,data_ingestion_artifact=data_ingestion_artifact)
        data_validation_artifact=data_validation.initiate_data_validation()



        #DATA TRANSFORMATION

        data_transformation_config = config_entity.DataTransformationConfig(training_pipeline_config=training_pipeline_config)
        data_transformation = DataTransformation(data_transformation_config=data_transformation_config,data_ingestion_artifact=data_ingestion_artifact)
        data_transformation_artifact=data_transformation.initiate_data_transformation()



        #Model trainer

        model_trainer_config = config_entity.ModelTrainerConfig(training_pipeline_config=training_pipeline_config)
        model_trainer = ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_tariner_artifact = model_trainer.initiate_model_trainer()




        #Model Evaluation

        model_evaluation_config = config_entity.ModelEvaluationConfig(training_pipeline_config=training_pipeline_config)
        model_evaluation = ModelEvaluation(model_eval_config=model_evaluation_config,
                                           data_ingestion_artifact=data_ingestion_artifact,
                                           data_transformation_artifact=data_transformation_artifact,
                                           model_trainer_artifact=model_tariner_artifact)
        model_eval_artifact = model_evaluation.initiate_model_evaluation()


          #Model Pusher

        model_pusher_config = config_entity.ModelPusherConfig(training_pipeline_config=training_pipeline_config)
        model_pusher = ModelPusher(model_pusher_config=model_pusher_config,
                                   data_transformation_artifact=data_transformation_artifact,
                                   model_trainer_artifact=model_tariner_artifact)
        model_pusher_artifact = model_pusher.initiate_model_pusher()

        


    except Exception as e:
        raise CyberException(e,sys)