from knowledge_base import KnowledgeBase

# Specifică calea corectă către fișierul de credențiale
kb = KnowledgeBase(firebase_credentials_path="credentials/plant-expert-cccb6-firebase-adminsdk-fbsvc-69b270c0e1.json")

# Încearcă să obții toate plantele
plants = kb.get_all_plants()
print(f"Plante găsite: {plants}")

# Încearcă să obții informații despre o plantă specifică
plant_info = kb.get_plant_info("orhidee")
print(f"Informații despre orhidee: {plant_info}")