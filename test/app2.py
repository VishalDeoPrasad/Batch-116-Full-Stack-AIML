import streamlit as st
import google.generativeai as genai

# Configure API key
API_KEY = 'AIzaSyBQLOmf273y-2R5Snvo7K0QwKC4j-veHV0'
genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel(model_name='gemini-2.5-flash')
chat = model.start_chat()

# Streamlit UI
st.title("Gemini AI Chatbot")
st.write("Ask anything to Gemini AI")

# User input
user_input = st.text_area("💬 Enter your prompt:", "Tell me about Python", height=150)

if st.button("Generate Response"):
    if user_input.strip():
        response = chat.send_message(user_input)
        st.subheader("Response:")
        st.write(response.text)
    else:
        st.warning("Please enter a prompt before generating a response.")