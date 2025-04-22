import tempfile
import os
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from knowledge_base import KnowledgeBase
from expert_system import PlantExpertSystem
from image_recognition import identify_plant
from chatbot import PlantCareBot

plant_care_bot = PlantCareBot()
app = FastAPI(title="Plant Care Expert System API")

# Configurare CORS pentru a permite conexiuni de la frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

kb = KnowledgeBase(
    firebase_credentials_path="credentials/plant-expert-cccb6-firebase-adminsdk-fbsvc-69b270c0e1.json")
expert_system = PlantExpertSystem()


class QueryRequest(BaseModel):
    text: str


@app.get("/")
async def root():
    return {"message": "Bine ai venit la Plant Care Expert System API"}


@app.get("/plants")
async def get_all_plants():
    plants = kb.get_all_plants()
    return {"plants": plants}


@app.get("/plants/{plant_name}")
async def get_plant_info(plant_name: str):
    plant = kb.get_plant_info(plant_name)
    if not plant:
        raise HTTPException(status_code=404, detail="Planta nu a fost găsită")
    return plant


@app.get("/plants/{plant_name}/care")
async def get_basic_care(plant_name: str):
    care_info = kb.get_basic_care(plant_name)
    if not care_info:
        raise HTTPException(
            status_code=404, detail="Informații de îngrijire negăsite")
    return care_info


@app.get("/plants/{plant_name}/problems")
async def get_plant_problems(plant_name: str):
    plant = kb.get_plant_info(plant_name)
    if not plant or 'probleme_comune' not in plant:
        raise HTTPException(
            status_code=404, detail="Informații despre probleme negăsite")
    return {"problems": plant['probleme_comune']}


@app.post("/query")
async def process_query(request: QueryRequest):
    # Procesare in limbaj natural intrebare despre plante
    response = plant_care_bot.generate_response(request.text)
    return {"response": response}


@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    # Identificare planta din poza
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as temp_file:
            content = await file.read()
            temp_file.write(content)
            temp_file_path = temp_file.name

        plant_name = identify_plant(temp_file_path)
        os.unlink(temp_file_path)

        if not plant_name:
            return {"message": "Nu am putut identifica planta din imagine."}

        # Afisare informatii despre planta identificata
        plant_info = kb.get_plant_info(plant_name)
        return {
            "plant_name": plant_name,
            "plant_info": plant_info
        }
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Eroare la procesarea imaginii: {str(e)}") from e

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
