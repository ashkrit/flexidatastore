use json::{JsonValue};
use json;
use sqlite;


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
    Box::new(EmbedDataSource {db_path})
}


fn col_type(val: &JsonValue) -> String {
    match val {
        JsonValue::Number(_) => String::from("DOUBLE"),
        _ => String::from("VARCHAR")
    }
}

fn col_value(val: &JsonValue) -> String {
    match val {
        JsonValue::Number(v) => v.to_string(),
        _ => String::from(format!(" '{val}' "))
    }
}


impl FlexDataStore for EmbedDataSource {
    fn insert(&self, table: &str, data: &str) -> () {
        println!("Table {table}  -> Db {:?}", self);

        let row = json::parse(data).unwrap();

        let cols_text = row
            .entries()
            .map(|(k, v)| {
                let col_type = col_type(v);
                format!("{k} {col_type}")
            })
            .collect::<Vec<String>>()
            .join(" ,");

        let create_sql = String::from(format!("CREATE TABLE IF NOT EXISTS {table} ( {cols_text} )"));

        println!("{:?}", create_sql);

        let connection = sqlite::open(self.db_path.as_str()).unwrap();
        connection
            .execute(create_sql)
            .unwrap();

        let cols_values = row
            .entries()
            .map(|(_, v)| { return col_value(v); })
            .collect::<Vec<String>>()
            .join(" ,");

        let insert_sql = String::from(format!("INSERT INTO {table} VALUES ( {cols_values} )"));

        println!("{:?}", insert_sql);

        connection
            .execute(insert_sql)
            .unwrap();
    }


    fn update(&self, table: &str, key_col: &str, key_val: &str, row: &str) -> () {
        todo!()
    }

    fn delete(&self, table: &str, key_col: &str, key_val: &str) -> () {
        todo!()
    }

    fn search(&self, table: &str) -> Vec<String> {
        let query = format!("SELECT * FROM {table}");
        println!("{}", query);
        let connection = sqlite::open(self.db_path.as_str()).unwrap();
        let mut statement = connection
            .prepare(query)
            .unwrap();

        let  names = statement.column_names().to_vec();

        let mut buffer: Vec<String> = Vec::new();

        while let Ok(sqlite::State::Row) = statement.next() {

            let mut row = json::object!{};

            for name in names.iter() {
                let value = statement.read::<String,_>(name.as_str()).unwrap();
                row.insert(name.as_str(), value).unwrap();
            }

            buffer.push(row.to_string());

        }
        return buffer;
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
