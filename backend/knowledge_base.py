import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from typing import Optional, Dict, List, Any

class KnowledgeBase:
    def __init__(self, firebase_credentials_path="credentials/plant-expert-cccb6-firebase-adminsdk-fbsvc-69b270c0e1.json"):
        try:
            # Inițializare Firebase (se face o singură dată)
            if not firebase_admin._apps:
                cred = credentials.Certificate(firebase_credentials_path)
                firebase_admin.initialize_app(cred)
            
            # Inițializare Firestore DB
            self.db = firestore.client()
            self.plants_collection = self.db.collection('plants')
            print("Conexiune la Firebase realizată cu succes!")
        except Exception as e:
            print(f"Eroare la inițializarea Firebase: {e}")
    
    def get_plant_info(self, plant_name: str) -> Optional[Dict[str, Any]]:
        """Obține informații despre o plantă specifică."""
        try:
            doc_ref = self.plants_collection.document(plant_name.lower())
            plant_doc = doc_ref.get()
            
            if plant_doc.exists:
                return plant_doc.to_dict()
            return None
        except Exception as e:
            print(f"Eroare la obținerea informațiilor despre plantă: {e}")
            return None
    
    def get_basic_care(self, plant_name: str) -> Optional[Dict[str, Any]]:
        """Obține informații de bază despre îngrijirea unei plante."""
        plant = self.get_plant_info(plant_name)
        return plant.get('cerinte_baza') if plant else None
    
    def get_care_aspect(self, plant_name: str, aspect: str) -> Optional[Any]:
        """Obține un aspect specific de îngrijire pentru o plantă."""
        basic_care = self.get_basic_care(plant_name)
        return basic_care.get(aspect) if basic_care else None
    
    def get_problem_details(self, plant_name: str, problem: str) -> Optional[Dict[str, Any]]:
        """Obține detalii despre o problemă specifică a unei plante."""
        plant = self.get_plant_info(plant_name)
        if plant and 'probleme_comune' in plant:
            return plant['probleme_comune'].get(problem)
        return None
    
    def get_all_plants(self) -> List[str]:
        """Obține lista tuturor numelor de plante din baza de date."""
        try:
            plants_docs = self.plants_collection.stream()
            return [doc.id for doc in plants_docs]
        except Exception as e:
            print(f"Eroare la obținerea listei de plante: {e}")
            return []
    
    # Metode noi pentru administrarea datelor
    
    def add_plant(self, plant_name: str, plant_data: Dict[str, Any]) -> bool:
        """Adaugă o plantă nouă în baza de date."""
        try:
            doc_ref = self.plants_collection.document(plant_name.lower())
            doc_ref.set(plant_data)
            return True
        except Exception as e:
            print(f"Eroare la adăugarea plantei: {e}")
            return False
    
    def update_plant(self, plant_name: str, plant_data: Dict[str, Any]) -> bool:
        """Actualizează informațiile despre o plantă existentă."""
        try:
            doc_ref = self.plants_collection.document(plant_name.lower())
            doc_ref.update(plant_data)
            return True
        except Exception as e:
            print(f"Eroare la actualizarea plantei: {e}")
            return False
    
    def delete_plant(self, plant_name: str) -> bool:
        """Șterge o plantă din baza de date."""
        try:
            doc_ref = self.plants_collection.document(plant_name.lower())
            doc_ref.delete()
            return True
        except Exception as e:
            print(f"Eroare la ștergerea plantei: {e}")
            return False