def linear_search(input_list: list, target: any) -> any:
    for i in range(len(input_list)):
        if input_list[i] == target:
            return i  # return the index of the target


def main():
    nums = [2, 4, 32, 34, 5, 2, 12, 3123, 13, 243, 234]

    print(linear_search(nums, 13))


if __name__ == "__main__":
    main()
