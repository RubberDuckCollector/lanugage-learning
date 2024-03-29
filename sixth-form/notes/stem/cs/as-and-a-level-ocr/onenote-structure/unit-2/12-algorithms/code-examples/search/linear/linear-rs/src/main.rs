// 2024-03-26
// https://rustp.org/data-structures/vector-searching
// the dot syntax in the println! statements were recommended to me by the compiler
// the function is taking in a reference to a vector, so when it's called you have to pass in a
// reference to the vector you want to search
//
// the function declaration is also using usize, which is platform dependant and represents a 32/64
// bit unsigned int (on 32 and 64 bit systems)
// this ensures that the compiler can allocate the right amount of memory for the usize, even as
// platforms change
// it's common to use it for indexing operations
// it's just like using an i32, don't panic

fn linear_search(input_vec: &Vec<usize>, target: usize) -> usize {
    for i in 0..input_vec.len() {
        if input_vec[i] == target {
            return i;
        }
    }
    // return this if the target wasn't found
    // have to return this because it's a usize and the func wants a usize as can be seen in the
    // function declaration
    return input_vec.len();
}

fn main() {
    let nums = vec![5, 4, 3, 2, 1];

    let target: i32 = 2;

    let target_2: i32 = 0;

    // pass a reference to the vector, as stated in the function declaration
    println!(
        "index of target {target} is {}",
        linear_search(&nums, target.try_into().unwrap())
    );

    println!(
        "index of target {target} is {}",
        linear_search(&nums, target_2.try_into().unwrap())
    );
}
