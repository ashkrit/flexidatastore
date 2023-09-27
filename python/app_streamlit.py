import streamlit as st
import requests
import pandas as pd
import json

st.set_page_config(layout="wide")
st.title("Ecommerce Admin Store")

tab_query, tab_crud = st.tabs(["Query Results","Products, Customers and Orders"]);

base_url="http://localhost"

row2_col1,row2_col2 = st.columns(2)

with tab_crud:
    row1_col1, row1_col2,row1_col3 = st.columns(3)
    with row1_col1:
        st.write("#### Create Products, Customers and Orders")
    with row1_col2:
        st.write("#### Update Products, Customers and Orders")
    with row1_col3:
        st.write("#### Delete Products, Customers and Orders")            

with tab_query:
    st.write("#### Show Products, Customers and Orders")
    table_name = st.text_input("Search Products, Customers and Orders", key="search_query")
   

    if len(table_name) > 0 :
        st.write(f"Showing result for {table_name}")
        search_url = f"{base_url}/api/search//{table_name}"
        search_result=requests.get(search_url)
        if(search_result.status_code == 200):
            table_data = pd.DataFrame(search_result.json())
            
            cols = table_data[0].map( lambda x : json.loads(x)).map(lambda x : x.keys()).drop_duplicates().to_list()
            col_names =[cname for keys in cols for cname in keys]
            for c in col_names:
                if(table_data.columns.to_list().count(c) == 0):
                    table_data[c] = table_data[0].map( lambda x : json.loads(x)).map(lambda x : x[c])


            table_data.drop(0,axis="columns",inplace=True)

            st.write(table_data)
            
        else:    
            st.error(f"Server return error {search_result.status_code}")

    else:
        st.stop()    