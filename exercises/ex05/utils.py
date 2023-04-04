"""EX02 - Utility Functions!"""

__author__ = "730402453"


def only_evens(list1: list[int]) -> list[int]:
    """Given a list of ints, will return elements in list that are even."""
    list2: list[int] = list()
    for elem in list1:
        if elem % 2 == 0:
            list2.append(elem)
    return list2


def concat(list1: list[int], list2: list[int]) -> int:
    """Given two lists of ints, returns new list that contains all of the elements of the first list followed by all of the elements of the second list."""
    list3: list[int] = list()
    for elem in list1:
        list3.append(elem)
    for elem in list2:
        list3.append(elem)
    return list3


def sub(list1: list[int], start: int, end: int) -> list[int]:
    """Given a list of ints, a start index, and an end index(not inclusive), generates a list that is a subset of the given list."""
    newlist: list[int] = list()
    if len(list1) == 0:
        return newlist

    if start < 0:
        start = 0

    if len(list1) < end:
        end = len(list1)
    
    while start < end:
        newlist.append(list1[start])
        start += 1

    return newlist