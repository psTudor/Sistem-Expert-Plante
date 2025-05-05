import spacy
from knowledge_base import KnowledgeBase
from expert_system import PlantExpertSystem
from image_recognition import identify_plant
from typing import Dict, List, Optional
from training_data import ENTITIES


class PlantCareBot:
    def __init__(self, model_path: str = "model"):
        self.nlp = spacy.load(model_path)
        self.kb = KnowledgeBase()
        self.expert_system = PlantExpertSystem()

        self.intent_keywords = {
            'problem': ['problema', 'probleme', 'cad', 'cazut', 'galben', 'putred', 'bolnav', 'pete', 'deteriorare'],
            'care': ['cum', 'cand', 'cat', 'trebuie', 'necesita', 'nevoie', 'ingrijire', 'ingrijesc'],
            'info': ['ce', 'care', 'spune', 'explica', 'despre', 'detalii', 'spune-mi', 'cum ingrijesc', 'ce ingrijire']
        }

        self.aspect_mappings = {
            'ud': 'udare', 'uda': 'udare', 'udat': 'udare', 'apa': 'udare', 'apă': 'udare',
            'lumina': 'lumina', 'luminozitate': 'lumina', 'soare': 'lumina',
            'sol': 'pamant', 'plantez': 'pamant', 'plantare': 'pamant', 'mediu': 'pamant',
            'temperatura': 'temperatura', 'cald': 'temperatura', 'rece': 'temperatura'
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
        self.plant_variations = {}

        # Creează variatiile pentru fiecare planta de baza
        for plant in self.base_plants:
            self.plant_variations[plant] = []

            for form in ENTITIES["PLANT"]:
                if form == plant or form.startswith(plant):
                    self.plant_variations[plant].append(form)

            plant_info = self.kb.get_plant_info(plant)
            if plant_info and "keywords" in plant_info:
                self.plant_variations[plant].extend(plant_info["keywords"])

            # Eliminare duplicate
            self.plant_variations[plant] = list(
                set(self.plant_variations[plant]))

    def preprocess_text(self, text: str) -> str:

        # Preproceseare pentru diacritice
        text = text.lower()
        diac_map = {'ă': 'a', 'â': 'a', 'î': 'i', 'ș': 's', 'ț': 't'}
        for k, v in diac_map.items():
            text = text.replace(k, v)
        return ' '.join(text.split())

    def identify_intent(self, text: str, entities: Dict[str, List[str]]) -> str:
        text = self.preprocess_text(text)

        problem_indicators = self.intent_keywords['problem']
        if any(keyword in text for keyword in problem_indicators) or entities['PROBLEM']:
            return 'problem'

        care_indicators = self.intent_keywords['care']
        if any(keyword in text for keyword in care_indicators) or entities['CARE_ASPECT']:
            return 'care'

        info_indicators = self.intent_keywords['info']
        if any(keyword in text for keyword in info_indicators):
            return 'info'

        if text.startswith('cum'):
            return 'care'
        if text.startswith('ce') or text.startswith('care'):
            if 'problema' in text or 'cauza' in text:
                return 'problem'
            return 'info'

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

        # Cautam plante in text
        for base_name, variations in self.plant_variations.items():
            if base_name in text_lower or any(var in text_lower for var in variations):
                entities["PLANT"].append(base_name)
                break

        for ent in doc.ents:
            if ent.label_ == "CARE_ASPECT":
                # Normalizam aspectul de ingrijire folosind maparea
                norm_text = self.aspect_mappings.get(
                    ent.text.lower(), ent.text.lower())
                if norm_text not in entities["CARE_ASPECT"]:
                    entities["CARE_ASPECT"].append(norm_text)
            elif ent.label_ == "PROBLEM":
                # Normalizam problema folosind maparea
                norm_text = self.problem_mappings.get(
                    ent.text.lower(), ent.text.lower())
                if norm_text not in entities["PROBLEM"]:
                    entities["PROBLEM"].append(norm_text)

        for problem_text, problem_id in self.problem_mappings.items():
            if f" {problem_text} " in f" {text_lower} ":  # match complet
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

        if not entities["PLANT"] and "planta" in text_lower:
            entities["PLANT"].append("generica")

        return entities

    def generate_response(self, text: str) -> str:
        try:
            entities = self.extract_entities(text)
            intent = self.identify_intent(text, entities)

            if not entities["PLANT"]:
                return "Îmi pare rău, dar nu am înțeles despre ce plantă vorbești. Poți să specifici numele plantei?"

            plant = entities["PLANT"][0]

            plant_info = self.kb.get_plant_info(plant)
            if not plant_info:
                return f"Îmi pare rău, dar nu am informații despre planta '{plant}' în baza mea de cunoștințe."

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

            return f"Am înțeles că te interesează {plant}, dar nu sunt sigur ce anume vrei să știi despre această plantă. Poți să reformulezi întrebarea?"

        except ValueError as e:
            return f"Eroare la procesarea textului: {str(e)}"
        except TypeError as e:
            return f"Eroare la accesarea bazei de cunostinte: {str(e)}"
        except AttributeError as e:
            return f"A aparut o eroare la apelarea expert system: {str(e)}"
        except Exception as e:
            return f"A apărut o eroare neașteptată: {str(e)}"

    def chat(self):

        print("Plant Care Bot: Bună! Cum te pot ajuta cu îngrijirea plantelor tale?")
        print("(Scrie 'exit' pentru a încheia conversația sau 'imagine: calea/catre/imagine.jpg' pentru a identifica o plantă)")

        while True:
            try:
                user_input = input("\nTu: ").strip()

                if user_input.lower() == 'exit':
                    print("\nPlant Care Bot: La revedere! Sper că te-am putut ajuta!")
                    break

                if user_input.lower().startswith('imagine:'):
                    image_path = user_input.split('imagine:')[1].strip()
                    plant_name = identify_plant(image_path)
                    print(
                        f"\nPlant Care Bot: Planta identificată: {plant_name}")
                    continue

                if not user_input:
                    print(
                        "\nPlant Care Bot: Te rog să îmi scrii o întrebare despre plante.")
                    continue

                response = self.generate_response(user_input)
                print("\nPlant Care Bot:", response)

            except Exception as e:
                print(
                    f"\nPlant Care Bot: Îmi pare rău, a apărut o eroare neașteptată. Te rog să încerci din nou.")
                print(f"Eroare: {str(e)}")


if __name__ == "__main__":
    bot = PlantCareBot()
    bot.chat()
