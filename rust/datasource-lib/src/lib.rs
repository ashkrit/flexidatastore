use json::{JsonValue};
use json;
use sqlite;
use sqlite::Connection;


pub trait FlexDataStore {
    fn insert(&self, table: &str, data: &str) -> ();
    fn update(&self, table: &str, key_col: &str, key_val: &str, row: &str) -> ();
    fn delete(&self, table: &str, key_col: &str, key_val: &str) -> ();
    fn search(&self, table: &str) -> Vec<String>;
}

#[derive(Debug)]
pub struct EmbedDataSource {
    pub db_path: String,
}


pub fn flex_datasource(db_path: String) -> Box<dyn FlexDataStore> {
    Box::new(EmbedDataSource { db_path })
}


impl FlexDataStore for EmbedDataSource {
    fn insert(&self, table: &str, data: &str) -> () {
        println!("Table {table}  -> Db {:?}", self);

        let row = json::parse(data).unwrap();

        let cols_text = row
            .entries()
            .map(|(k, v)| {
                let col_type = self.col_type(v);
                format!("{k} {col_type}")
            })
            .collect::<Vec<String>>()
            .join(" ,");

        let create_sql = String::from(format!("CREATE TABLE IF NOT EXISTS {table} ( {cols_text} )"));

        let connection = self.open_connection();
        connection
            .execute(create_sql)
            .unwrap();

        let cols_values = row
            .entries()
            .map(|(_, v)| { return self.col_value(v); })
            .collect::<Vec<String>>()
            .join(" ,");

        let insert_sql = String::from(format!("INSERT INTO {table} VALUES ( {cols_values} )"));

        connection
            .execute(insert_sql)
            .unwrap();
    }


    fn update(&self, table: &str, key_col: &str, key_val: &str, row: &str) -> () {
        let row = json::parse(row).unwrap();

        let cols_values = row
            .entries()
            .map(|(k, v)| format!("{k}='{v}' "))
            .collect::<Vec<String>>()
            .join(",");

        let query = format!("UPDATE {table} SET {cols_values} WHERE {key_col}={key_val}");
        let connection = self.open_connection();
        connection.execute(query).unwrap();
    }

    fn delete(&self, table: &str, key_col: &str, key_val: &str) -> () {
        let query = format!("DELETE FROM {table} WHERE {key_col} = {key_val}");
        let connection = self.open_connection();
        connection.execute(query).unwrap();
    }

    fn search(&self, table: &str) -> Vec<String> {
        let query = format!("SELECT * FROM {table}");
        println!("{}", query);
        let connection = self.open_connection();
        let mut statement = connection
            .prepare(query)
            .unwrap();

        let names = statement.column_names().to_vec();

        let mut buffer: Vec<String> = Vec::new();

        while let Ok(sqlite::State::Row) = statement.next() {
            let mut row = json::object! {};

            for name in names.iter() {
                let value = statement.read::<String, _>(name.as_str()).unwrap();
                row.insert(name.as_str(), value).unwrap();
            }

            buffer.push(row.to_string());
        }
        return buffer;
    }
}

impl EmbedDataSource {
    fn open_connection(&self) -> Connection {
        sqlite::open(self.db_path.as_str()).unwrap()
    }

    fn col_type(&self, val: &JsonValue) -> String {
        match val {
            JsonValue::Number(_) => String::from("DOUBLE"),
            _ => String::from("VARCHAR")
        }
    }

    fn col_value(&self, val: &JsonValue) -> String {
        match val {
            JsonValue::Number(v) => v.to_string(),
            _ => String::from(format!(" '{val}' "))
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let ds = EmbedDataSource {
            db_path: String::from("/Users/ashkrit/_tmp/db/rust_ecom_2.db")
        };


        let product = object! {
            "product_id":"1",
            "name":"Laptop",
            "price":1000
        };


        //ds.insert("products", product.to_string().as_str());
        let r = ds.search("products");
        println!("{:?}", r);
    }
}
