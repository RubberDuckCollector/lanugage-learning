#include <stdio.h>

void bubble_sort(int *arr, int arr_length) {
  for (int i = 0; i < arr_length - 1; i++) {
    for (int j = 0; j < arr_length - i - 1; j++) {
      if (arr[j] < arr[j + 1]) {
        // do nothing
      } else {
        int temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
}

int main() {
  int nums[10] = {9, 5, 3, 7, 2, 8, 4, 1, 6, 0};

  size_t nums_size = sizeof(nums) / sizeof(nums[0]);

  printf("unsorted:\n");
  for (int i = 0; i < nums_size; i++) {
    printf("%d ", nums[i]);
  }

  bubble_sort(nums, nums_size);

  printf("sorted:\n");
  for (int i = 0; i < nums_size; i++) {
    printf("%d ", nums[i]);
  }

  return 0;
}
