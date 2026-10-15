def filter_evens(numbers: list[int]) -> list[int]:
    result = []
    if numbers == []:
        return []
    else:
        for i in numbers:
            if i % 2 == 0:
                result.append(i)
    return result
