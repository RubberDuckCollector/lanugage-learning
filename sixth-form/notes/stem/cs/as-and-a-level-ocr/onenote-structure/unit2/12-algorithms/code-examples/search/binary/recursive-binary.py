def recursive_binary_search(input_list, target, right_pointer, left_pointer=0):
    midpoint = left_pointer + (right_pointer - left_pointer) // 2

    if left_pointer <= right_pointer:
        if input_list[midpoint] == target:
            return midpoint
        else:
            if input_list[midpoint] > target:

                # we move the right pointer to the midpoint of the list
                # and then one towards the left
                # because the target can't be in the right half of the list
                # and we've already confirmed it's not the midpoint

                right_pointer = midpoint - 1

                # we continue the function by calling it again
                # with the list, the target, and the right pointer,
                # which we just changed
                # the left pointer stays the same as the default value,
                # we don't have to call the function with it
                # and python handles it for us

                return recursive_binary_search(input_list, target, right_pointer)
            elif input_list[midpoint] < target:

                # we move the left pointer to the midpoint of the list
                # and then one towards the right
                # because the target can't be in the left half of the list
                # and we've already confirmed it's not the midpoint

                left_pointer = midpoint + 1

                # we continue the function by calling it again
                # with the list, the target, the right pointer, and the left pointer, which we just changed
                # the left pointer stays the same as the default value,
                # we have to specify the left pointer this time because otherwise
                # python will use the default value of the left pointer argument which is 0

                return recursive_binary_search(input_list, target, right_pointer, left_pointer)
    else:
        # return -1 if the target wasn't found
        return -1


#       0  1  2   3   4    5    6     7     8     9
nums = [1, 3, 7, 10, 24, 110, 444, 1000, 1111, 5000]

right_pointer = len(nums) - 1
# print(f"{recursive_binary_search(nums, 3, right_pointer)}")

for i in range(len(nums)):
    print(f"{recursive_binary_search(nums, nums[i], right_pointer)}")

print(f"{recursive_binary_search(nums, 12, right_pointer)}")
