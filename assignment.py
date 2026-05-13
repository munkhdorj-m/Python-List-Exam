# Exercise 1
 def sum_elements(lst):
    total = 0
    for num in lst:
        total += num
    return total


# Exercise 2

def find_smallest(lst):
    smallest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
    return smallest


# Exercise 3
def count_occurrences(lst, target):
    count = 0
    for num in lst:
        if num == target:
            count += 1
    return count


# Exercise 4
def move_zeroes(lst):
    result = []

    for num in lst:
        if num != 0:
            result.append(num)

    zero_count = len(lst) - len(result)

    for _ in range(zero_count):
        result.append(0)

    return result


# Exercise 5
def find_indices(lst, target):
    indices = []

    for i in range(len(lst)):
        if lst[i] == target:
            indices.append(i)

    return indices


# Exercise 6
def mirror_list(lst):
    result = []

    for num in lst:
        result.append(num)

    for i in range(len(lst) - 1, -1, -1):
        result.append(lst[i])

    return result
