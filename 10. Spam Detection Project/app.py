import streamlit as st
import pandas as pd

# Sample data
df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Revenue": [300, 450, 400, 500, 600]
})

st.title("Area Chart Example")

df = df.set_index("Month")

st.area_chart(df)