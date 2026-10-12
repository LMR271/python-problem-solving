def find_max(numbers: list[int]) -> int | None:
    if not numbers:
        return None
    max_so_far = numbers[0]
    for j in numbers[1:]:
        if j > max_so_far:
            max_so_far = j
    return max_so_far
