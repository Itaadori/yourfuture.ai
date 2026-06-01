import ollama
import streamlit as st

# set page
st.set_page_config(
    page_title="PurwoDaddy AI",
    page_icon="✡️",
    layout="centered"
)

# Model name
MODEL_NAME = "llama3.2"

# header and caption
st.header("AI Bapak Kau")
st.caption("OW YEAH YOUR PURWODADDY")

# session state
if "message" not in st.session_state:
    st.session_state.message = [
        {
            "role":"system", 
            "content":"You are a host in a podcast called TCUC"   
        }
    ]

# otak AI supaya ga lupa
for message in st.session_state.message:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# memberikan response user ke AI
if prompt := st.chat_input("Masukan pesan kamu disini!"):
    st.session_state.message.append({"role":"system", "content":prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

        # ambil response AI
    with st.chat_message("assistant"):
        with st.spinner("Loading..."):
            try:
                AI_response = ollama.chat(
                    model=MODEL_NAME,
                    messages=st.session_state.message
                    )
                text = AI_response['messages']['content']
                st.markdown(text)

                st.session_state.message.append({"role":"system", "content":text})
            except Exception as e:
                print(f"Error: {e}! Pastikan Ollama sudah di-install!")