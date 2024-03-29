"""
two pointers dictate the searchable part of the list.
left pointer begins at the first index of the list
right pointer begins at the last index of the list.
"""

def binary_search(input_list, target):
    """
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

    "what if the first value we check is the target?" - only one comparison would be made.
    - the average and worst case time complexities of this is O(log n)
    - you can see how the time complexity is O(log n),
    - as we halve the list every time the algorithm doesn't find the target.
    """

    left_pointer = 0

    # we want the last index, not the index + 1 or the length
    right_pointer = len(input_list) - 1

    while left_pointer <= right_pointer:
        midpoint = left_pointer + (right_pointer - left_pointer) // 2
        if input_list[midpoint] == target:
            return midpoint
        # change the searchable section of the list
        elif input_list[midpoint] > target:

            # we bring the right pointer to the midpoint
            # and then towards the centre once more.
            # because we've already checked the midpoint
            # this results in the searchable part of the list being
            # half the size minus 1.

            right_pointer = midpoint - 1
        else:

            # we bring the left pointer to the midpoint
            # and then towards the centre once more.
            # because we've already checked the midpoint
            # this results in the searchable part of the list being
            # half the size minus 1.

            left_pointer = midpoint + 1

    return -1


def main():
    nums = [1, 2, 3, 38, 48, 51, 53, 61, 62, 65, 72, 73, 83, 83, 93]
    #       0  1  2  3   4   5   6   7   8   9   10  11  12  13  14

    for i in range(len(nums)):
        print(binary_search(nums, nums[i]))

    # works on characters and strings as well as numbers
    # this is because characters have a corresponding ASCII value
    # they're sorted by ASCII value, in ascending order

    letters = ["a", "b", "c", "d", "e"]
    print(binary_search(letters, "b"))


if __name__ == "__main__":
    main()
