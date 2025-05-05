import json


def generate_training_data(plant_data):
    training_data = []

    care_aspect_templates = {
        "udare": [
            "Cum ud {plant}?",
            "Ce metoda de udare folosesc la {plant}?",
            "Care e frecventa udarii la {plant}?"
        ],
        "lumina": [
            "Ce fel de lumina prefera {plant}?",
            "Cata lumina are nevoie {plant}?",
            "Unde pun {plant} pentru o lumina buna?"
        ],
        "pamant": [
            "In ce mediu palntez {plant}?",
            "Ce sol e potrivit pentru {plant}?",
            "Ce fel de pamant ii trebuie lui {plant}?"
        ]
    }

    problem_templates = [
        "{plant} are problema: {problem}.",
        "Cum rezolv {problem} la {plant}?",
        "Am observat {problem} la {plant}. Ce fac?"
    ]

    general_templates = [
        "Ce trebuie sa stiu despre {plant}?",
        "Cum se ingrijeste {plant}?",
        "Informatii generale despre {plant}.",
        "Cum cresc {plant}?",
        "Ce recomandari aveti pentru {plant}?"
    ]

    plants = []
    care_aspects = list(care_aspect_templates.keys())
    problems = []

    for plant_name, info in plant_data["plants"].items():
        plants.append(plant_name)

        # --- CERINTE BAZA ---
        for aspect, templates in care_aspect_templates.items():
            for phrase in templates:
                text = phrase.format(plant=plant_name)
                start = text.lower().find(plant_name.lower())
                end = start + len(plant_name)
                aspect_start = text.lower().find(aspect)
                entities = []
                if aspect_start != -1:
                    entities.append(
                        (aspect_start, aspect_start + len(aspect), "CARE_ASPECT"))
                entities.append((start, end, "PLANT"))
                training_data.append((text, {"entities": entities}))

        # --- ÎNTREBĂRI GENERALE ---
        for phrase in general_templates:
            text = phrase.format(plant=plant_name)
            start = text.lower().find(plant_name.lower())
            end = start + len(plant_name)
            entities = [(start, end, "PLANT")]
            training_data.append((text, {"entities": entities}))

        # --- PROBLEME COMUNE ---
        for problem_key in info.get("probleme_comune", {}):
            problem_text = problem_key.replace("_", " ")
            problems.append(problem_text)

            for template in problem_templates:
                text = template.format(plant=plant_name, problem=problem_text)
                plant_start = text.lower().find(plant_name.lower())
                plant_end = plant_start + len(plant_name)
                problem_start = text.lower().find(problem_text.lower())
                problem_end = problem_start + len(problem_text)
                entities = [
                    (problem_start, problem_end, "PROBLEM"),
                    (plant_start, plant_end, "PLANT")
                ]
                training_data.append((text, {"entities": entities}))

    return training_data, plants, care_aspects, list(set(problems))


def save_to_py_file(training_data, plants, care_aspects, problems, filename="backend/training_data.py"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("# Set generat automat pentru antrenare\n")
        f.write("TRAINING_DATA = [\n")
        for text, annot in training_data:
            f.write(f'    ("{text}", {{\n')
            f.write(f'        "entities": {annot["entities"]}\n')
            f.write("    }),\n")
        f.write("]\n\n")

        f.write("# Lista entitatilor cunoscute\n")
        f.write("ENTITIES = {\n")
        f.write(f'    "PLANT": {sorted(plants)},\n')
        f.write(f'    "CARE_ASPECT": {sorted(care_aspects)},\n')
        f.write(f'    "PROBLEM": {sorted(problems)}\n')
        f.write("}\n")


if __name__ == "__main__":
    with open("data/plants.json", "r", encoding="utf-8") as f:
        plant_data = json.load(f)

    training_data, plants, care_aspects, problems = generate_training_data(
        plant_data)
    save_to_py_file(training_data, plants, care_aspects, problems)
    print(f"✅ Am generat {len(training_data)} exemple în training_data.py")
