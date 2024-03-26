fn main() {
    let nums = vec![1, 2, 3, 4, 5, 6, 7, 8, 9];

    for i in &nums {
        println!(
            "num: {}, index: {}",
            i,
            nums.iter().position(|i| i == num).unwrap()
        );
    }
}
