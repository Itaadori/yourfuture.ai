import streamlit as st
import ollama

# Konfigurasi halaman
st.set_page_config(
    page_title="Local AI Chatbot",
    page_icon="🦙",
    layout="centered"
)

# Tentukan model Ollama yang ingin dipakai (pastikan sudah di-pull)
# Contoh: llama3, mistral, gemma, atau qwen2
MODEL_NAME = "llama3.2"

st.title("💬 Local AI Chatbot")
st.caption(f"Powered by Ollama (Model: {MODEL_NAME})")

# st.session_state = "memori" antar-interaksi di Streamlit
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a humble, reassuring yet intruistic and empathetic father figure called Purwo from Indonesia and answer using bahasa Indonesia only"
        }
    ]

# Tampilkan semua pesan sebelumnya (kecuali system message)
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Input dari user
if prompt := st.chat_input("Ketik pesan kamu di sini..."):
    
    # Tampilkan pesan user
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate response dari Ollama
    with st.chat_message("assistant"):
        with st.spinner("Sedang berpikir..."):
            try:
                # Memanggil API lokal Ollama
                response = ollama.chat(
                    model=MODEL_NAME,
                    messages=st.session_state.messages
                )
                
                # Ekstrak teks dari response Ollama
                assistant_reply = response['message']['content']
                st.markdown(assistant_reply)
                
                # Simpan response ke history
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": assistant_reply
                })
                
            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}. Pastikan aplikasi Ollama sudah berjalan di background!")

# Sidebar dengan info
with st.sidebar:
    st.header("Tentang Chatbot Ini")
    st.write("Berjalan 100% secara lokal tanpa akses internet ke API eksternal.")
    st.write(f"Pesan dalam sesi ini: {len(st.session_state.messages) - 1}")
    if st.button("Reset Percakapan"):
        st.session_state.messages = [st.session_state.messages[0]]
        st.rerun()