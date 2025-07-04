
import streamlit as st
import requests
from PIL import Image
from requests.exceptions import RequestException
import logging
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

API_URL = "http://localhost:8000"

st.set_page_config(
    page_title="Expert Ingrijire Plante",
    page_icon="🪴",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Interactiune cu API
def send_query(text):
    from constants import (API_ERROR_QUERY, API_GENERIC_RESPONSE_FAIL)
    try:
        local_response = requests.post(f"{API_URL}/query",
                                       json={"text": text}, timeout=10)
        local_response.raise_for_status()
        return local_response.json()["response"]
    except RequestException as e:
        logging.error(API_ERROR_QUERY.format(error=str(e)))
        return API_GENERIC_RESPONSE_FAIL


def upload_plant_image(image_file):
    from constants import API_ERROR_UPLOAD
    try:
        files = {"file": (image_file.name, image_file, "image/jpeg")}
        local_response = requests.post(
            f"{API_URL}/upload-image", files=files, timeout=10)
        local_response.raise_for_status()
        return local_response.json()
    except RequestException as e:
        logging.error(API_ERROR_UPLOAD.format(error=str(e)))
        return None


# CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #2e7d32;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #388e3c;
    }
    .plant-card {
        background-color: #f1f8e9;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
    }
    .info-box {
        background-color: #e8f5e9;
        border-left: 5px solid #4caf50;
        padding: 10px;
        margin-bottom: 10px;
    }
    .chat-message {
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .user-message {
        background-color: #e3f2fd;
        border-left: 5px solid #2196f3;
    }
    .bot-message {
        background-color: #f1f8e9;
        border-left: 5px solid #4caf50;
    }
    .result-box {
        background-color: #e8f5e9;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
        text-align: center;
        font-size: 1.5rem;
        border: 2px solid #4caf50;
    }
    .stDeployButton {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)

st.sidebar.markdown(
    "<h1 class='main-header'>🪴 Plant Expert</h1>", unsafe_allow_html=True)
page = st.sidebar.radio(
    "Navigare", ["Acasă", "Chatbot", "Identificare Plantă"])

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if page == "Acasă":
    st.markdown("<h1 class='main-header'>🪴 Sistem Expert Îngrijire Plante</h1>",
                unsafe_allow_html=True)

    st.markdown("""
        <div class='info-box'>
        <h2 class='sub-header'>Bine ai venit!</h2>
        <p>Acest sistem expert te ajută să îngrijești plantele tale și să rezolvi problemele comune.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            "<h3 class='sub-header'>Ce poți face cu acest sistem?</h3>", unsafe_allow_html=True)
        st.markdown("""
            * 💬 **Chatbot** - Pune întrebări despre îngrijirea plantelor
            * 📷 **Identificare Plantă** - Încarcă o imagine pentru a identifica o plantă
        """)

    with col2:
        st.image("https://images.unsplash.com/photo-1466692476868-aef1dfb1e735",
                 use_container_width=True)

elif page == "Chatbot":
    st.markdown("<h1 class='main-header'>💬 Chatbot pentru Îngrijirea Plantelor</h1>",
                unsafe_allow_html=True)

    st.markdown("""
        <div class='info-box'>
        <p>Pune-mi orice întrebare despre îngrijirea plantelor tale! De exemplu:</p>
        <ul>
            <li>Cum îngrijesc o orhidee?</li>
            <li>De ce are ficusul meu frunze galbene?</li>
            <li>Când trebuie să ud trandafirii?</li>
        </ul>
        </div>
    """, unsafe_allow_html=True)

    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.markdown(
                f"<div class='chat-message user-message'><strong>Tu:</strong> {message['content']}</div>", unsafe_allow_html=True)
        else:
            bot_msg = message["content"].replace("\n", "<br>")
            st.markdown(
                f"<div class='chat-message bot-message'><strong>🪴 Plant Expert:</strong> {bot_msg}</div>",
                unsafe_allow_html=True)

    user_query = st.text_input("Întreabă-mă despre plante:", key="user_query")

    if st.button("Trimite"):
        if user_query:
            st.session_state.chat_history.append(
                {"role": "user", "content": user_query})
            response = send_query(user_query)
            st.session_state.chat_history.append(
                {"role": "bot", "content": response})
            st.rerun()

elif page == "Identificare Plantă":
    st.markdown("<h1 class='main-header'>📷 Identificare Plantă</h1>",
                unsafe_allow_html=True)

    st.markdown("""
        <div class='info-box'>
        <p>Încarcă o imagine cu o plantă pentru a o identifica.</p>
        </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Alege o imagine...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Imagine încărcată", use_container_width=True)

        if st.button("Identifică Planta"):
            with st.spinner("Se procesează imaginea..."):
                uploaded_file.seek(0)
                result = upload_plant_image(uploaded_file)

                if result and "plant_name" in result:
                    display_name = result.get("plant_name", "")
                    scientific_name = result.get("scientific_name", "")
                    message = result.get("message")

                    if "message" in result:
                        st.markdown(
                            f"<div class='result-box'>Plantă identificată: <strong>{scientific_name.capitalize()}</strong><br/><em>{message}</em></div>",
                            unsafe_allow_html=True
                        )
                    else:
                        st.markdown(
                            f"<div class='result-box'>Plantă identificată: <strong>{display_name.capitalize()}</strong> ({scientific_name})</div>",
                            unsafe_allow_html=True
                        )
                else:
                    st.error(
                        "Nu am putut identifica planta din imagine. Te rog să încerci cu o altă imagine.")
