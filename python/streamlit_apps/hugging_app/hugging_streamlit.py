import streamlit as st
from transformers import pipeline

st.title("Hugging Face Demo")
text = st.text_input("Enter text to analyze")
model = pipeline("sentiment-analysis")
if text:
    result = model(text)
    st.write("Sentiment:", result[0]["label"])
    st.write("Confidence:", result[0]["score"])