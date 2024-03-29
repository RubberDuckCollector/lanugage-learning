from random import randint


# takes list parameter and return type is list
# denoted after '->'


def bubble_sort(input_list: list) -> list:  # input_list means list

    for i in range(len(input_list) - 1):

        # the inner loop is the one that the swaps are made off of
        # the -1 is there to make sure that the swaps are being made within the index
        # boundaries of the list

        # (if we use the i loop, the algorithm will check
        # the last element with the element after that which is out of bounds)
        # len(input_list) - i - 1 is the most efficient range of the inner loop

        for j in range(len(input_list) - i - 1):
            # if the element being checked is larger than the one after it:
            if input_list[j] > input_list[j + 1]:
                # python shorthand for swapping variables
                input_list[j + 1], input_list[j] = input_list[j], input_list[j + 1]

    return input_list


def bubble_sort_no_shorthand(input_list: list) -> list:
    for i in range(len(input_list) - 1):
        for j in range(len(input_list) - i - 1):
            if input_list[j] > input_list[j + 1]:
                # normal way to swap variables
                temp = input_list[j]
                input_list[j] = input_list[j + 1]
                input_list[j + 1] = temp
                # input_list[j+1], input_list[j] = input_list[j], input_list[j+1]
            print(f"i: {i}")
            print(f"j: {j}")

    return input_list


def main():
    nums = [9, 5, 3, 7, 2, 8, 4, 1, 6, 0]

    nums2 = [randint(0, 100) for i in range(15)]

    print(f"nums = {nums}")

    print(f"sorted nums = {bubble_sort(nums)}")

    print(f"nums2 = {nums2}")

    print(f"sorted nums2 = {bubble_sort(nums2)}")


if __name__ == '__main__':
    main()
