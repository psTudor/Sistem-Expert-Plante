
import os
import requests
import json
import logging
import sys
import os
from api_key import (IMAGE_KEY, IMAGE_URL)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import (
    FILE_NOT_FOUND_MSG, GENERIC_ERROR, NO_IDENTIFICATION_RESULTS,
    API_ERROR_BODY, API_ERROR_STATUS, IMAGE_FILE_NOT_FOUND, PLANT_IDENTIFICATION_ERROR
)

def identify_plant(image_path: str) -> str:
    try:
        # PlantNet API key
        api_key = IMAGE_KEY

        # URL-ul API
        api_url = IMAGE_URL

        # Parametrii request
        params = {
            'api-key': api_key,
            'include-related-images': 'false',
            'no-reject': 'false',
            'lang': 'ro',  # rezultate in romana
        }

        try:
            with open('data/plants.json', 'r', encoding="utf-8") as f:
                plants_data = json.load(f)['plants']
        except FileNotFoundError:
            plants_data = {}
            logging.error(FILE_NOT_FOUND_MSG.format(
                path='data/plants.json'))

        with open(image_path, 'rb') as image_file:
            files = {'images': (os.path.basename(
                image_path), image_file, 'image/jpeg')}

            # Request API
            response = requests.post(api_url, params=params, files=files)

        if response.status_code == 200:
            data = response.json()
            if 'results' in data and len(data['results']) > 0:
                top_result = data['results'][0]
                score = top_result['score']
                scientific_name_from_api = top_result['species']['scientificNameWithoutAuthor']
                identified_plant_name = None

                for plant, details in plants_data.items():
                    if 'keywords' in details and any(kw.lower() in scientific_name_from_api.lower() for kw in details['keywords']):
                        identified_plant_name = plant
                        break

                if identified_plant_name:
                    print(
                        f"Plantă identificată (din baza de date): {identified_plant_name}")
                    print(f"Nume științific (API): {scientific_name_from_api}")
                    print(f"Scor de încredere: {score:.2f}")
                    return {
                        "plant_name": identified_plant_name,
                        "scientific_name": scientific_name_from_api
                    }
                else:
                    common_names = top_result['species'].get('commonNames', [])
                    plant_name_from_api = common_names[0] if common_names else scientific_name_from_api
                    print(f"Plantă identificată (API): {plant_name_from_api}")
                    print(f"Nume științific: {scientific_name_from_api}")
                    print(f"Scor de încredere: {score:.2f}")
                    return {
                        "plant_name": plant_name_from_api,
                        "scientific_name": scientific_name_from_api
                    }
            else:
                logging.warning(NO_IDENTIFICATION_RESULTS)
                return {"plant_name": "Nu am putut identifica planta.", "scientific_name": None}
        else:
            logging.error(API_ERROR_STATUS.format(
                status_code=response.status_code))
            logging.error(API_ERROR_BODY.format(response_text=response.text))
            return {"plant_name": PLANT_IDENTIFICATION_ERROR, "scientific_name": None}

    except FileNotFoundError:
        logging.error(IMAGE_FILE_NOT_FOUND)
        return {"plant_name": IMAGE_FILE_NOT_FOUND, "scientific_name": None}
    except Exception as e:
        logging.exception("Unexpected error")
        return GENERIC_ERROR.format(error=str(e))


def plant_exists_in_database(plant_name: str) -> bool:
    try:
        with open('data/plants.json', 'r', encoding='utf-8') as f:
            plants_data = json.load(f)['plants']

        plant_name_lower = plant_name.lower()

        if plant_name_lower in [name.lower() for name in plants_data.keys()]:
            return True

        for plant_info in plants_data.values():
            if 'keywords' in plant_info:
                keywords = [kw.lower() for kw in plant_info['keywords']]
                if plant_name_lower in keywords:
                    return True

        return False
    except Exception:
        return False


if __name__ == '__main__':
    image_path = 'backend/res/1.jpg'
    plant = identify_plant(image_path)
    print(f"Rezultat final: {plant}")
