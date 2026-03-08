import streamlit as st
import google.generativeai as genai

# Page settings
st.set_page_config(
    page_title="Sreyas AI",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>

.main {
background: linear-gradient(135deg,#0f172a,#020617);
color:white;
}

.title {
text-align:center;
font-size:48px;
font-weight:700;
background: linear-gradient(90deg,#38bdf8,#818cf8);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
margin-bottom:10px;
}

.subtitle{
text-align:center;
color:#94a3b8;
margin-bottom:30px;
}

.chat-container{
background:rgba(255,255,255,0.05);
padding:20px;
border-radius:15px;
backdrop-filter: blur(10px);
}

.user{
background:#1e293b;
padding:12px 16px;
border-radius:12px;
margin:10px 0;
text-align:right;
}

.bot{
background:#2563eb;
padding:12px 16px;
border-radius:12px;
margin:10px 0;
}

textarea{
border-radius:10px !important;
}

.stButton>button{
background:linear-gradient(90deg,#3b82f6,#6366f1);
color:white;
border:none;
padding:10px 20px;
border-radius:10px;
font-weight:bold;
}

.stButton>button:hover{
transform:scale(1.05);
transition:0.2s;
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🤖 Sreyas AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your personal AI assistant</div>', unsafe_allow_html=True)

# Gemini setup
key = "YOUR_API_KEY"
genai.configure(api_key=key)

model = genai.GenerativeModel(model_name="gemini-2.5-flash")
chat = model.start_chat()

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat container
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user">🧑 {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot">🤖 {msg["content"]}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Input
user_input = st.text_input("Ask something...")

# Ask button
if st.button("🚀 Ask AI"):
    if user_input:

        st.session_state.messages.append({
            "role":"user",
            "content":user_input
        })

        result = chat.send_message(user_input)

        st.session_state.messages.append({
            "role":"bot",
            "content":result.text
        })

        st.rerun()