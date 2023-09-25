from flexi_datasource import FlexiDataStore
from memory_datastore import SQLiteDataStore

class DataStoreFactory:
    def create(self,filePath:str) -> FlexiDataStore:
        return SQLiteDataStore.make(path=filePath)