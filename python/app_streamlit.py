import streamlit as st
import requests
import pandas as pd
import json
import app_streamlit_api

st.set_page_config(layout="wide")
st.title("Ecommerce Admin Store")

tab_query, tab_crud,tab_logs = st.tabs(["Query Results","Create Products, Customers and Orders","Logs - Show Activity"]);



if 'log_messages' not in st.session_state:
    st.session_state.log_messages = log_messages = {
    "action":[],
    "params":[],
    "result":[],
}

if 'log_df' not in st.session_state:
    st.session_state.log_df = pd.DataFrame(st.session_state.log_messages)


row2_col1,row2_col2 = st.columns(2)

def execute_insert(name:str, payload:str):
    insert_result = app_streamlit_api.insert_object(name,payload)
    if(insert_result.status_code == 200):
        st.success(f"Insert {name} success")
        
        st.session_state.log_messages["action"].append("Insert")
        st.session_state.log_messages["params"].append(f"{name} - {payload}")
        st.session_state.log_messages["result"].append(f"Status {status_code}")

        st.session_state.log_df = pd.DataFrame(st.session_state.log_messages)
        
    else:
        st.error(f"Insert {insert_result} failed")
        st.stop()
        

with tab_crud:
    row1_col1, row1_col2,row1_col3 = st.columns(3)
    with row1_col1:
        st.write("#### Create Products, Customers and Orders")
        object_name = st.selectbox("Insert into table", ["products","customers","orders"])
        payload_text = st.text_area("Payload")
        st.button("Insert", key="insert_button", on_click=lambda: execute_insert(object_name, payload_text))
        
    with row1_col2:
        st.write("#### Update Products, Customers and Orders")
    with row1_col3:
        st.write("#### Delete Products, Customers and Orders")            

with tab_query:
    st.write("#### Show Products, Customers and Orders")
    table_name = st.selectbox("Search Table", ["products","customers","orders"])

    if len(table_name) > 0 :
        st.write(f"Showing result for {table_name}")

        table_data,status_code =app_streamlit_api.search_object(table_name)

        st.session_state.log_messages["action"].append("Search")
        st.session_state.log_messages["params"].append(f"{table_name}")
        st.session_state.log_messages["result"].append(f"Status {status_code} - {table_data.size} Rows")

        st.session_state.log_df = pd.DataFrame(st.session_state.log_messages)
        
      
        if(status_code == 200):
            st.write(table_data)
        else:    
            st.error(f"Server return error {status_code}")

    else:
        st.stop()    



with tab_logs:
    st.write("#### Show users actions")
    table = st.empty()
    table.dataframe(st.session_state.log_df)