"""Challenge Question - Practice with Dictionaries"""

__author__ = "730402453"

def zip(list1: list[str], list2: list[int]) -> dict[str,int]:
    """Produce a dictionary where the keys are the items of the first list and the values are the corresponding items at the same index of the second list."""
    dict_hello: dict[str, int] = {}
    if len(list1) == 0 or len(list2) == 0:
        return dict()
    if len(list1) != len(list2):
        return dict()

    for idx in range(len(list1)):
        dict_hello[list1[idx]] = list2[idx]
    return dict_hello