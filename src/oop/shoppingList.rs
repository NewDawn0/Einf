use std::collections::HashMap;

#[derive(Debug)]
struct Cart(HashMap<String, u64>); // Item name, amount
impl Cart {
    fn new() -> Self {
        Self(HashMap::<String, u64>::new())
    }
    fn add(&mut self, item: &str, amount: u64) {
        match &self.0.contains_key(&item.to_string()) {
            true => {
                *self.0.get_mut(&item.to_string()).unwrap() += amount;
            }
            false => {
                self.0.insert(item.to_string(), amount);
            }
        }
    }
    fn remove(&mut self, item: &str, amount: u64) {
        let curr_amount = *self.0.get(&item.to_string()).unwrap();
        match amount <= curr_amount {
            true => {
                *self.0.get_mut(&item.to_string()).unwrap() -= amount;
            }
            false => {
                self.0.remove(&item.to_string());
            }
        }
    }
    fn remove_all(&mut self) {
        self.0 = HashMap::<String, u64>::new();
    }
}

fn main() {
    let mut cart = Cart::new();
    cart.add("Apple", 1);
    cart.add("Apple", 10);
    cart.remove("Apple", 4);
    println!("{:?}", cart);
    cart.remove_all();
    println!("{:?}", cart);
}
