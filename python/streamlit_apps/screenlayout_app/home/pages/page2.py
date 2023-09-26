import streamlit as st


st.title("Page 2")
st.write("Welcome to the Page 2 the app")

#Defining Columns
c1, c2, c3 = st.columns(3)
# Defining Metrics

c1.metric("Rainfall", "100 cm", "10 cm")
c2.metric(label="Population", value="123 Billions", delta="1 Billions", delta_color="inverse")
c3.metric(label="Customers", value=100, delta=10, delta_color="off")