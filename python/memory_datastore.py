from flexi_datasource import FlexiDataStore
import sqlite3
import logging
import sys
import json


class SQLiteDataStore(FlexiDataStore):
    def __init__(self,dbPath:str):
        self.data = {}
        self.data["dbpath"] = dbPath
        self.conn = sqlite3.connect(dbPath)
        logging.info(f"Connected to DB {self.conn}")


    def delete(self, key):
        del self.data[key]

    def insert(self, table:str,value:str):
        logging.info(f"Inserting {value} into {table}")   
        record = json.loads(value)

        col = [ (key,self.column_type(record[key]) ) for key in record.keys()]
        col_text = ", ".join( [f"{c}  {t}" for (c,t) in col])
        create_table = f"CREATE TABLE IF NOT EXISTS {table} ( {col_text} )"
        cursor = self.conn.cursor()
        cursor.execute(create_table)

        col_values = ", ".join([ f"'{record[key]}'"  for key in record.keys()])

        insert_sql = f"INSERT INTO {table} VALUES ({col_values})"
        cursor.execute(insert_sql)
        cursor.close()
        self.conn.commit()

    def column_type(self, v) -> str:
        if isinstance(v,str):
            return 'VARCHAR'
        elif isinstance(v,int):
            return 'INT'
        elif isinstance(v,float):
            return 'DOUBLE'
        else:
            return'VARCHAR'  
            
            


    def update(self, key):
        self.data[key] = key        
    
    def search(self,table_name:str) -> list[str]:
        cursor = self.conn.cursor()
        data = cursor.execute(f"SELECT * FROM {table_name}")
        results = []
        col_names = [d[0] for d in data.description]
    
        for r in data.fetchall():
            row = dict(zip(col_names,r))
            results.append(json.dumps(row))
        return results
        
    def __repr__(self):
        return "InmemoryDataStore()"

    def __str__(self):
        return f"InmemoryDataStore() {self.data}"
    
    @staticmethod
    def make(path:str) -> FlexiDataStore:
        return SQLiteDataStore(path)