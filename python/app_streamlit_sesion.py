import streamlit as st

def init_key(key:str,value):
    if key not in st.session_state:
        st.session_state[key]=value

def get_entry(key:str):
    return st.session_state[key]

def update_entry(key:str,value):
    st.session_state[key]=value