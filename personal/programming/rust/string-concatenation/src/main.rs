// 2024-03-24
// there are strings in rust
// String (string) and &str (string slice)
// checked by someone else: NO

fn _example() {
    // we can declare a String like this

    let _msg = String::from("hello world");

    // or like this

    let _msg = String::new(); // this seems to take on the value ""

    // or like this

    let _msg: String = "hello world".to_string();

    // we can declare a &str like this

    let _msg: &str = "hello world"; // this is not a String but a &str, a string slice

    // differences between String and &str:

    // furthermore:
    //
    // let msg = String::from("hello");
    //
    // is the same as:
    //
    // let msg: String = "hello".to_owned();
}

fn string_string() {
    println!("String and String concatenation (one const):");

    let mut msg1 = String::from("String 1 ");
    let msg2 = String::from("String 2");

    println!("msg1: {msg1}");
    println!("msg2: {msg2}");

    // push msg2 to the end of msg1
    // this is done by referencing msg2 with & when we want to push it
    msg1.push_str(&msg2);

    println!("new msg: {}\n", msg1);
}

fn string_string_const() {
    println!("String and String concatenation (both const)");

    let msg1 = String::from("msg1 ");
    let msg2 = String::from("msg2");

    println!("msg1: {}", msg1);
    println!("msg2: {}", msg2);

    let msg3 = format!("{msg1}{msg2}");

    println!("result: {}\n", msg3);
}

fn string_str() {
    println!("String and slice concatenation (one const):");

    let mut msg1: String = "Hello ".to_owned();

    // let mut msg1 = String::from("hello "); // also works

    // those 2 lines have the same outcome. we are declaring a variable, the type is String, and
    // taking ownership of it.

    let msg2: &str = "Serena!";
    // this slice is borrowing the string literal "Serena!". the literal has a static lifetime so
    // will exist for the duration of the program.
    // it's possible to borrow this literal again with anoter slice, or take ownership over it by
    // turning it into a String

    // possible to use .push_str()
    msg1.push_str(msg2);

    println!("new msg: {}", msg1); // msg1 turns into "Hello Serena!"

    // can also use + to concatenate

    let new_string: String = msg1 + msg2; // concatenates again, producing "Hello Serena!Serena"
                                          // new_string has ownership over this value

    println!("after '+' operator: {}\n", new_string);
}

fn str_str_const() {
    println!("slice and slice concatenation (both const):");

    // both of these are borrowed values
    // they're also both constants
    let msg1: &str = "hello ";
    let msg2: &str = "world";

    println!("msg1: {}", msg1);
    println!("msg2: {}", msg2);

    // and we can have it so they're not touched
    let msg3 = format!("{msg1}{msg2}");
    println!("result: {}\n", msg3);
}

fn user_input() {
    println!("User input concatenation:");

    // going to concatenate this later
    let mut msg = String::from("hello world");

    println!("string 1: {}", msg);

    println!("enter msg ");

    let mut user_input = String::new();

    std::io::stdin()
        .read_line(&mut user_input)
        .expect("failed to read line");

    println!("user input: {}", user_input);

    msg.push_str(&user_input);
    println!("concatenated strings: {}\n", msg);
}

fn main() {
    string_string();
    string_string_const();
    string_str();
    str_str_const();
    user_input();
}
