import gradio as gr
import google.generativeai as genai
import time

genai.configure(api_key="AIzaSyBQLOmf273y-2R5Snvo7K0QwKC4j-veHV0")

model = genai.GenerativeModel("gemini-2.5-flash")

def ask_football_question(question):
    try:
        response = model.generate_content(
            f"""
            You are an expert football (soccer) historian and analyst with knowledge up to May 2026.

            Answer clearly and concisely.

            Question: {question}
            """
        )
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"

interface = gr.Interface(
    fn=ask_football_question,
    inputs=gr.Textbox(lines=4, placeholder="Ask anything about football..."),
    outputs="text",
    title="Football Expert Chatbot"
)

if __name__ == "__main__":
    interface.launch()