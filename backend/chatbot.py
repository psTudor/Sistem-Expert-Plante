import spacy
from knowledge_base import KnowledgeBase
from expert_system import PlantExpertSystem
from typing import Dict, List
from training_data import ENTITIES
import sys
import os
import logging
from constants import (
    PLANT_NOT_SPECIFIED, PLANT_NOT_FOUND,
    NEEDS_REPHRASE, GENERIC_ERROR, EXPERT_ERROR
)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class PlantCareBot:
    def __init__(self, model_path: str = "output/model-best"):
        self.nlp = spacy.load(model_path)
        self.kb = KnowledgeBase()
        self.expert_system = PlantExpertSystem()

        self.intent_keywords = {
            'problem': ['problema', 'cad', 'cazut', 'galben', 'putred', 'bolnav', 'pete', 'deteriorare'],
            'care': ['cum', 'cand', 'cat', 'trebuie', 'necesita', 'nevoie', 'ingrijire', 'ingrijesc'],
            'list_problems': ['ce probleme', 'lista probleme', 'toate problemele', 'probleme', "ce probleme apar"]
        }

        self.aspect_mappings = {

            'ud': 'udare', 'uda': 'udare', 'udat': 'udare', 'apa': 'udare',
            'luminozitate': 'lumina', 'soare': 'lumina',
            'sol': 'pamant', 'plantez': 'pamant', 'plantare': 'pamant', 'mediu': 'pamant', 'substrat' : 'pamant'
        }

        self.problem_mappings = {
            'cad frunze': 'cadere_frunze',
            'cad frunzele': 'cadere_frunze',
            'caderea frunzelor': 'cadere_frunze',
            'frunze galbene': 'frunze_galbene',
            'ingalbenire': 'frunze_galbene',
            'radacini putrede': 'radacini_putrede',
            'putrezire radacini': 'radacini_putrede',
            'pete maro': 'pete_maro',
            'pete maronii': 'pete_maro'
        }

        # Initializare baza de date cu plante
        self.base_plants = self.kb.get_all_plants()

    def preprocess_text(self, text: str) -> str:

        # Preproceseare pentru diacritice
        text = text.lower()
        diac_map = {'ă': 'a', 'â': 'a', 'î': 'i', 'ș': 's', 'ț': 't'}
        for k, v in diac_map.items():
            text = text.replace(k, v)
        return ' '.join(text.split())

    def identify_intent(self, text: str, entities: Dict[str, List[str]]) -> str:
        text = self.preprocess_text(text)

        list_problem_indicators = self.intent_keywords['list_problems']
        if any(keyword in text for keyword in list_problem_indicators):
            return 'list_problems'

        problem_indicators = self.intent_keywords['problem']
        if any(keyword in text for keyword in problem_indicators) or entities['PROBLEM']:
            return 'problem'

        care_indicators = self.intent_keywords['care']
        if any(keyword in text for keyword in care_indicators) or entities['CARE_ASPECT']:
            return 'care'

        return 'general'

    def extract_entities(self, text: str) -> Dict[str, List[str]]:
        doc = self.nlp(text)
        entities = {
            "PLANT": [],
            "CARE_ASPECT": [],
            "PROBLEM": [],
            "CONDITION": []
        }

        text_lower = self.preprocess_text(text.lower())

        # Cautare plante in text
        for plant in self.base_plants:
            if plant in text_lower:
                entities["PLANT"].append(plant)
                break

        for ent in doc.ents:
            if ent.label_ == "CARE_ASPECT":
                # Normalizare aspect de ingrijire folosind maparea
                ent_text = self.preprocess_text(ent.text.lower())
                norm_text = self.aspect_mappings.get(ent_text, ent_text)
                if norm_text not in entities["CARE_ASPECT"]:
                    entities["CARE_ASPECT"].append(norm_text)
            elif ent.label_ == "PROBLEM":
                # Normalizare problema folosind maparea
                ent_text = self.preprocess_text(ent.text.lower())
                norm_text = self.problem_mappings.get(ent_text, ent_text)
                if norm_text not in entities["PROBLEM"]:
                    entities["PROBLEM"].append(norm_text)

        for problem_text, problem_id in self.problem_mappings.items():
            if f" {problem_text} " in f" {text_lower} ":
                if problem_id not in entities["PROBLEM"]:
                    entities["PROBLEM"].append(problem_id)

        if any(word in text_lower for word in ["plantez", "plantat", "planta"]):
            entities["PROBLEM"] = []

        for aspect_text, aspect_id in self.aspect_mappings.items():
            if aspect_text in text_lower:
                if aspect_id not in entities["CARE_ASPECT"]:
                    entities["CARE_ASPECT"].append(aspect_id)

        if "uscat" in text_lower and "sol" not in text_lower and "pamant" not in text_lower:
            pass
        else:
            if any(word in text_lower for word in ["uscat", "sec", "uscata", "uscare"]):
                entities["CONDITION"].append("dry")
        if any(word in text_lower for word in ["umed", "umeda", "ud", "uda", "umiditate"]):
            entities["CONDITION"].append("wet")

        for key in entities:
            entities[key] = list(set(entities[key]))

        return entities

    def generate_response(self, text: str) -> str:
        try:
            entities = self.extract_entities(text)
            intent = self.identify_intent(text, entities)

            if not entities["PLANT"]:
                return PLANT_NOT_SPECIFIED

            plant = entities["PLANT"][0]

            plant_info = self.kb.get_plant_info(plant)
            if not plant_info:
                return PLANT_NOT_FOUND.format(plant=plant)

            if intent == 'list_problems':
                problems_list = self.kb.get_all_problems_for_plant(plant)
                if problems_list:
                    return (
                        f"Pentru {plant}, problemele comune identificate sunt: "
                        f"{', '.join(problems_list)}."
                    )
                else:
                    return f"Nu am găsit probleme comune înregistrate pentru {plant}."

            expert_response = self.expert_system.get_expert_response(
                entities=entities,
                intent=intent
            )

            if expert_response:
                if plant.lower() not in expert_response.lower():
                    return f"Pentru {plant}: {expert_response}"
                return expert_response

            basic_care = self.kb.get_basic_care(plant)
            if basic_care:
                return (
                    f"Pentru {plant}, iată informațiile de bază de îngrijire:\n"
                    f"- Udare: {basic_care['udare']['detalii']}\n"
                    f"- Lumină: {basic_care['lumina']['detalii']}\n"
                    f"- Pământ: {basic_care['pamant']['detalii']}"
                )

            return NEEDS_REPHRASE.format(plant=plant)

        except ValueError as e:
            logging.error("ValueError: %s", e)
            return GENERIC_ERROR.format(error=str(e))
        except TypeError as e:
            logging.error("TypeError: %s", e)
            return GENERIC_ERROR.format(error=str(e))
        except AttributeError as e:
            logging.error("AttributeError (expert system): %s", e)
            return EXPERT_ERROR.format(error=str(e))
        except Exception as e:
            logging.exception("Unexpected error")
            return GENERIC_ERROR.format(error=str(e))

    def chat(self):

        print("Plant Care Bot: Bună! Cum te pot ajuta cu îngrijirea plantelor tale?")

        while True:
            try:
                user_input = input("\nTu: ").strip()

                if user_input.lower() == 'exit':
                    print("\nPlant Care Bot: La revedere! Sper că te-am putut ajuta!")
                    break

                if not user_input:
                    print(
                        "\nPlant Care Bot: Te rog să îmi scrii o întrebare despre plante.")
                    continue

                response = self.generate_response(user_input)
                print("\nPlant Care Bot:", response)

            except Exception as e:
                logging.exception("Unexpected error")
                return GENERIC_ERROR.format(error=str(e))


if __name__ == "__main__":
    bot = PlantCareBot()
    bot.chat()
