# What is this project about

this project contains code from streamlit , generic database library and REST api opening database library

## Which scripts are important

### Standalone App
```
python3 app_main.py ~/_tmp/db/amazon.db
```

### Web App

```
python3 app_web.py ~/_tmp/db/amazon.db
```

#### REST API endpoint 

##### Create
POST http://localhost/api/insert/{tablename}

```
{"customer_id":"1","name":"John","age":25}
```

##### Update
PUT http://localhost/api/update/{tablename}/{pk}/2

```
{

    "age": 30
}
```


##### Search
GET http://localhost/api/search/{tablename}

##### Delete
DELETE http://localhost/api/delete/{tablename}/{pk}/2