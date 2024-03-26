#include <stdio.h>

// pass the array by reference to the function
int linear_search(int *arr, int target) {

  // dereference the pointer when working out the size to look at the array at
  // the corresponding location in memory
  int arr_len = sizeof(&arr) / sizeof(&arr[0]);

  for (int i = 0; i < arr_len; i++) {
    if (arr[i] == target) {
      return i;
    }
  }
  return -1;
}

int main() {
  int target = 5;

  int nums[] = {5, 4, 3, 2, 1};

  /* int result = linear_search(nums, target); */

  printf("index of %d is %d", target, linear_search(nums, target));
}
