def sum_list(numbers: list[int]) -> int:
    sum = 0
    for i in numbers:
        sum += i
    return sum


if __name__ == "__main__":
    print(sum_list([2,5,64,65,24,647,34,577]))
