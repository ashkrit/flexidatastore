import streamlit as st


st.title("Home Page")
st.write("Welcome to the home page of the app")

st.graphviz_chart('''
    digraph {
        "Training Data" -> "ML Algorithm"
        "ML Algorithm" -> "Model"
        "Model" -> "Result Forecasting"
        "New Data" -> "Model"
    }
''')