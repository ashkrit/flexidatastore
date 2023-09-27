import streamlit as st
import requests
import pandas as pd
import json
import app_streamlit_api
import app_streamlit_sesion
import datetime

st.set_page_config(layout="wide")
st.title("Ecommerce Admin Store")

tab_crud, tab_query, tab_logs, tab_sample = st.tabs(
    ["Create Products, Customers and Orders", "Search - Query Results", "Logs - Show Activity", "Sample Payload"])


app_streamlit_sesion.init_key('counter', 0)
app_streamlit_sesion.init_key('log_messages', {
    "when": [],
    "action": [],
    "params": [],
    "result": [],
})
app_streamlit_sesion.init_key('log_df', pd.DataFrame(
    app_streamlit_sesion.get_entry('log_messages')))


def inc_message():
    app_streamlit_sesion.update_entry(
        'counter', app_streamlit_sesion.get_entry('counter') + 1)


row2_col1, row2_col2 = st.columns(2)


def execute_insert(name: str, payload: str):
    insert_result = app_streamlit_api.insert_object(name, payload)
    if (insert_result.status_code == 200):
        st.success(f"Insert {name} success")

        log_messages = app_streamlit_sesion.get_entry('log_messages')
        log_messages["when"].append(datetime.datetime.now())
        log_messages["action"].append("Insert")
        log_messages["params"].append(f"{name} - {payload}")
        log_messages["result"].append(f"Status {status_code}")

        app_streamlit_sesion.update_entry('log_df', pd.DataFrame(
            app_streamlit_sesion.get_entry('log_messages')))

        inc_message()

    else:
        st.error(f"Insert {insert_result} failed")
        st.stop()


def execute_update(object_name, update_key_name, update_key_value, payload_text):
    insert_result = app_streamlit_api.update_object(
        object_name, update_key_name, update_key_value, payload_text)
    if (insert_result.status_code == 200):
        st.success(f"Update {object_name} success")

        log_messages = app_streamlit_sesion.get_entry('log_messages')
        log_messages["when"].append(datetime.datetime.now())
        log_messages["action"].append("Update")
        log_messages["params"].append(f"{object_name} - {payload_text}")
        log_messages["result"].append(f"Status {status_code}")

        app_streamlit_sesion.update_entry('log_df', pd.DataFrame(
            app_streamlit_sesion.get_entry('log_messages')))

        inc_message()

    else:
        st.error(f"Update {insert_result} failed")
        st.stop()


def execute_delete(object_name, update_key_name, update_key_value):
    insert_result = app_streamlit_api.delete_object(object_name, update_key_name, update_key_value)
    if (insert_result.status_code == 200):
        st.success(f"Update {object_name} success")

        log_messages = app_streamlit_sesion.get_entry('log_messages')
        log_messages["when"].append(datetime.datetime.now())
        log_messages["action"].append("Delete")
        log_messages["params"].append(f"{object_name} - {payload_text}")
        log_messages["result"].append(f"Status {status_code}")

        app_streamlit_sesion.update_entry('log_df', pd.DataFrame(app_streamlit_sesion.get_entry('log_messages')))

        inc_message()

    else:
        st.error(f"Delete {insert_result} failed")
        st.stop()


with tab_crud:
    row1_col1, row1_col2, row1_col3 = st.columns(3)
    with row1_col1:
        st.write("#### Create Products, Customers and Orders")
        object_name = st.selectbox("Insert into table", [
                                   "products", "customers", "orders"])
        payload_text = st.text_area("Payload")
        st.button("Insert", key="insert_button",
                  on_click=lambda: execute_insert(object_name, payload_text))

    with row1_col2:
        st.write("#### Update Products, Customers and Orders")
        update_object_name = st.selectbox(
            "Update table", ["products", "customers", "orders"])
        update_key_name = st.text_input(
            "PK Column Name", key="update_key_name")
        update_key_value = st.text_input(
            "PK Column Name", key="update_key_value")
        update_payload_text = st.text_area(
            "Payload", key="update_payload_text")
        st.button("Update", key="update_button", on_click=lambda: execute_update(
            update_object_name, update_key_name, update_key_value, update_payload_text))

    with row1_col3:
        st.write("#### Delete Products, Customers and Orders")
        delete_object_name = st.selectbox(
            "Delete table", ["products", "customers", "orders"])
        delete_key_name = st.text_input(
            "PK Column Name", key="delete_key_name")
        delete_key_value = st.text_input(
            "PK Column Name", key="delete_key_value")
        
        st.button("Delete", key="delete_button", on_click=lambda: execute_delete(
            delete_object_name, delete_key_name, delete_key_value))

with tab_query:
    st.write("#### Show Products, Customers and Orders")
    table_name = st.selectbox(
        "Search Table", ["products", "customers", "orders"])

    if len(table_name) > 0:
        st.write(f"Showing result for {table_name}")

        table_data, status_code = app_streamlit_api.search_object(table_name)

        log_messages = app_streamlit_sesion.get_entry('log_messages')
        log_messages["when"].append(datetime.datetime.now())
        log_messages["action"].append("Search")
        log_messages["params"].append(f"{table_name}")
        log_messages["result"].append(
            f"Status {status_code} - {table_data.size} Rows")
        app_streamlit_sesion.update_entry('log_df', pd.DataFrame(
            app_streamlit_sesion.get_entry('log_messages')))

        inc_message()

        if (status_code == 200):
            st.write(table_data)
        else:
            st.error(f"Server return error {status_code}")

    else:
        st.stop()


with tab_logs:
    st.write(
        f"#### Show users actions {app_streamlit_sesion.get_entry('counter')} Messages")
    table = st.empty()
    table.dataframe(app_streamlit_sesion.get_entry('log_df'))

with tab_sample:
    st.write("#### Sample Payload")

    row1_col1, row1_col2, row1_col3 = st.columns(3)

    with row1_col1:
        st.write("### Products")
        p = {
            "product_id": "2",
            "name": "Laptop",
            "price": 3500
        }
        st.write(p)

    with row1_col2:
        st.write("### Customers")
        p = {"customer_id":"1","name":"John","age":25}
        st.write(p)

    with row1_col3:
        st.write("### Orders")
        p = {"order_id":"2", "order_date":"2021-01-01","customer_id":"2","product_id":"2","quantity":3}
        st.write(p)
