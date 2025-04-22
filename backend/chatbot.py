import spacy
from knowledge_base import KnowledgeBase
from expert_system import PlantExpertSystem
from image_recognition import identify_plant
from typing import Dict, List, Optional


class PlantCareBot:
    def __init__(self, model_path: str = "model"):
        self.nlp = spacy.load(model_path)
        self.kb = KnowledgeBase()
        self.expert_system = PlantExpertSystem()

        self.intent_keywords = {
            'problem': ['problema', 'probleme', 'cad', 'cazut', 'galben', 'putred', 'bolnav', 'pete', 'deteriorare'],
            'care': ['cum', 'cand', 'cat', 'trebuie', 'necesita', 'nevoie', 'ingrijire', 'ingrijesc'],
            'info': ['ce', 'care', 'spune', 'explica', 'despre', 'detalii']
        }

        self.aspect_mappings = {
            'ud': 'udare', 'uda': 'udare', 'udat': 'udare', 'apa': 'udare',
            'lumina': 'lumina', 'luminozitate': 'lumina', 'soare': 'lumina',
            'substrat': 'substrat', 'pamant': 'substrat', 'sol': 'substrat',
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

        # Creează variațiile pentru fiecare planta de baza
        for plant in self.base_plants:
            variations = [plant]  # Adaugă forma de baza

            # Adaugă forme flexionate comune în română
            if plant.endswith('a'):  # pentru nume feminine (ex: muscata)
                variations.extend([
                    f"{plant}",
                    f"{plant[:-1]}ei",  # muscatei
                    f"{plant}le"  # muscatele
                ])
            else:  # pentru nume masculine/neutre
                variations.extend([
                    f"{plant}ul",  # ficusul
                    f"{plant}ului",  # ficusului
                    f"{plant}ii"  # ficusii
                ])

            plant_info = self.kb.get_plant_info(plant)

            # Adaugă și cuvinte cheie din JSON dacă există
            if plant_info and "keywords" in plant_info:
                variations.extend(plant_info["keywords"])

            self.plant_variations[plant] = variations

    def preprocess_text(self, text: str) -> str:

        # Preproceseare pentru diacritice
        text = text.lower()
        diac_map = {'ă': 'a', 'â': 'a', 'î': 'i', 'ș': 's', 'ț': 't'}
        for k, v in diac_map.items():
            text = text.replace(k, v)
        return ' '.join(text.split())

    def identify_intent(self, text: str, entities: Dict[str, List[str]]) -> str:
        """
        Identifica intentia utilizatorului pe baza textului si a entitatilor extrase
        Imbunatatita pentru a detecta mai precis intențiile

        Args:
            text (str): Textul introdus de utilizator.
            entities (Dict[str, List[str]]): Entitatile extrase din text

        Returns:
            str: Intentia identificata
        """
        text = self.preprocess_text(text)

        # Intentia de a rezolva o problema
        problem_indicators = self.intent_keywords['problem']
        if any(keyword in text for keyword in problem_indicators) or entities['PROBLEM']:
            return 'problem'

        # Intentia de a afla despre ingrijire
        care_indicators = self.intent_keywords['care']
        if any(keyword in text for keyword in care_indicators) or entities['CARE_ASPECT']:
            return 'care'

        # Intentia de a obtine informatii generale
        info_indicators = self.intent_keywords['info']
        if any(keyword in text for keyword in info_indicators):
            return 'info'

        # Detectie bazata pe structura intrebarii
        if text.startswith('cum'):
            return 'care'
        if text.startswith('ce') or text.startswith('care'):
            if 'problema' in text or 'cauza' in text:
                return 'problem'
            return 'info'

        # Intentia implicita daca nu am putut determina altceva
        return 'general'

    def extract_entities(self, text: str) -> Dict[str, List[str]]:
        """
        Extrage entitatile relevante din textul introdus de utilizator
        Imbunatatita pentru a asigura potriviri corecte

        Args:
            text (str): Textul de analizat

        Returns:
            Dict[str, List[str]]: Un dictionar cu entitatile extrase
        """
        doc = self.nlp(text)
        entities = {
            "PLANT": [],
            "CARE_ASPECT": [],
            "PROBLEM": [],
            "CONDITION": []
        }

        # Preprocesam textul pentru o potrivire mai buna
        text_lower = self.preprocess_text(text.lower())

        # Cautam plante in text
        plant_found = False
        for base_name, variations in self.plant_variations.items():
            # Verificam daca baza sau vreo variatie este continuta in text
            if base_name in text_lower or any(var in text_lower for var in variations):
                entities["PLANT"].append(base_name)
                plant_found = True
                break

        # Folosim entitățile NER pentru a completa rezultatele
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

        # Cautam explicit problemele comune in text
        for problem_text, problem_id in self.problem_mappings.items():
            if problem_text in text_lower:
                if problem_id not in entities["PROBLEM"]:
                    entities["PROBLEM"].append(problem_id)

        # Cautam aspecte de ingrijire in text
        for aspect_text, aspect_id in self.aspect_mappings.items():
            if aspect_text in text_lower:
                if aspect_id not in entities["CARE_ASPECT"]:
                    entities["CARE_ASPECT"].append(aspect_id)

        # Detectam conditii specifice in text
        if any(word in text_lower for word in ["uscat", "sec", "uscata", "uscare"]):
            entities["CONDITION"].append("dry")
        if any(word in text_lower for word in ["umed", "umeda", "ud", "uda", "umiditate"]):
            entities["CONDITION"].append("wet")

        # Eliminare duplicate
        for key in entities:
            entities[key] = list(set(entities[key]))

        # Verificare finala și eroare dacă nu am găsit nicio plantă
        if not entities["PLANT"] and "planta" in text_lower:
            # Verificam daca utilizatorul se refera la o planta generica
            entities["PLANT"].append("generica")

        return entities

    def generate_response(self, text: str) -> str:
        """
        Genereaza un raspuns pe baza textului introdus de utilizator
        Imbunatatita pentru consistenta si tratarea erorilor

        Args:
            text (str): Textul introdus de utilizator

        Returns:
            str: Raspunsul generat
        """
        try:
            # Extragem entitatile si determinam intentia
            entities = self.extract_entities(text)
            intent = self.identify_intent(text, entities)

            # Verificam daca am detectat o planta
            if not entities["PLANT"]:
                return "Îmi pare rău, dar nu am înțeles despre ce plantă vorbești. Poți să specifici numele plantei?"

            # Extragem numele plantei
            plant = entities["PLANT"][0]

            # Verificam daca planta exista in baza de cunostinte
            plant_info = self.kb.get_plant_info(plant)
            if not plant_info:
                return f"Îmi pare rău, dar nu am informații despre planta '{plant}' în baza mea de cunoștințe."

            # Trimitem cererea catre sistemul expert cu planta detectata
            expert_response = self.expert_system.get_expert_response(
                entities=entities,
                intent=intent
            )

            # Verificam daca avem un raspuns de la sistemul expert
            if expert_response:
                # Verificam daca raspunsul contine numele plantei detectate
                if plant.lower() not in expert_response.lower():
                    # Adaugam explicit numele plantei in raspuns pentru claritate
                    return f"Pentru {plant}: {expert_response}"
                return expert_response

            # Raspuns implicit cu informatii de baza despre ingrijire
            basic_care = self.kb.get_basic_care(plant)
            if basic_care:
                return (
                    f"Pentru {plant}, iată informațiile de bază de îngrijire:\n"
                    f"- Udare: {basic_care['udare']['detalii']}\n"
                    f"- Lumină: {basic_care['lumina']['detalii']}\n"
                    f"- Substrat: {basic_care['substrat']['detalii']}"
                )

            # Raspuns final daca nu am putut genera alt raspuns
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
