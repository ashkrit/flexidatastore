from flexi_datasource import FlexiDataStore
from datastore_factory import DataStoreFactory
import sys
import logging
import sys
import json

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

    products = []
    products.append({"product_id":"1","name":"Laptop","price":1000})
    products.append({"product_id":"2","name":"Mobile","price":500})
    products.append({"product_id":"3","name":"Tablet","price":200})
    products.append({"product_id":"4","name":"Television","price":1000})

    """
    for product in products:
        ds.insert("products", json.dumps(product))
    """
    

    logging.info(f"Created products {products}")

    result = ds.search("products")

    logging.info(f"Search result {result}")


    
if __name__=="__main__":
    main()   

