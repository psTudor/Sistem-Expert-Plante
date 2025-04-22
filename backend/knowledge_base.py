"""
Modulul KnowledgeBase oferă acces la baza de cunoștințe despre plante și îngrijirea lor
"""
import json
import os


class KnowledgeBase:

    def __init__(self, data_file: str = "data/plants.json"):
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

    def get_all_plants(self) -> list:
        return list(self.data["plants"].keys())

    def get_plant_info(self, plant: str) -> dict:
        plant = plant.lower().strip()

        if plant in self.data["plants"]:
            return self.data["plants"][plant]

        for plant_name, plant_data in self.data["plants"].items():
            if "keywords" in plant_data:
                if plant in [kw.lower() for kw in plant_data["keywords"]]:
                    return plant_data
        return None

    def get_basic_care(self, plant: str) -> dict:
        plant_info = self.get_plant_info(plant)
        if plant_info and "cerinte_baza" in plant_info:
            return plant_info["cerinte_baza"]
        return None

    def get_problem_details(self, plant: str, problem: str) -> dict:
        plant_info = self.get_plant_info(plant)
        if not plant_info or "probleme_comune" not in plant_info:
            return None

        problem = problem.lower().strip()

        if problem in plant_info["probleme_comune"]:
            return plant_info["probleme_comune"][problem]

        # potrivire cu underscore
        problem_alt = problem.replace(" ", "_")
        if problem_alt in plant_info["probleme_comune"]:
            return plant_info["probleme_comune"][problem_alt]

        # potrivire fara underscore
        problem_alt2 = problem.replace("_", " ")
        if problem_alt2 in plant_info["probleme_comune"]:
            return plant_info["probleme_comune"][problem_alt2]

        for prob_key, prob_data in plant_info["probleme_comune"].items():
            prob_key_norm = prob_key.replace("_", " ")
            if problem in prob_key_norm or prob_key_norm in problem:
                return prob_data

        return None

    def get_care_aspect(self, plant: str, aspect: str) -> dict:
        basic_care = self.get_basic_care(plant)
        if not basic_care:
            return None

        aspect = aspect.lower().strip()

        if aspect in basic_care:
            return basic_care[aspect]

        aspect_mapping = {
            "apa": "udare", "irigare": "udare", "udat": "udare", "uda": "udare",
            "soare": "lumina", "luminozitate": "lumina", "iluminare": "lumina",
            "pamant": "substrat", "sol": "substrat", "mediu": "substrat",
            "temperatura": "temperatura", "caldura": "temperatura", "clima": "temperatura"
        }

        if aspect in aspect_mapping and aspect_mapping[aspect] in basic_care:
            return basic_care[aspect_mapping[aspect]]

        for aspect_key in basic_care.keys():
            if aspect in aspect_key or aspect_key in aspect:
                return basic_care[aspect_key]

        return None
