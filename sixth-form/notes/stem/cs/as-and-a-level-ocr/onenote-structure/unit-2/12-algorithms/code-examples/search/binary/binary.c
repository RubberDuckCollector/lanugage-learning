#include <stdio.h>

// 2024-03-26

// we pass the array of ints by reference, pass a target int by value, and pass
// the length of our array by value
int binary_search(int *arr, int target, int arr_len) {

  // left_pointer and right_pointer are expected to move
  // save for the case where the first midpoint is the target

  int left_pointer = 0;
  int right_pointer = arr_len - 1;

  int midpoint;

  while (left_pointer <= right_pointer) {
    // this does floor division by default
    // because we are using ints
    // if we use floats here, C will use those decimal places
    midpoint = left_pointer + (right_pointer - left_pointer) / 2;

    // we test for the midpoint first
    // just in case it's the target...
    // ...which lets us achieve the O(1) best case time complexity
    // because only one comparison is made

    if (arr[midpoint] == target) {
      return midpoint;
    } else if (arr[midpoint] < target) {

      // if the value at the midpoint is less than the target...
      // move the left pointer to the midpoint, AND one more to the LEFT
      // this means that we've excluded all of the values that CANNOT be equal
      // to the midpoint

      left_pointer = midpoint + 1;
    } else {

      // if the value at the midpoint is greater than the target...
      // move the left pointer to the midpoint, AND one more to the LEFT
      // this means that we've excluded all of the values that CANNOT be equal
      // to the midpoint

      right_pointer = midpoint - 1;
    }
  }
  // case not found
  return -1;
}

int main() {

  int nums[] = {1, 2, 3, 4, 5};

  int nums_len = sizeof(nums) / sizeof(nums[0]);

  for (int i = 0; i < nums_len; i++) {
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
        // because arrays are stored in contiguous space in memory,
        // meaning that the compiler can work out where the rest of the elements
        // are
        binary_search(nums, nums[i], nums_len));
  }

  return 0;
}
