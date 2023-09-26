import streamlit as st


st.title("Page 3")
st.write("Welcome to the Page 3 the app")


button = st.button('Click Here')
if button:
    st.write('You have clicked the Button')
else:
     st.write('You have not clicked the Button')