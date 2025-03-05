from google.cloud import vision

import json

def load_plants():
    """Încarcă baza de date cu plante din fișierul JSON."""
    with open('data/plants.json', 'r', encoding='utf-8') as f:
        return json.load(f)['plants']

def identify_plant(image_path):
        """Identifică o plantă și returnează numele în română."""
        try:
            client = vision.ImageAnnotatorClient()
            with open(image_path, 'rb') as image_file:
                content = image_file.read()
            image = vision.Image(content=content)
            response = client.label_detection(image=image)
            labels = response.label_annotations
            print("Etichete detectate:")
            for label in labels:
                print(f"- {label.description} (scor: {label.score})")

            english_keywords = [label.description.lower() for label in labels]
            plants = load_plants()
            for plant_name, plant_data in plants.items():
                if any(keyword in plant_data['keywords'] for keyword in english_keywords):
                    return plant_name  # Returnează cheia (numele plantei)
            return "Nu am putut identifica planta."
        except Exception as e:
            print(f"A apărut o eroare: {e}")
            return "A apărut o eroare la procesarea imaginii."

if __name__ == '__main__':
        plant_name = identify_plant('res/trandafir.jpg')
        print(plant_name)