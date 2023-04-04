"""EX04 - Utils!"""

__author__ = "730402453"


def all(list: list[int], number: int) -> bool: 
    """Checks to see if given number is equal to the number at each index."""
    idxnum: int = 0
    if len(list) == 0:
        return False
    while idxnum < len(list):
        if list[idxnum] != number:
            return False
        
        else:
            idxnum += 1

    return True


def max(list: list[int]) -> int:
    """Returns the largest number in the given list of integers."""
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")
    max_num: int = list[0]
    idxnum: int = 0    
    while idxnum < len(list):
        if max_num <= list[idxnum]:
            max_num = list[idxnum]
        idxnum += 1
    return max_num


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Given two lists of int values, return True if every element at every index is equal in both lists."""
    if len(list1) != len(list2):
        return False
    idxnum: int = 0
    while idxnum < len(list1):
        if list1[idxnum] != list2[idxnum]:
            return False
        idxnum += 1
    return True