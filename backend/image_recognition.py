import os
import json
from google.cloud import vision


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials/plants-452112-8502b77c9773.json"

def load_plants():
    with open('data/plants.json', 'r', encoding='utf-8') as f:
        return json.load(f)['plants']

def identify_plant(image_path):
        try:
            client = vision.ImageAnnotatorClient()
            with open(image_path, 'rb') as image_file:
                content = image_file.read()
            image_path = vision.Image(content=content)
            response = client.label_detection(image=image_path)
            labels = response.label_annotations
            print("Etichete detectate:")
            for label in labels:
                print(f"- {label.description} (scor: {label.score})")

            english_keywords = [label.description.lower() for label in labels]
            plants = load_plants()
            for plant_name, plant_data in plants.items():
                if any(keyword in plant_data['keywords'] for keyword in english_keywords):
                    return plant_name  # Returneaza cheia
            return "Nu am putut identifica planta."
        except FileNotFoundError:
            print(f"Eroare: Fișierul imagine '{image_path}' nu a fost găsit.")
            return []

if __name__ == '__main__':
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image = os.path.join(current_dir, 'trandafir.jpg')
        plant = identify_plant(image)