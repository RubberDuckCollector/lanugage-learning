import time
from random import randint

"""
GCSE:
this is an abstracted demonstration of insertion sort. in the output the user does not
see precisely what happens when the element "moves down the list".
the user thinks the sorted item
barges into its correct index, shoving all elements on its right up by 1 index.

however in reality, the value moves down by swapping with the adjacent value to the left,
then another comparison is made in an iterative fashion until the value on its left is smaller than it.
therefore resulting in many comparisons...

A LEVEL:
...which is why the average and worst case time complexities are O(n^2),
the algorithm simply makes that many comparisons,
which are significant for big O.

insertion sort sorts in place, meaning that it doesn't use any more or less memory than the input data set
we can safely return the input list, knowing that no new lists need to be initialised
since the algorithm just
meaning the space complexity of insertion sort is O(1)
however the average and worst case time complexity is O(n^2)
and the best case time complexity is O(n)
"""

# colours make the output easier to read
class Color:
    Reset = "\033[0m"
    Red = "\033[031m"
    Green = "\033[32m"
    Yellow = "\033[33m"
    Magenta = "\033[35m"
    Cyan = "\033[96m"


sleep_time = 0.7


# takes list parameter input_list and returns a list
def insertion_sort(input_list: list) -> list:

    print(f"First pass: {input_list[0]} is already reagarded as sorted, no changes")

    # the insertion sort for loop runs len(list)-1 times,
    # because element 1 is regarded already as sorted
    for i in range(1, len(input_list)):
        print(f"list: {Color.Red}{input_list}{Color.Reset}\n")
        time.sleep(sleep_time)

        # consider this value of the list
        current_vaule = input_list[i]
        print(f"current_value: {Color.Yellow}{current_vaule}{Color.Reset} (looking at this value to sort on this pass)")
        time.sleep(sleep_time)
        # sorting smallest to largest so if its already sorted
        if input_list[i-1] < current_vaule:
            print(f"{Color.Yellow}{current_vaule}{Color.Reset} does {Color.Green}NOT{Color.Reset} need to be sorted (it's {Color.Green}bigger{Color.Reset} than the value on its left)\n")
            time.sleep(sleep_time)
            print("no changes to the list.")
            time.sleep(sleep_time)
        # if it's not sorted
        else:
            print(f"{Color.Yellow}{current_vaule}{Color.Reset} {Color.Magenta}DOES{Color.Reset} need to be sorted (it's {Color.Magenta}smaller{Color.Reset} than the value on its left)")
            time.sleep(sleep_time)
            while input_list[i-1] > current_vaule and i > 0:
                print(f"index of {current_vaule}: {i}")
                print(f"i before minus: {i}")
                time.sleep(sleep_time)
                input_list[i] = input_list[i-1]
                i -= 1
                print(f"i after minus: {i}")
                time.sleep(sleep_time)
                print(f"put {current_vaule} at index {i}.")
            input_list[i] = current_vaule
            time.sleep(sleep_time)

    return f"sorted list: {Color.Cyan}{input_list}{Color.Reset}\n"


def main():

    # nums = [1, 2, 3, 4, 5, 6] # best case: already sorted

    nums = [6, 5, 4, 3, 2, 1]  # worst case: reversed

    print(insertion_sort(nums))

    # uncomment the following 2 lines to make a list of random values
    # nums2 = [randint(0, 100) for i in range(15)]
    # print(insertion_sort(nums2))


if __name__ == '__main__':
    main()
