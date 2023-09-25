from flexi_datasource import FlexiDataStore
from datastore_factory import DataStoreFactory




def main():
    print("Staring App")

    ds = DataStoreFactory().create()

    print(ds)

    



if __name__=="__main__":
    main()   

