#include <stdio.h>

// 2024-03-26

int binary_search(int *arr, int target, int arr_len) {

  int left_pointer = 0;
  int right_pointer = arr_len - 1;

  int midpoint;

  while (left_pointer <= right_pointer) {
    // this does floor division by default
    midpoint = left_pointer + (right_pointer - left_pointer) / 2;

    if (arr[midpoint] == target) {
      return midpoint;
    } else if (arr[midpoint] < target) {
      left_pointer = midpoint + 1;
    } else {
      right_pointer = midpoint - 1;
    }
  }
  // case not found
  return -1;
}

int main() {

  int nums[] = {5, 4, 3, 2, 1};

  int nums_len = sizeof(nums) / sizeof(nums[0]);

  for (int i = 0; i < 6; i++) {
    printf(
        "the index of %d is %d\n", nums[i],
        // don't need to pass &nums here
        // because binary_search() expects a pointer to the first element of the
        // array which is what is passed here, with just `nums`. no baggage.

        // if `&nums` is passed, binary_search() would receive the address of
        // the entire array,
        // which would lead to incorrect behaviour -> a logic error
        // (colloquially named a runtime error outside of OCR land)

        // theory: you only need to pass the address of the first element
        // because array elements are stored in contiguous space in memory,
        // meaning that the compiler can work out where the rest of the elements
        // are
        binary_search(nums, nums[i], nums_len));
  }

  return 0;
}
