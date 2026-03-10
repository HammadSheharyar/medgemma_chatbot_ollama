import streamlit as st
import ollama

# Page configuration
st.set_page_config(
    page_title="MedGemma Medical Chatbot",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 MedGemma Medical Chatbot")
st.write("Ask medical questions. This AI provides informational guidance only.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
prompt = st.chat_input("Ask a medical question...")

if prompt:

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    # Send to MedGemma
    response = ollama.chat(
        model="medgemma-local",
        messages=st.session_state.messages
    )

    answer = response["message"]["content"]

    # Save assistant message
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    with st.chat_message("assistant"):
        st.markdown(answer)

# Sidebar
with st.sidebar:
    st.header("About")

    st.write("""
    **Model:** MedGemma 4B  
    **Runtime:** Ollama  
    **Interface:** Streamlit  

    Running locally on CPU.
    """)

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

st.caption("⚠️ This tool provides informational medical content and is not a substitute for professional medical advice.")