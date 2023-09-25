use datasource_lib::FlexDataStore;
use datasource_lib::flex_datasource;
use json::object;

fn main() {


    let ds = flex_datasource(String::from("/Users/ashkrit/_tmp/db/rust_ecom_2.db"));

    let mut produts = vec![];
    produts.push(object! {
            "product_id":"1",
            "name":"Laptop",
            "price":1000
    });

    produts.push(object! {
            "product_id":"2",
            "name":"Mobile",
            "price":560
    });

    produts.push(object! {
            "product_id":"3",
            "name":"TV",
            "price":3000
    });

    for product in produts {
        ds.insert("products", product.to_string().as_str());
    }


    let r = ds.search("products");

    println!("Rows {:?}", r);
}
