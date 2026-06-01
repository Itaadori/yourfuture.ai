import streamlit as st
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="YOUR_OPENROUTER_API_KEY" 
)

with st.spinner("Loading..."):
    try:
        response = client.chat.completions.create(
            model="nvidia/nemotron-3-super-120b-a12b:free",
            messages=st.session_state.messages
        )
        
        content = response.choices[0].message.content
        st.markdown(content)
        
        st.session_state.messages.append({"role": "assistant", "content": content})
            
    except Exception as e:
        st.error(f"Error: {e}")
