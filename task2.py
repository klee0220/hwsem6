'''
Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
'''
def find_indices(array, minimum, maximum):
    indices = []
    for i in range(len(array)):
        if minimum <= array[i] <= maximum:
            indices.append(i)
    return indices

# Example usage:
array = [1, 5, 3, 7, 9, 2, 4, 6, 8]
minimum = 3
maximum = 7

result = find_indices(array, minimum, maximum)
print("Indices of elements within the specified range:")
print(result)