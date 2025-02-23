from pymongo import MongoClient
from typing import Dict, List, Optional

class KnowledgeBase:
    def __init__(self):
        connection_string = "mongodb+srv://tudorpascaru1:plants5@plants.y138r.mongodb.net/?retryWrites=true&w=majority&appName=Plants"
        self.client = MongoClient(connection_string)
        self.db = self.client.plant_expert
        self.collection = self.db.plant

    def get_plant_info(self, plant_name: str) -> Optional[Dict]:
        return self.collection.find_one({"name": plant_name.lower()})

    def get_basic_care(self, plant_name: str) -> Optional[Dict]:
        plant = self.get_plant_info(plant_name)
        return plant.get('cerinte_baza') if plant else None

    def get_care_aspect(self, plant_name: str, aspect: str) -> Optional[Dict]:
        basic_care = self.get_basic_care(plant_name)
        return basic_care.get(aspect) if basic_care else None

    def get_problem_details(self, plant_name: str, problem: str) -> Optional[Dict]:
        plant = self.get_plant_info(plant_name)
        if plant and 'probleme_comune' in plant:
            return plant['probleme_comune'].get(problem)
        return None

    def get_all_plants(self) -> List[str]:
        return [plant['name'] for plant in self.collection.find({}, {"name": 1})]
    