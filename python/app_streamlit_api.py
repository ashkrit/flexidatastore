import requests
import json
import pandas as pd



base_url:str = "http://localhost"

def insert_object(name: str, payload: str) -> requests.Response:
    url = f"{base_url}/api/insert/{name}"
    print(f"Sennding {payload} to {name}")
    headers = {
        'Content-Type': "application/json"
    }
    return requests.post(url, data=payload, headers=headers)

def update_object(name: str, key_column:str,key_value:str, payload: str) -> requests.Response:
    url = f"{base_url}/api/update/{name}/{key_column}/{key_value}"
    print(f"Sennding {payload} to {name}")
    headers = {
        'Content-Type': "application/json"
    }
    return requests.put(url, data=payload, headers=headers)

def delete_object(name: str, key_column:str,key_value:str) -> requests.Response:
    url = f"{base_url}/api/delete/{name}/{key_column}/{key_value}"
    print(f"Deleting {name} with {key_column} = {key_value}")
    headers = {
        'Content-Type': "application/json"
    }
    return requests.delete(url,headers=headers)


def search_object(table_name: str) -> (pd.DataFrame,int):
    search_url = f"{base_url}/api/search/{table_name}"
    search_result=requests.get(search_url)
    if(search_result.status_code == 200):
        table_data = _create_dataframe(search_result)
        return (table_data,search_result.status_code)
    else:
        return (pd.DataFrame(),search_result.status_code)

def _create_dataframe(search_result):
    table_data = pd.DataFrame(search_result.json())

    col_names = _extract_cols_names(table_data)
    _flat_columns(table_data, col_names)
        
    table_data.drop(0,axis="columns",inplace=True)
    return table_data

def _flat_columns(table_data, col_names):
    for c in col_names:
        if(table_data.columns.to_list().count(c) == 0):
            table_data[c] = table_data[0].map( lambda x : json.loads(x)).map(lambda x : x[c])

def _extract_cols_names(table_data:pd.DataFrame) -> list[str]:
    cols = table_data[0].map( lambda x : json.loads(x)).map(lambda x : x.keys()).drop_duplicates().to_list()
    col_names =[cname for keys in cols for cname in keys]
    return col_names