import json
import os
from typing import Dict, Any, Optional, List

try:
    import firebase_admin
    from firebase_admin import credentials, firestore
    firebase_available = True
except ImportError:
    firebase_available = False


class KnowledgeBase:

    def __init__(self, data_file: str = "data/plants.json", firebase_credentials_path: Optional[str] = None):

        self.data = None
        self.db = None
        self.using_firebase = False

        self.data = None
        self.db = None
        self.using_firebase = False

        if firebase_credentials_path and firebase_available:
            try:
                if not firebase_admin._apps:
                    cred = credentials.Certificate(firebase_credentials_path)
                    firebase_admin.initialize_app(cred)

                self.db = firestore.client()
                self.using_firebase = True
                print("Firebase initializat cu succes.")
                self._load_data_from_firebase()

            except Exception as e:
                print(f"Eroare la initializarea Firebase: {str(e)}")
                print("Se va folosi fișierul JSON local ca backup.")
                self._load_data_from_file(data_file)
        else:
            self._load_data_from_file(data_file)

    def _load_data_from_file(self, data_file: str):
        try:
            if os.path.exists(data_file):
                with open(data_file, 'r', encoding='utf-8') as f:
                    self.data = json.load(f)
            else:
                alternative_path = "plants.json"
                if os.path.exists(alternative_path):
                    with open(alternative_path, 'r', encoding='utf-8') as f:
                        self.data = json.load(f)
                else:
                    raise FileNotFoundError(
                        f"Nu s-a găsit fișierul de date: {data_file} sau {alternative_path}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Eroare la parsarea JSON: {str(e)}")
        if not self.data or not isinstance(self.data, dict) or "plants" not in self.data:
            raise ValueError(
                "Format incorect al fișierului de date: lipsește cheia 'plants'")

    def _load_data_from_firebase(self):
        try:
            plants_ref = self.db.collection('plants').get()
            self.data = {"plants": {}}

            for doc in plants_ref:
                plant_data = doc.to_dict()
                self.data["plants"][doc.id] = plant_data

            print(
                f"Date încărcate din Firebase: {len(self.data['plants'])} plante găsite.")

        except Exception as e:
            raise ValueError(
                f"Eroare la încărcarea datelor din Firebase: {str(e)}")

    def get_all_plants(self) -> List[str]:
        return list(self.data["plants"].keys())

    def get_plant_info(self, plant: str) -> Optional[Dict[str, Any]]:
        plant = plant.lower().strip()

        if plant in self.data["plants"]:
            return self.data["plants"][plant]

        for plant_name, plant_data in self.data["plants"].items():
            if "keywords" in plant_data and plant in [kw.lower() for kw in plant_data.get("keywords", [])]:
                return plant_data

        return None

    def get_basic_care(self, plant: str) -> Optional[Dict[str, Any]]:
        plant_info = self.get_plant_info(plant)
        if plant_info and "cerinte_baza" in plant_info:
            return plant_info["cerinte_baza"]
        return None

    def get_problem_details(self, plant: str, problem: str) -> Optional[Dict[str, Any]]:
        plant_info = self.get_plant_info(plant)
        if not plant_info or "probleme_comune" not in plant_info:
            return None

        problem = problem.lower().strip()

        if problem in plant_info["probleme_comune"]:
            return plant_info["probleme_comune"][problem]

        # Potrivire cu underscore
        problem_alt = problem.replace(" ", "_")
        if problem_alt in plant_info["probleme_comune"]:
            return plant_info["probleme_comune"][problem_alt]

        # Potrivire fara underscore
        problem_alt2 = problem.replace("_", " ")
        if problem_alt2 in plant_info["probleme_comune"]:
            return plant_info["probleme_comune"][problem_alt2]

        for prob_key, prob_data in plant_info["probleme_comune"].items():
            prob_key_norm = prob_key.replace("_", " ")
            if problem in prob_key_norm or prob_key_norm in problem:
                return prob_data

        return None

    def get_care_aspect(self, plant: str, aspect: str) -> Optional[Dict[str, Any]]:
        basic_care = self.get_basic_care(plant)
        if not basic_care:
            return None

        aspect = aspect.lower().strip()

        if aspect in basic_care:
            return basic_care[aspect]

        aspect_mapping = {
            "apa": "udare", "irigare": "udare", "udat": "udare", "uda": "udare",
            "soare": "lumina", "luminozitate": "lumina", "iluminare": "lumina",
            "sol": "pamant", "mediu": "pamant",
            "temperatura": "temperatura", "caldura": "temperatura", "clima": "temperatura"
        }

        if aspect in aspect_mapping and aspect_mapping[aspect] in basic_care:
            return basic_care[aspect_mapping[aspect]]

        for aspect_key in basic_care.keys():
            if aspect in aspect_key or aspect_key in aspect:
                return basic_care[aspect_key]

        return None
