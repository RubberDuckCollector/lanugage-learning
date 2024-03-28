"""
left_pointer may have to change during the function, but its default is 0 because indexes start at 0
we call left pointer last because it's a default argument, so it's implicitly passed if we don't pass it.
python will pass it for us
i learnt about it from playing around with them and here:
https://www.geeksforgeeks.org/default-arguments-in-python/
it's a handy technique. i honestly don't know how to implement recursive binary search without it.
i figured it out by myself this way
"""


def recursive_binary_search(input_list: list, target: any, right_pointer: int, left_pointer=0):
    """
    two pointers dictate the searchable part of the list.
    left pointer begins at the first index of the list
    right pointer begins at the last index of the list

    GCSE:
    the precondition of binary search is that the list HAS TO be sorted beforehand
    for it to execute without any logic errors
    otherwise, the target element may be discarded even though
    it may be present in the list

    e.g: my_list = [2, 3, 4, 5, 1]
    if the target is 1, it would get erroneously invalidated by binary search
    because it would check 4 first as the first midpoint
    and since 4 is larger than 1,
    binary search would move the right pointer to 3, and would ultimately not return 1, the target.


    BOTH POINTERS ARE EXPECTED TO MOVE,
    WITH THE EXCEPTION OF THE TARGET BEING AT THE FIRST MIDPOINT...

    A LEVEL:
    ...which is why sorting algorithms' best case time complexity is O(1).
    in other words,

    "what if the first value we check is the target?"
    - the average and worst case time complexities of this is O(log n)
    - you can see how the time complexity is O(log n),
    - as we halve the list every time the algorithm doesn't find the target.
    """

    midpoint = left_pointer + (right_pointer - left_pointer) // 2

    if left_pointer <= right_pointer:
        if input_list[midpoint] == target:
            return midpoint
        else:
            if input_list[midpoint] > target:

                # we bring the right pointer to the midpoint
                # and then towards the centre once more.
                # because we've already checked the midpoint
                # this results in the searchable part of the list being
                # half the size minus 1.
                right_pointer = midpoint - 1

                # we continue the binary search
                # by returning it with the input list again, the target,
                # and the right pointer that we just changed.

                # python can fill in left_pointer as 0 again,
                # as we haven't had to change the left_pointer.
                return recursive_binary_search(input_list, target, right_pointer)

            elif input_list[midpoint] < target:

                # we bring the left pointer to the midpoint
                # and then towards the centre once more.
                # because we've already checked the midpoint
                # this results in the searchable part of the list being
                # half the size minus 1.
                left_pointer = midpoint + 1

                # we continue the binary search
                # by calling it again with the list again, the target
                # the right pointer (which we haven't changed)
                # and the left pointer, which we just changed.

                return recursive_binary_search(input_list, target, right_pointer, left_pointer)
    else:
        return -1  # return -1 if item hasn't been found


def main():

    #       0  1  2   3   4    5    6     7     8     9
    nums = [1, 3, 7, 10, 24, 110, 444, 1000, 1111, 5000]

    # we want the index of the right pointer's start, not the length of the list
    right_pointer = len(nums) - 1

    # print(f"{recursive_binary_search(nums, 3, right_pointer)}")

    for i in range(len(nums)):
        print(f"{recursive_binary_search(nums, nums[i], right_pointer)}")

    print(f"{recursive_binary_search(nums, 12, right_pointer)}")


if __name__ == "__main__":
    main()
