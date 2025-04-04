from typing import Optional, Dict, List, Any
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.exceptions import GoogleCloudError


class KnowledgeBase:
    """
    Clasa pentru gestionarea bazei de cunostinte despre plante, stocate in Firebase Firestore.
    """
    def __init__(self, firebase_credentials_path="credentials/plant-expert-cccb6-firebase-adminsdk-fbsvc-69b270c0e1.json"):
        """
        Initializeaza conexiunea cu Firebase Firestore.
        """
        try:
            if not firebase_admin._apps:
                cred = credentials.Certificate(firebase_credentials_path)
                firebase_admin.initialize_app(cred)
            
            self.db = firestore.client()
            self.plants_collection = self.db.collection('plants')
            print("Conexiune la Firebase realizată cu succes!")
        except (firebase_admin.exceptions.FirebaseError, FileNotFoundError, ValueError) as e:
            print(f"Eroare la initializarea Firebase: {e}")
            self.db = None
            self.plants_collection = None
    
    def get_plant_info(self, plant_name: str) -> Optional[Dict[str, Any]]:
        """Obtine informatii despre o planta specifica."""
        try:
            doc_ref = self.plants_collection.document(plant_name.lower())
            plant_doc = doc_ref.get()
            
            if plant_doc.exists:
                return plant_doc.to_dict()
            return None
        except GoogleCloudError as e:
            print(f"Eroare la obtinerea informatiilor despre planta: {e}")
            return None
    
    def get_basic_care(self, plant_name: str) -> Optional[Dict[str, Any]]:
        """Obtine informatii de baza despre ingrijirea unei plante."""
        plant = self.get_plant_info(plant_name)
        return plant.get('cerinte_baza') if plant else None
    
    def get_care_aspect(self, plant_name: str, aspect: str) -> Optional[Any]:
        """Obtine un aspect specific de ingrijire pentru o planta."""
        basic_care = self.get_basic_care(plant_name)
        return basic_care.get(aspect) if basic_care else None
    
    def get_problem_details(self, plant_name: str, problem: str) -> Optional[Dict[str, Any]]:
        """Obtine detalii despre o problema specifica a unei plante."""
        plant = self.get_plant_info(plant_name)
        if plant and 'probleme_comune' in plant:
            return plant['probleme_comune'].get(problem)
        return None
    
    def get_all_plants(self) -> List[str]:
        """Obtine lista tuturor numelor de plante din baza de date."""
        try:
            plants_docs = self.plants_collection.stream()
            return [doc.id for doc in plants_docs]
        except GoogleCloudError as e:
            print(f"Eroare la obtinerea listei de plante: {e}")
            return []
    
    def add_plant(self, plant_name: str, plant_data: Dict[str, Any]) -> bool:
        """Adauga o planta noua in baza de date."""
        try:
            doc_ref = self.plants_collection.document(plant_name.lower())
            doc_ref.set(plant_data)
            return True
        except GoogleCloudError as e:
            print(f"Eroare la adăugarea plantei: {e}")
            return False
    
    def update_plant(self, plant_name: str, plant_data: Dict[str, Any]) -> bool:
        """Actualizeaza informatiile despre o planta existenta."""
        try:
            doc_ref = self.plants_collection.document(plant_name.lower())
            doc_ref.update(plant_data)
            return True
        except GoogleCloudError as e:
            print(f"Eroare la actualizarea plantei: {e}")
            return False
    
    def delete_plant(self, plant_name: str) -> bool:
        """sterge o planta din baza de date."""
        try:
            doc_ref = self.plants_collection.document(plant_name.lower())
            doc_ref.delete()
            return True
        except GoogleCloudError as e:
            print(f"Eroare la ștergerea plantei: {e}")
            return False
        