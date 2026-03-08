import streamlit as st
import google.generativeai as genai
import pandas as pd

df = pd.read_csv("student_dataset.csv")

key = "AIzaSyCKRIGDh9a5-YIZ1DEHQ011yZLHbfcPY8I"
genai.configure(api_key=key)

model = genai.GenerativeModel(model_name="gemini-2.5-flash")
chat = model.start_chat()

st.title("Sreyas AI Chatbot")
user_input = st.text_area("Enter your Question!")

if st.button("Ask"):
    df = df.to_string()
    prompt = f"""you are an data analyst, here is my rapido data:{df} 
    Answer the question based on this dataset. Question: {user_input}
    """
    result = model.generate_content(prompt)
    st.write(result.text)