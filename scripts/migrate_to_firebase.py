import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.exceptions import GoogleCloudError


def migrate_json_to_firebase(json_path="data/plants.json", firebase_credentials_path="credentials/plant-expert-cccb6-firebase-adminsdk-fbsvc-69b270c0e1.json"):
    """
    Acest modul contine functii pentru a migra date JSON în Firebase.
    """
    try:
        with open(json_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            plants = data.get("plants", {})

        if not plants:
            print("Nu s-au găsit date despre plante în fișierul JSON.")
            return False

        print(f"S-au încărcat {len(plants)} plante din fișierul JSON.")
    except FileNotFoundError:
        print(f"Fișierul JSON {json_path} nu a fost găsit.")
        return False

    try:
        creds = credentials.Certificate(firebase_credentials_path)
        firebase_admin.initialize_app(creds)
        db = firestore.client()
        plants_collection = db.collection('plants')
        print("Conexiune la Firebase realizată cu succes!")
    except firebase_admin.exceptions.FirebaseError as e:
        print(f"Eroare la inițializarea Firebase: {e}")
        return False

    success_count = 0
    for plant_name, plant_data in plants.items():
        try:
            plants_collection.document(plant_name).set(plant_data)
            success_count += 1
            print(f"Planta '{plant_name}' a fost migrată cu succes.")
        except GoogleCloudError as e:
            print(f"Eroare la scrierea datelor pentru {plant_name}: {e}")

    print(
        f"\nMigrare completă: {success_count}/{len(plants)} plante au fost migrate cu succes.")
    return True


if __name__ == "__main__":
    migrate_json_to_firebase(
        json_path="data/plants.json",
        firebase_credentials_path="credentials/plant-expert-cccb6-firebase-adminsdk-fbsvc-69b270c0e1.json"
    )
