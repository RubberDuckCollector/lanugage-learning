#include <stdio.h>

void insertion_sort(int *arr, int length) {
  /* passes by reference so no return is needed */
  /* changes array as needed and the array will be modified outside this proc */

  /* this is becuase the program goes to the data at the address in memory of
   * the array, the program DOES NOT make a copy of the array when the function
   * is called */

  /* this is the difference between passing by reference and passing by value */
  /* a negative of passing by reference is that you might not want to mutate the
   * data you pass into a function by reference */

  for (int i = 0; i < length; i++) {
    int current_value = arr[i];
    if (current_value > arr[i - 1]) {
      ;
    } else {
      while (current_value < arr[i - 1] && i > 0) {
        arr[i] = arr[i - 1];
        i = i - 1;
      }
      arr[i] = current_value;
    }
  }
}

int main() {
  int test_array[10] = {9, 5, 3, 7, 2, 8, 4, 1, 6, 0};

  // idk how this works don't @ me
  size_t test_array_len = sizeof(test_array) / sizeof(test_array[0]);

  printf("unsorted:\n");
  for (int i = 0; i < test_array_len; i++) {
    printf("%d ", test_array[i]);
  }

  printf("\nsorted:\n");

  insertion_sort(test_array, test_array_len);

  for (int i = 0; i < test_array_len; i++) {
    printf("%d ", test_array[i]);
  }

  return 0;
}
