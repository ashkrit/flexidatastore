from flexi_datasource import FlexiDataStore
from embded_datastore import SQLiteDataStore

class DataStoreFactory:
    def create(self,filePath:str) -> FlexiDataStore:
        return SQLiteDataStore.make(path=filePath)