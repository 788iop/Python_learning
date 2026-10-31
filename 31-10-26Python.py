def shift_right(numbers):
    result = []
    result.append(numbers[-1])
    result.append(numbers[:-2])
    return result
print(shift_right([1,2,3,4,5]))




def unique_items(numbers):
    total = []
    for I in range(len(numbers)):
        if numbers[I] not in total:
            yield numbers[I]
            total.append(numbers[I])
for num in unique_items([1,2,2,2,3,4,4,5,6]):
    print(num)