from flexi_datasource import FlexiDataStore,SearchParams
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
    
    db_location = sys.argv[1]

    ds = DataStoreFactory().create(db_location)


    logging.info(f"Created data store {ds}")

    products = []
    products.append({"product_id":"1","name":"Laptop","price":1000})
    products.append({"product_id":"2","name":"Mobile","price":500})
    products.append({"product_id":"3","name":"Tablet","price":200})
    products.append({"product_id":"4","name":"Television","price":1000})


    """
    for product in products:
        ds.insert("products", json.dumps(product))
    logging.info(f"Created products {products}")    
    """
    
    result = ds.search("products")
    logging.info(f"Search result {result}")

    search_params = SearchParams()
    search_params.append("price", ">=",500)
    result = ds.search("products", search_params , limit=2)
    logging.info(f"Search result {result}")


    ds.delete("products", "product_id", "1")
    result = ds.search("products")
    logging.info(f"Search result {result}")

    ds.update("products", "product_id", "4",json.dumps( {"price":1025}))
    result = ds.search("products")
    logging.info(f"Search result {result}")

    customers = []
    customers.append({"customer_id":"1","name":"John","age":25})
    customers.append({"customer_id":"2","name":"Peter","age":30})
    customers.append({"customer_id":"3","name":"Mary","age":35})
    customers.append({"customer_id":"4","name":"Jane","age":40})
    customers.append({"customer_id":"5","name":"Mark","age":45})
    customers.append({"customer_id":"6","name":"Steve","age":50})
    customers.append({"customer_id":"7","name":"Bill","age":55})

    for customer in customers:
        ds.insert("customers", json.dumps(customer))

    result = ds.search("customers")
    logging.info(f"Search result {result}")


    orders = []
    orders.append({"order_id":"1", "order_date":"2021-01-01","customer_id":"1","product_id":"1","quantity":2})

    orders.append({"order_id":"2", "order_date":"2021-01-01","customer_id":"2","product_id":"2","quantity":3})
    orders.append({"order_id":"2", "order_date":"2021-01-01","customer_id":"2","product_id":"1","quantity":3})
    orders.append({"order_id":"2", "order_date":"2021-01-01","customer_id":"2","product_id":"3","quantity":1})
    
    orders.append({"order_id":"3", "order_date":"2021-01-01","customer_id":"3","product_id":"3","quantity":4})

    for order in orders:
        ds.insert("orders", json.dumps(order))

    result = ds.search("orders")
    logging.info(f"Search result {result}")
    
if __name__=="__main__":
    main()   

