import ollama
import streamlit as st

st.set_page_config(
    page_title="AI Masa Kini 🚀",
    page_icon="🤖",
    layout="centered"
)

MODEL_NAME = "llama3.2"

st.header("YourFuture.ai")
st.caption("Predict Your Future In One Click!")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role":"system",
            "content":"A female future-predictor, sort of like a kind witch who knows the future for this AI's user, have inruistic, humble, caring personality!"
        }
    ]

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("Masukkan pesan kamu disini!"):
    st.session_state.messages.append({"role":"user", "content":prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        
        
    with st.chat_message("assistant"):
        with st.spinner("Loading..."):
             try:
                API_calling = ollama.chat(
                    model=MODEL_NAME,
                    messages=st.session_state.messages)
                    
                response = API_calling['message']['content']
                st.markdown(response)

                st.session_state.messages.append({
                    "role":"assistant",
                    "content":response 
                    })
                    
             except Exception as e:
                st.error(f"Error: {e}. Please do install Ollama on your device!")
