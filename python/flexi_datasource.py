from abc import ABC, abstractmethod

class FlexiDataStore(ABC):

    @abstractmethod
    def list(Self):
        pass

    @abstractmethod
    def insert(Self):
        pass

    @abstractmethod
    def update(Self):
        pass

    @abstractmethod
    def delete(Self):
        pass
    

    @abstractmethod
    def search(Self):
        pass