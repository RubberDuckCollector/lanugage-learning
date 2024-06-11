// 2024-03-26

fn loop_through_vector() {
    let nums = vec![1, 2, 3, 4, 5, 6, 7, 8, 9];

    println!("nums: {:?}", nums);

    for i in &nums {
        println!("num: {}", *i);
    }
}

fn main() {
    loop_through_vector();
}
