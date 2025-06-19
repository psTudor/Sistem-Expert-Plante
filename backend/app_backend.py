from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, List, Optional
import tempfile
import os
from pydantic import BaseModel
from knowledge_base import KnowledgeBase
from expert_system import PlantExpertSystem
from image_recognition import identify_plant
from chatbot import PlantCareBot
import uvicorn

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

        identification_result = identify_plant(temp_file_path)
        os.unlink(temp_file_path)

        plant_name = identification_result.get("plant_name")
        scientific_name = identification_result.get("scientific_name")

        # Planta exista in baza de cunostinte
        plant_info_from_db = kb.get_plant_info(plant_name)

        response_data = {
            "plant_name": plant_name,
            "scientific_name": scientific_name
        }

        if not plant_info_from_db:
            response_data["message"] = "Fară informații adiționale"
        return response_data
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Eroare la procesarea imaginii: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
