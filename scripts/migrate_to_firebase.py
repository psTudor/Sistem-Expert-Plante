import os
import sys
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.exceptions import GoogleCloudError
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='trace.log', encoding='utf-8', level=logging.DEBUG)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import (
    JSON_FILE_NOT_FOUND, PLANTS_DATA_MISSING, PLANTS_DATA_LOADED,
    FIREBASE_INIT_SUCCESS, FIREBASE_INIT_ERROR, PLANT_MIGRATION_SUCCESS,
    PLANT_MIGRATION_ERROR, MIGRATION_SUMMARY, JSON_PARSER_ERROR
)



def migrate_json_to_firebase(json_path="data/plants.json", firebase_credentials_path="credentials/plant-expert-cccb6-firebase-adminsdk-fbsvc-69b270c0e1.json"):
    try:
        with open(json_path, "r") as file:
            data = json.load(file)
            plants = data.get("plants", {})

        if not plants:
            logger.warning(PLANTS_DATA_MISSING)
            return False

        logger.info(PLANTS_DATA_LOADED.format(count=len(plants)))

    except FileNotFoundError:
        logger.error(JSON_FILE_NOT_FOUND.format(path=json_path))
        return False
    except json.JSONDecodeError as e:
        logger.error(JSON_PARSER_ERROR.format(error=str(e)))
        return False

    try:
        creds = credentials.Certificate(firebase_credentials_path)
        firebase_admin.initialize_app(creds)
        db = firestore.client()
        plants_collection = db.collection('plants')
        logger.info(FIREBASE_INIT_SUCCESS)
    except firebase_admin.exceptions.FirebaseError as e:
        logger.error(FIREBASE_INIT_ERROR.format(error=str(e)))
        return False

    success_count = 0
    for plant_name, plant_data in plants.items():
        try:
            plants_collection.document(plant_name).set(plant_data)
            logger.info(PLANT_MIGRATION_SUCCESS.format(plant=plant_name))
            success_count += 1
        except GoogleCloudError as e:
            logger.error(PLANT_MIGRATION_ERROR.format(
                plant=plant_name, error=str(e)))

    logger.info(MIGRATION_SUMMARY.format(
        success=success_count, total=len(plants)))
    return True


if __name__ == "__main__":
    migrate_json_to_firebase()
