from flexi_datasource import FlexiDataStore,SearchParams
import sqlite3
import logging
import sys
import json


class SQLiteDataStore(FlexiDataStore):
    def __init__(self,dbPath:str):
        self.data = {}
        self.data["dbpath"] = dbPath
        self.conn = sqlite3.connect(dbPath,check_same_thread=False)
        logging.info(f"Connected to DB {self.conn}")


    def delete(self, table:str,key_col:str,key_val:str):
        logging.info(f"Deleting {key_val} from {table}")
        cursor = self.conn.cursor()
        delete_sql = f"DELETE FROM {table} WHERE {key_col} = {key_val}"
        cursor.execute(delete_sql)
        cursor.close()
        self.conn.commit()

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
            

    def update(self, table:str,key_col:str,key_val:str, row:str):
        logging.info(f"Updating {key_val} in {table}")
        cursor = self.conn.cursor()
        record = json.loads(row)
        cursor = self.conn.cursor()
        update_sql = f"UPDATE {table} SET "
        for k in record.keys():
            update_sql += f"{k} = '{record[k]}', "

        update_sql = update_sql[:-2]
        update_sql += f" WHERE {key_col} = {key_val}"
        cursor.execute(update_sql)
        cursor.close()
        self.conn.commit()    
    
    def search(self,table_name:str,params:SearchParams=None,limit:int=100) -> list[str]:

        cursor = self.conn.cursor()

        if params is not None:
            sql = f"SELECT * FROM {table_name} WHERE {params.where_clause()} LIMIT {limit}"
        else:
            sql = f"SELECT * FROM {table_name}  LIMIT {limit}"    

        logging.info(f"Executing SQL {sql}")    

        data = cursor.execute(sql)
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