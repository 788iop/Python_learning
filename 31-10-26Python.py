def shift_right(numbers):
    result = []
    result.append(numbers[-1])
    result.append(numbers[:-2])
    return result
print(shift_right([1,2,3,4,5]))