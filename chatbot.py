import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Masa Kini 🚀", page_icon="🤖", layout="centered")

# --- INISIALISASI SESSION STATE ---
# Pastikan ini dijalankan pertama kali sebelum akses apapun ke st.session_state.messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system", 
            "content": "A female future-predictor, sort of like a kind witch who knows the future for this AI's user, have intuitive, humble, caring personality!"
        }
    ]

# Sekarang kamu bisa mengaksesnya dengan aman
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# ... sisa logika aplikasimu ...
