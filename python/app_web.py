from flask import Flask,request,jsonify
from flexi_datasource import SearchParams
from datastore_factory import DataStoreFactory
import json
import logging
import sys



app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/api/search/<tablename>' , methods=['GET'])
def search(tablename:str):
    q = request.args.get('q')
    logging.info(f"Searching in table {tablename} for {q}")

    params = None
    if q is not None:
        query_params = json.loads(q)
        params =SearchParams()
        for k,v in query_params.items():
            params.append(k,v["op"],v["value"])

    results = ds.search(tablename,params)    

    return  jsonify(results)

@app.route('/api/insert/<tablename>' , methods=['POST'])
def insert(tablename:str):
    logging.info(f"Inserting into table {tablename}")
    data = request.get_json()
    ds.insert(tablename,json.dumps(data))
    return jsonify({
        "table":tablename,
        "data":data
    })

dbLocation = sys.argv[1]
ds = DataStoreFactory().create(dbLocation)
app.run(host='0000000', port=80)