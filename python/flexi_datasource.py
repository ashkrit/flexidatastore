from abc import ABC, abstractmethod

class FlexiDataStore(ABC):


    @abstractmethod
    def insert(Self,table:str,value:str):
        pass

    @abstractmethod
    def update(Self):
        pass

    @abstractmethod
    def delete(Self):
        pass
    
    @abstractmethod
    def search(Self,table:str) -> list[str]:
        pass