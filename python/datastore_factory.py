from flexi_datasource import FlexiDataStore
from memory_datastore import InmemoryDataStore

class DataStoreFactory:
    def create(self,filePath:str) -> FlexiDataStore:
        return InmemoryDataStore.make(path=filePath)