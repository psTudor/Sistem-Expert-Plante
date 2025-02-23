import spacy
from knowledge_base import KnowledgeBase
from expert_system import PlantExpertSystem
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

    def preprocess_text(self, text: str) -> str:
        """Preprocesează textul pentru a normaliza diacriticele și spațiile"""
        text = text.lower()
        diac_map = {'ă': 'a', 'â': 'a', 'î': 'i', 'ș': 's', 'ț': 't'}
        for k, v in diac_map.items():
            text = text.replace(k, v)
        return ' '.join(text.split())

    def identify_intent(self, text: str, entities: Dict[str, List[str]]) -> str:
        """Identifică intenția utilizatorului din text și entitățile extrase"""
        text = self.preprocess_text(text)
        
        # Verifică keywords pentru probleme
        if any(keyword in text for keyword in self.intent_keywords['problem']) or entities['PROBLEM']:
            return 'problem'
        
        # Verifică keywords pentru îngrijire
        if any(keyword in text for keyword in self.intent_keywords['care']):
            return 'care'
        
        # Verifică dacă există aspect de îngrijire
        if entities['CARE_ASPECT']:
            return 'care'
        
        # Default la informații generale
        return 'general'

    def extract_entities(self, text: str) -> Dict[str, List[str]]:
        """Extrage entitățile relevante din text folosind modelul NLP"""
        doc = self.nlp(text)
        entities = {
            "PLANT": [],
            "CARE_ASPECT": [],
            "PROBLEM": [],
            "CONDITION": []
        }
        
        # Normalizează numele plantelor
        plant_names = {
            'orhidee': ['orhideea', 'orhideei', 'orhideele'],
            'ficus': ['ficusul', 'ficusului', 'ficusii']
        }
        
        # Procesează textul pentru a găsi planta
        text_lower = text.lower()
        for base_name, variations in plant_names.items():
            if base_name in text_lower or any(var in text_lower for var in variations):
                entities["PLANT"].append(base_name)
                break
        
        # Procesează entitățile NER pentru alte tipuri
        for ent in doc.ents:
            if ent.label_ == "CARE_ASPECT":
                norm_text = self.aspect_mappings.get(ent.text.lower(), ent.text.lower())
                entities["CARE_ASPECT"].append(norm_text)
            elif ent.label_ == "PROBLEM":
                norm_text = self.problem_mappings.get(ent.text.lower(), ent.text.lower())
                entities["PROBLEM"].append(norm_text)
        
        # Verifică probleme comune în text
        text_lower = self.preprocess_text(text)
        for problem_text, problem_id in self.problem_mappings.items():
            if problem_text in text_lower:
                entities["PROBLEM"].append(problem_id)
        
        # Verifică aspecte de îngrijire în text
        for aspect_text, aspect_id in self.aspect_mappings.items():
            if aspect_text in text_lower:
                entities["CARE_ASPECT"].append(aspect_id)
        
        # Elimină duplicate
        for key in entities:
            entities[key] = list(set(entities[key]))
        
        return entities

    def generate_response(self, text: str) -> str:
        """Generează răspunsul folosind sistemul expert și NLP"""
        try:
            entities = self.extract_entities(text)
            intent = self.identify_intent(text, entities)
            
            if not entities["PLANT"]:
                return "Îmi pare rău, dar nu am înțeles despre ce plantă vorbești. Poți să specifici numele plantei?"
            
            plant = entities["PLANT"][0]
            
            if not self.kb.get_plant_info(plant):
                return f"Îmi pare rău, dar nu am informații despre planta '{plant}' în baza mea de cunoștințe."
            
            # Folosim sistemul expert pentru a genera răspunsul
            expert_response = self.expert_system.get_expert_response(
                entities=entities,
                intent=intent
            )
            
            if expert_response:
                return expert_response
            
            # Fallback la informații generale
            basic_care = self.kb.get_basic_care(plant)
            if basic_care:
                return (
                    f"Pentru {plant}, iată informațiile de bază de îngrijire:\n"
                    f"- Udare: {basic_care['udare']['detalii']}\n"
                    f"- Lumină: {basic_care['lumina']['detalii']}\n"
                    f"- Substrat: {basic_care['substrat']['detalii']}"
                )
            
            return "Am înțeles ce plantă te interesează, dar nu sunt sigur ce anume vrei să știi despre ea. Poți să reformulezi întrebarea?"
            
        except Exception as e:
            return f"A apărut o eroare în procesarea cererii tale: {str(e)}"

    def chat(self):
        """Funcția principală pentru interacțiunea cu utilizatorul"""
        print("Plant Care Bot: Bună! Cum te pot ajuta cu îngrijirea plantelor tale?")
        print("(Scrie 'exit' pentru a încheia conversația)")
        
        while True:
            try:
                user_input = input("\nTu: ").strip()
                
                if user_input.lower() == 'exit':
                    print("\nPlant Care Bot: La revedere! Sper că te-am putut ajuta!")
                    break
                
                if not user_input:
                    print("\nPlant Care Bot: Te rog să îmi scrii o întrebare despre plante.")
                    continue
                
                response = self.generate_response(user_input)
                print("\nPlant Care Bot:", response)
                
            except Exception as e:
                print(f"\nPlant Care Bot: Îmi pare rău, a apărut o eroare neașteptată. Te rog să încerci din nou.")
                print(f"Eroare: {str(e)}")

if __name__ == "__main__":
    bot = PlantCareBot()
    bot.chat()