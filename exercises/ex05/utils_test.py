"""EX02 - Utility Functions!"""

__author__ = "730402453"

from exercises.ex05.utils import only_evens, concat, sub


def test_only_evens():
    """Test only evens function with a use case."""
    assert (only_evens([2, 2, 2, 2]) == [2, 2, 2, 2])


def test_only_evens1():
    """Test only evens function with a use case."""
    assert (only_evens([2, 1, 3, 5]) == [2])


def test_only_evens2():
    """Test only evens function with an edge case."""
    assert (only_evens([]) == [])


def test_concat():
    """Test concat function with a use case."""
    assert (concat([2, 2, 2, 2], [4, 6]) == [2, 2, 2, 2, 4, 6])


def test_concat1():
    """Test concat function with a use case."""
    assert (concat([2, 2, 2, 2], [7, 8]) == [2, 2, 2, 2, 7, 8])


def test_concat2():
    """Test concat function with an edge case."""
    assert (concat([2, 2, 2, 2], []) == [2, 2, 2, 2])


def test_sub():
    """Test sub function with an edge case."""
    assert (sub([2, 2, 2, 2], 1, 5) == [2, 2, 2])


def test_sub1():
    """Test sub function with a use case."""
    assert (sub([2, 2, 2, 2], 1, 2) == [2])


def test_sub2():
    """Test sub function with a use case."""
    assert (sub([2, 2, 2, 2], 2, 3) == [2])
