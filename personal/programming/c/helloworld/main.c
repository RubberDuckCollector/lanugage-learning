#include <stdio.h>

// 2024-03-25

int main() {

  printf("Hello world!\n");

  int age = 300000;

  // this is like rust, although rust smartly inserts the type of your data for
  // you in c you have to do it yourself
  // rust example: print!("i am {} years old unfortunately", age);
  printf("i am %d years old unfortunately", age);

  return 0;
}
