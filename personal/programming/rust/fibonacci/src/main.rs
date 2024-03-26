use std::time::Instant;

// 2024-03-25

fn fib_it(n: i128) -> i128 {
    let mut a: i128 = 0;
    let mut b: i128 = 1;
    let mut c: i128;

    if n < 0 {
        -1
    } else if n == 0 {
        a
    } else if n == 1 {
        b
    } else {
        // not using the iterative variable so make it clear by calling it a _
        for _ in 2..n + 1 {
            c = a + b;
            a = b;
            b = c;
        }
        b
    }
}

fn fib_rec(n: i128) -> i128 {
    if n < 2 {
        n
    } else {
        fib_rec(n - 1) + fib_rec(n - 2)
    }
}

fn main() {
    let test_nums = vec![10, 20, 25, 30, 35, 40, 100];

    // reference test nums as we're looping through it
    // the program wants the memory location of the vector and then goes to the vector in memory to
    // access it

    // ITERATIVE
    println!("iterative");
    for i in &test_nums {
        let before_count_time = Instant::now();

        println!("current int: {}", i);

        let result = fib_it(*i);
        println!("result: {}", result);

        println!("time taken: {:?}", before_count_time.elapsed());
    }

    println!("\n");

    // RECURSIVE
    println!("recursive");
    for i in &test_nums {
        let before_count_time = Instant::now();

        println!("current test int: {}", i);

        // here, i is a reference to each element in the vector test_nums
        // we dereference i because it starts out as a referenced piece of data
        // we do this to access the value of i, which is the index of test_nums
        // if i isn't dereferenced, we'd be passing a REFERENCE to an i32, instead of an actual int
        // value, meaning that the function being called, fib_rec(), would have to deal with an int
        // reference, not an int
        let result = fib_rec(*i);
        println!("result: {}", result);

        println!("time taken: {:?}", before_count_time.elapsed());
    }
}
