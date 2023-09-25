from flexi_datasource import FlexiDataStore
from datastore_factory import DataStoreFactory
import sys




def main():
    
    dbLocation = sys.argv[1]

    ds = DataStoreFactory().create(dbLocation)

    print(ds)

    
if __name__=="__main__":
    main()   

