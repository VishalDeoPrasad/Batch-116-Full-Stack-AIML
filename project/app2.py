import gradio as gr
import google.generativeai as genai
import pandas as pd

# Load dataset
df = pd.read_csv("student_dataset.csv")

# Configure API
key = "AIzaSyCKRIGDh9a5-YIZ1DEHQ011yZLHbfcPY8I"
genai.configure(api_key=key)

# Load model
model = genai.GenerativeModel(model_name="gemini-2.5-flash")

# Function for chatbot
def ask_question(user_input):
    
    data = df.to_string()

    prompt = f"""
    You are a data analyst.
    Here is my student dataset:
    {data}

    Answer the question based on this dataset.

    Question: {user_input}
    """

    result = model.generate_content(prompt)

    return result.text


# Gradio UI
interface = gr.Interface(
    fn=ask_question,
    inputs=gr.Textbox(lines=4, placeholder="Enter your question..."),
    outputs="text",
    title="Sreyas AI Chatbot",
    description="Ask questions about the student dataset"
)

interface.launch(share=True, server_name="0.0.0.0")