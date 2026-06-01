import streamlit as st
from openai import OpenAI

# 1. Konfigurasi Halaman
st.set_page_config(page_title="YourFuture.ai", page_icon="🔮", layout="centered")

# 2. Inisialisasi Client OpenAI (mengarah ke OpenRouter)
# Pastikan OPENROUTER_API_KEY sudah diisi di Streamlit Secrets
try:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=st.secrets["OPENROUTER_API_KEY"]
    )
except Exception as e:
    st.error("API Key tidak ditemukan. Pastikan sudah mengisi st.secrets!")
    st.stop()

# 3. Inisialisasi Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system", 
            "content": "You are a kind, humble, and intuitive female future-predictor. You speak with a caring personality. Answer just enough phrases don't sugarcoat it. Answer only in Bahasa Indonesia!"
        }
    ]

# 4. Tampilan Header
st.header("YourFuture.ai 🔮")
st.caption("Predict Your Future In One Click!")

# 5. Render History Chat
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# 6. Logika Input & Chat
if prompt := st.chat_input("Apa yang ingin kamu ketahui tentang masa depan?"):
    # Simpan dan tampilkan input user
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        
    # Panggil API
    with st.chat_message("assistant"):
        with st.spinner("Membaca garis takdir..."):
            try:
                response = client.chat.completions.create(
                    model="nvidia/nemotron-3-super-120b-a12b:free",
                    messages=st.session_state.messages
                )
                
                content = response.choices[0].message.content
                st.markdown(content)
                
                # Simpan respon ke state
                st.session_state.messages.append({"role": "assistant", "content": content})
                    
            except Exception as e:
                st.error(f"Terjadi kesalahan saat menghubungi server AI: {e}")
