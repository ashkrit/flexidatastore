from abc import ABC, abstractmethod

class SearchParams():
     def __init__(self):
        self.data = {}

     def append(self,key:str,op:str, value):
        self.data[key] = (op,value)   

     def where_cluase(self) -> str :
         return " AND ".join([ f"{k} {v[0]} {self.fv(v[1])}" for k,v in self.data.items()])

     def fv(self, value) -> str :
        if isinstance(value,list):
            x = ",".join([ f"{self.fv(x)}" for x in value])     
            return f"( { x } )"
        elif isinstance(value,int) or isinstance(value,float) :
            return value
        else:     
            return f"'{value}'"   
     
     def __repr__(self):
        return "SearchParams()"

     def __str__(self):
        return f"SearchParams() {self.data}"   

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
    def search(Self,table:str,params:SearchParams=None) -> list[str]:
        pass
