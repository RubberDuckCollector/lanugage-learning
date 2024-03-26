#include <stdio.h>

long fib_rec(int n) {
  if (n < 2) {
    return n;
  } else {
    return fib_rec(n - 1) + fib_rec(n - 2);
  }
}

long fib_it(int n) {
  long a = 0;
  long b = 1;
  long c = 0;

  // if the function receives a value lower than 0 it can't really compute the
  // nth term of the fibonacci sequence with it
  if (n < 0) {
    return -1;
  } else if (n == 0) {
    return a;
  } else if (n == 1) {
    return b;
  } else {
    for (int i = 2; i < n + 1; i++) {
      c = a + b;
      a = b;
      b = c;
    }
    return b;
  }
}

int main() {

  int arg = 10;
  long result = fib_rec(arg);

  // here we use %ld to denote that we are formatting a long in printf(), not
  // just an int
  // i used a long to store the answer because it has a larger range than int
  printf("fib_rec(%d) is %ld\n", arg, result);

  arg = 20;
  result = fib_rec(arg);
  printf("fib_rec(%d) is %ld\n", arg, result);

  arg = 40;
  result = fib_rec(arg);
  printf("fib_rec(%d) is %ld\n", arg, result);

  arg = 20;
  result = fib_it(arg);
  printf("fib_it(%d) is %ld\n", arg, result);

  return 0;
}
