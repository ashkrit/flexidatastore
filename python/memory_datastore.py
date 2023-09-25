from flexi_datasource import FlexiDataStore
import sqlite3
import logging
import sys


class SQLiteDataStore(FlexiDataStore):
    def __init__(self,dbPath:str):
        self.data = {}
        self.data["dbpath"] = dbPath
        self.conn = sqlite3.connect(dbPath)
        logging.info(f"Connected to DB {self.conn}")


    def delete(self, key):
        del self.data[key]

    def insert(self, key):
        
        self.data[key] = key    

    def update(self, key):
        self.data[key] = key        

    def list(self):
        return self.data.keys()
    
    def search(self):
        return self.data.keys()
    
    def __repr__(self):
        return "InmemoryDataStore()"

    def __str__(self):
        return f"InmemoryDataStore() {self.data}"
    
    @staticmethod
    def make(path:str) -> FlexiDataStore:
        return SQLiteDataStore(path)