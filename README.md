# Sistem Expert pentru Ingrijirea Plantelor
Proiectul este compus din urmatoarele componente:
* **Backend**
  * app_backend.py FastAPI
  * expert_system.py Reguli definite cu Experta
  * chatbot.py Interactiunea utilizatorului cu sistemul
  * knowledge_base.py Gestionarea datelor despre plante
  * image_recogniztion.py: Identificarea unei plante pe baza unei poze
* **Frontend**
  * app_frontend.py Interfata implementata cu Streamlit

## Instalare si rulare local in Windows
### Crearea unui mediu virtual si activarea acestuia
```
python -m venv venv
venv/Scripts/activate
 ```
### Instalare biblioteci si model spaCy pentru limba Romana
Aceste comenzi se executa cu mediul virtual activat
```
pip install -r requirements.txt
python -m spacy download ro_core_news_md
```
### Pornire server FastAPI
Mediul virtual ramane activat
```
python backend/app_backend.py
```
### Se deschide un nou terminal in care se activeaza mediul virtual in timp ce se pastreaza terminalul cu FastAPI deschis
```
venv/Scripts/activate
streamlit run frontend/app_frontend.py
```
Apoi se acceseaza pagina web Local URL: http://localhost:8501
