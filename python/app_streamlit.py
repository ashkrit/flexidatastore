import streamlit as st
import requests
import pandas as pd
import json
import app_streamlit_api
import app_streamlit_sesion
import datetime

st.set_page_config(layout="wide")
st.title("Ecommerce Admin Store")

tab_query, tab_crud,tab_logs = st.tabs(["Query Results","Create Products, Customers and Orders","Logs - Show Activity"]);


app_streamlit_sesion.init_key('counter',0)
app_streamlit_sesion.init_key('log_messages',{
    "when":[],
    "action":[],
    "params":[],
    "result":[],
})
app_streamlit_sesion.init_key('log_df',pd.DataFrame(app_streamlit_sesion.get_entry('log_messages')))

def inc_message():
     app_streamlit_sesion.update_entry('counter', app_streamlit_sesion.get_entry('counter') + 1)

row2_col1,row2_col2 = st.columns(2)

def execute_insert(name:str, payload:str):
    insert_result = app_streamlit_api.insert_object(name,payload)
    if(insert_result.status_code == 200):
        st.success(f"Insert {name} success")
        
        log_messages= app_streamlit_sesion.get_entry('log_messages')
        log_messages["when"].append(datetime.datetime.now())
        log_messages["action"].append("Insert")
        log_messages["params"].append(f"{name} - {payload}")
        log_messages["result"].append(f"Status {status_code}")

        app_streamlit_sesion.update_entry('log_df', pd.DataFrame(app_streamlit_sesion.get_entry('log_messages')))

        inc_message()
        
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

        log_messages= app_streamlit_sesion.get_entry('log_messages')
        log_messages["when"].append(datetime.datetime.now())
        log_messages["action"].append("Search")
        log_messages["params"].append(f"{table_name}")
        log_messages["result"].append(f"Status {status_code} - {table_data.size} Rows")
        app_streamlit_sesion.update_entry('log_df', pd.DataFrame(app_streamlit_sesion.get_entry('log_messages')))

        inc_message()
    
        if(status_code == 200):
            st.write(table_data)
        else:    
            st.error(f"Server return error {status_code}")

    else:
        st.stop()    



with tab_logs:
    st.write(f"#### Show users actions {app_streamlit_sesion.get_entry('counter')} Messages")
    table = st.empty()
    table.dataframe(app_streamlit_sesion.get_entry('log_df'))