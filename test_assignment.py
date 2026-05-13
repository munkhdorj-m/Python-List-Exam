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

def test1():
    try:
        assert sum_elements([8, 12, 5, 10]) == 35
        assert sum_elements([1, 1, 1, 1]) == 4
        assert sum_elements([0, 0, 0]) == 0
        assert sum_elements([-1, -2, -3]) == -6

        if not uses_loop(sum_elements):
            pytest.fail("Use loop in sum_elements")

    except:
        pytest.fail("Exercise 1 failed")


# ==================================================
# Exercise 2
# ==================================================

def test2():
    try:
        assert find_smallest([7, -4, 9, 2]) == -4
        assert find_smallest([100, 50, 25]) == 25
        assert find_smallest([-5, -10, -2]) == -10
        assert find_smallest([1]) == 1

        if not uses_loop(find_smallest):
            pytest.fail("Use loop in find_smallest")

    except:
        pytest.fail("Exercise 2 failed")


# ==================================================
# Exercise 3
# ==================================================

def test3():
    try:
        assert count_occurrences([4, 2, 4, 7, 4], 4) == 3
        assert count_occurrences([1, 2, 3], 5) == 0
        assert count_occurrences([9, 9, 9], 9) == 3
        assert count_occurrences([], 1) == 0

        if not uses_loop(count_occurrences):
            pytest.fail("Use loop in count_occurrences")

    except:
        pytest.fail("Exercise 3 failed")


# ==================================================
# Exercise 4
# ==================================================

def test4():
    try:
        assert move_zeroes([0, 4, 0, 2, 9]) == [4, 2, 9, 0, 0]
        assert move_zeroes([1, 2, 3]) == [1, 2, 3]
        assert move_zeroes([0, 0, 1]) == [1, 0, 0]
        assert move_zeroes([0, 0, 0]) == [0, 0, 0]

        if not uses_loop(move_zeroes):
            pytest.fail("Use loop in move_zeroes")

    except:
        pytest.fail("Exercise 4 failed")


# ==================================================
# Exercise 5
# ==================================================

def test5():
    try:
        assert find_indices([5, 1, 5, 3, 5], 5) == [0, 2, 4]
        assert find_indices([7, 8, 9], 1) == []
        assert find_indices([2, 2, 2], 2) == [0, 1, 2]
        assert find_indices([], 1) == []

        if not uses_loop(find_indices):
            pytest.fail("Use loop in find_indices")

    except:
        pytest.fail("Exercise 5 failed")


# ==================================================
# Exercise 6
# ==================================================

def test6():
    try:
        assert mirror_list([1, 2, 3]) == [1, 2, 3, 3, 2, 1]
        assert mirror_list([5, 8]) == [5, 8, 8, 5]
        assert mirror_list([7]) == [7, 7]
        assert mirror_list([]) == []

        if not uses_loop(mirror_list):
            pytest.fail("Use loop in mirror_list")

    except:
        pytest.fail("Exercise 6 failed")
