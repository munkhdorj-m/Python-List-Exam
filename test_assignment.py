import pytest
import inspect

from assignment import (
    sum_elements,
    find_smallest,
    count_occurrences,
    move_zeroes,
    find_indices,
    mirror_list
)


def uses_loop(func):
    source = inspect.getsource(func)
    return "for" in source or "while" in source


# Exercise 1
@pytest.mark.parametrize("lst, expected", [
    ([8, 12, 5, 10], 35),
    ([1, 1, 1, 1, 1], 5),
    ([0, 0, 0], 0),
])
def test1(lst, expected):
    assert sum_elements(lst) == expected
    assert uses_loop(sum_elements)


# Exercise 2
@pytest.mark.parametrize("lst, expected", [
    ([7, -4, 9, 2], -4),
    ([100, 50, 25], 25),
    ([-1, -5, -2], -5),
])
def test2(lst, expected):
    assert find_smallest(lst) == expected
    assert uses_loop(find_smallest)


# Exercise 3
@pytest.mark.parametrize("lst, target, expected", [
    ([4, 2, 4, 7, 4], 4, 3),
    ([1, 2, 3], 5, 0),
    ([9, 9, 9], 9, 3),
])
def test3(lst, target, expected):
    assert count_occurrences(lst, target) == expected
    assert uses_loop(count_occurrences)


# Exercise 4
@pytest.mark.parametrize("lst, expected", [
    ([0, 4, 0, 2, 9], [4, 2, 9, 0, 0]),
    ([1, 2, 3], [1, 2, 3]),
    ([0, 0, 1], [1, 0, 0]),
])
def test4(lst, expected):
    assert move_zeroes(lst) == expected
    assert uses_loop(move_zeroes)


# Exercise 5
@pytest.mark.parametrize("lst, target, expected", [
    ([5, 1, 5, 3, 5], 5, [0, 2, 4]),
    ([7, 8, 9], 1, []),
    ([2, 2, 2], 2, [0, 1, 2]),
])
def test5(lst, target, expected):
    assert find_indices(lst, target) == expected
    assert uses_loop(find_indices)


# Exercise 6
@pytest.mark.parametrize("lst, expected", [
    ([1, 2, 3], [1, 2, 3, 3, 2, 1]),
    ([5, 8], [5, 8, 8, 5]),
    ([7], [7, 7]),
])
def test6(lst, expected):
    assert mirror_list(lst) == expected
    assert uses_loop(mirror_list)
