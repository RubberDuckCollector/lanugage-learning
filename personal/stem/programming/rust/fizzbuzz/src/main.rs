// 2024-03-25

fn fizzbuzz_modular(i: u128) {
    match (i % 3, i % 5) {
        (0, 0) => println!("fizzbuzz"),
        (0, _) => println!("fizz"),
        (_, 0) => println!("buzz"),
        _ => println!("{}", i),
    }
}

fn main() {
    for i in 1..101 {
        fizzbuzz_modular(i);
    }
}
