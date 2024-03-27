// takes a reference to a vec of usize (&Vec<usize>), a target<usize>, and returns a <usize>
fn binary_search(input_vec: &Vec<usize>, target: usize) -> usize {
    let mut left_pointer = 0;
    let mut right_pointer = input_vec.len() - 1;

    while left_pointer <= right_pointer {
        let midpoint = left_pointer + (right_pointer - left_pointer) / 2;

        if input_vec[midpoint] == target {
            return midpoint;
        } else if input_vec[midpoint] < target {
            left_pointer = midpoint + 1;
        } else {
            right_pointer = midpoint - 1;
        }
    }
    // case not found
    // returning the len of the vec is smart because it's always 1 more than the last index
    // since indexes start at 0
    // therefore no element of a vector could possibly be after the last index
    return input_vec.len();
}

fn main() {
    println!("Hello, world!");
}
