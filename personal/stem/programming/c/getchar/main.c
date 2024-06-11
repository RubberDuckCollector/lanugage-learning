#include <stdio.h>

void get_char() {
  int c;

  c = getchar();

  while (c != EOF) {
    putchar(c);
    c = getchar();
  }
}

void count_num_chars() {
  long num_chars;

  num_chars = 0;

  while (getchar() != EOF) {
    ++num_chars;
    printf("%ld\n", num_chars);
  }
}

int main() {

  /* get_char(); */

  count_num_chars();

  return 0;
}
