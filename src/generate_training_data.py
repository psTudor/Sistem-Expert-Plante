import spacy
import json
from typing import List, Dict, Tuple
from itertools import product

def load_plant_data():
    """Încarcă datele despre plante din JSON"""
    with open('data/plants.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_forms_for_word(base_word: str) -> List[str]:
    """Generează forme românești comune pentru un cuvânt"""
    forms = [base_word]
    if base_word.endswith(('e', 'ă')):
        forms.append(f"{base_word}a")
    else:
        forms.append(f"{base_word}ul")
        forms.append(f"{base_word}ului")
    return forms

def get_token_offsets(nlp, text: str) -> List[Tuple[str, int, int]]:
    """Obține offset-urile pentru fiecare token din text"""
    doc = nlp(text)
    return [(token.text, token.idx, token.idx + len(token.text)) for token in doc]

def find_entity_offsets(text: str, entity: str) -> List[Tuple[int, int]]:
    """Găsește toate aparițiile unei entități în text"""
    offsets = []
    start = 0
    while True:
        start = text.lower().find(entity.lower(), start)
        if start == -1:
            break
        offsets.append((start, start + len(entity)))
        start += 1
    return offsets

def generate_examples(plant_data: Dict) -> List[str]:
    """Generează exemple de antrenare folosind datele din JSON"""
    examples = []
    
    # Pattern-uri pentru aspecte de îngrijire
    care_patterns = {
        "udare": [
            "Cum ud {plant}",
            "Când trebuie să ud {plant}",
            "Ce frecvență de udare are {plant}",
            "Cât de des ud {plant}"
        ],
        "lumina": [
            "Ce lumină îi trebuie la {plant}",
            "Câtă lumină necesită {plant}",
            "Care sunt cerințele de lumină pentru {plant}",
            "{plant} are nevoie de lumină"
        ],
        "substrat": [
            "Ce substrat folosesc pentru {plant}",
            "Care e substratul potrivit pentru {plant}",
            "Când schimb substratul la {plant}",
            "Ce tip de pământ folosesc la {plant}"
        ]
    }
    
    # Pattern-uri pentru probleme
    problem_patterns = [
        "{plant} are {problem}",
        "De ce are {plant} {problem}",
        "{problem} la {plant}",
        "Probleme cu {problem} la {plant}"
    ]

    # Generăm exemple pentru fiecare plantă
    for plant_name in plant_data["plants"].keys():
        plant_forms = generate_forms_for_word(plant_name)
        
        # Exemple pentru aspecte de îngrijire
        for aspect, patterns in care_patterns.items():
            for pattern in patterns:
                for plant_form in plant_forms:
                    examples.append(pattern.format(plant=plant_form))
        
        # Exemple pentru probleme
        plant_info = plant_data["plants"][plant_name]
        for problem in plant_info["probleme_comune"].keys():
            problem_text = problem.replace("_", " ")
            for pattern in problem_patterns:
                for plant_form in plant_forms:
                    examples.append(pattern.format(
                        plant=plant_form,
                        problem=problem_text
                    ))
    
    # Adăugăm exemple negative
    negative_examples = [
        "Nu știu ce să fac",
        "Care sunt pașii de îngrijire",
        "Am nevoie de ajutor",
        "Planta mea nu arată bine",
        "Ce să fac mai departe",
        "Cum procedez"
    ]
    examples.extend(negative_examples)
    
    return examples

def generate_training_example(nlp, text: str, plant_data: Dict) -> Dict:
    """Generează anotările pentru un exemplu, aliniate cu tokenizarea spaCy"""
    doc = nlp(text)
    found_entities = []
    
    # Convertim textul în tokens și găsim offset-urile corecte
    tokens = [(t.text, t.idx, t.idx + len(t.text)) for t in doc]
    
    # Căutăm plante
    for plant_name in plant_data["plants"].keys():
        for form in generate_forms_for_word(plant_name):
            for i, token in enumerate(doc):
                if token.text.lower() == form.lower():
                    start = token.idx
                    end = token.idx + len(token.text)
                    found_entities.append((start, end, "PLANT"))
    
    # Căutăm aspecte de îngrijire
    care_aspects = ["udare", "lumina", "substrat", "lumină", "pământ", "sol"]
    for aspect in care_aspects:
        for i, token in enumerate(doc):
            if token.text.lower() == aspect.lower():
                start = token.idx
                end = token.idx + len(token.text)
                found_entities.append((start, end, "CARE_ASPECT"))
    
    # Căutăm probleme
    for plant_info in plant_data["plants"].values():
        for problem in plant_info["probleme_comune"].keys():
            problem_text = problem.replace("_", " ")
            # Pentru probleme care pot conține mai mulți tokens
            problem_doc = nlp(problem_text.lower())
            for i in range(len(doc)):
                if i + len(problem_doc) <= len(doc):
                    span = doc[i:i + len(problem_doc)]
                    if span.text.lower() == problem_text.lower():
                        start = span.start_char
                        end = span.end_char
                        found_entities.append((start, end, "PROBLEM"))
    
    # Sortăm entitățile după poziția de start și eliminăm suprapunerile
    found_entities.sort(key=lambda x: x[0])
    filtered_entities = []
    last_end = -1
    for start, end, label in found_entities:
        if start >= last_end:  # Evităm suprapunerile
            filtered_entities.append((start, end, label))
            last_end = end
    
    return {"entities": filtered_entities}

def save_training_data(training_data: List[Tuple[str, Dict]], plant_data: Dict):
    """Salvează datele de antrenare în fișier"""
    output = """# Date de antrenare generate automat
# NU EDITAȚI MANUAL ACEST FIȘIER!

TRAINING_DATA = [\n"""
    
    for text, annotations in training_data:
        output += f'    ("{text}", {{\n'
        output += f'        "entities": {annotations["entities"]}\n'
        output += "    }),\n"
    
    output += "]\n\n"
    
    # Adăugăm lista de entități cunoscute
    plants = []
    care_aspects = ["udare", "lumina", "substrat", "lumină", "pământ", "sol"]
    problems = []
    
    for plant_name in plant_data["plants"].keys():
        plants.extend(generate_forms_for_word(plant_name))
    
    for plant_info in plant_data["plants"].values():
        for problem in plant_info["probleme_comune"].keys():
            problems.append(problem.replace("_", " "))
    
    output += "# Lista de entități cunoscute pentru referință\n"
    output += "ENTITIES = {\n"
    output += f'    "PLANT": {plants},\n'
    output += f'    "CARE_ASPECT": {care_aspects},\n'
    output += f'    "PROBLEM": {problems}\n'
    output += "}"
    
    with open("src/training_data.py", "w", encoding="utf-8") as f:
        f.write(output)

if __name__ == "__main__":
    print("Generare date de antrenare...")
    
    # Încărcăm modelul spaCy și datele despre plante
    nlp = spacy.load("ro_core_news_md")
    plant_data = load_plant_data()
    
    # Generăm exemplele
    examples = generate_examples(plant_data)
    
    # Generăm datele de antrenare
    training_data = []
    for text in examples:
        annotations = generate_training_example(nlp, text, plant_data)
        training_data.append((text, annotations))
        print(f"\nText: {text}")
        print("Entități găsite:", annotations["entities"])
    
    # Salvăm datele generate
    save_training_data(training_data, plant_data)
    
    print("\nDate de antrenare generate și salvate în src/training_data.py")