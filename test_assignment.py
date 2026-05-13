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


# ==================================================
# Exercise 1
# ==================================================

@pytest.mark.parametrize("lst, expected", [
    ([1, 2, 3], 6),
    ([5, 5], 10),
])
def test1_basic(lst, expected):
    assert sum_elements(lst) == expected


@pytest.mark.parametrize("lst, expected", [
    ([0, 0, 0], 0),
    ([-1, -2, -3], -6),
])
def test1_edge(lst, expected):
    assert sum_elements(lst) == expected
    assert uses_loop(sum_elements)


# ==================================================
# Exercise 2
# ==================================================

@pytest.mark.parametrize("lst, expected", [
    ([4, 2, 9], 2),
    ([7, -1, 5], -1),
])
def test2_basic(lst, expected):
    assert find_smallest(lst) == expected


@pytest.mark.parametrize("lst, expected", [
    ([1], 1),
    ([-5, -10, -2], -10),
])
def test2_edge(lst, expected):
    assert find_smallest(lst) == expected
    assert uses_loop(find_smallest)


# ==================================================
# Exercise 3
# ==================================================

@pytest.mark.parametrize("lst, target, expected", [
    ([1, 2, 1], 1, 2),
    ([5, 5, 5], 5, 3),
])
def test3_basic(lst, target, expected):
    assert count_occurrences(lst, target) == expected


@pytest.mark.parametrize("lst, target, expected", [
    ([1, 2, 3], 7, 0),
    ([], 1, 0),
])
def test3_edge(lst, target, expected):
    assert count_occurrences(lst, target) == expected
    assert uses_loop(count_occurrences)


# ==================================================
# Exercise 4
# ==================================================

@pytest.mark.parametrize("lst, expected", [
    ([0, 1, 0, 2], [1, 2, 0, 0]),
    ([1, 2, 3], [1, 2, 3]),
])
def test4_basic(lst, expected):
    assert move_zeroes(lst) == expected


@pytest.mark.parametrize("lst, expected", [
    ([0, 0, 0], [0, 0, 0]),
    ([5], [5]),
])
def test4_edge(lst, expected):
    assert move_zeroes(lst) == expected
    assert uses_loop(move_zeroes)


# ==================================================
# Exercise 5
# ==================================================

@pytest.mark.parametrize("lst, target, expected", [
    ([5, 1, 5], 5, [0, 2]),
    ([1, 2, 3], 2, [1]),
])
def test5_basic(lst, target, expected):
    assert find_indices(lst, target) == expected


@pytest.mark.parametrize("lst, target, expected", [
    ([1, 2, 3], 7, []),
    ([], 1, []),
])
def test5_edge(lst, target, expected):
    assert find_indices(lst, target) == expected
    assert uses_loop(find_indices)


# ==================================================
# Exercise 6
# ==================================================

@pytest.mark.parametrize("lst, expected", [
    ([1, 2], [1, 2, 2, 1]),
    ([5], [5, 5]),
])
def test6_basic(lst, expected):
    assert mirror_list(lst) == expected


@pytest.mark.parametrize("lst, expected", [
    ([], []),
    ([1, 2, 3], [1, 2, 3, 3, 2, 1]),
])
def test6_edge(lst, expected):
    assert mirror_list(lst) == expected
    assert uses_loop(mirror_list)
