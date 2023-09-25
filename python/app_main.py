from flexi_datasource import FlexiDataStore
from datastore_factory import DataStoreFactory
import sys
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)



def main():
    
    dbLocation = sys.argv[1]

    ds = DataStoreFactory().create(dbLocation)

    logging.info(f"Created data store {ds}")

    
if __name__=="__main__":
    main()   

