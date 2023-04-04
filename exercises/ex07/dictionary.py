"""EX07 - Dictionary Functions!"""

__author__ = "730402453"


def invert(dict_1: dict[str, str]) -> dict[str, str]:
    """Given a dictionary of strings, return the dictionary with inverted keys and values."""
    result: dict[str, str] = {}
    for key in dict_1:
        if dict_1[key] in result:
            raise KeyError("Duplicate key provided in dictionary")
        result[dict_1[key]] = key
    return result


def favorite_color(dict_1: dict[str, str]) -> str:
    """Given a dictionary of strings, return a str with the color that appears the most frequently."""
    result: dict[str, int] = {}
    for key in dict_1:
        color = dict_1[key]
        if color in result:
            result[color] = result[color] + 1
        else:
            result[color] = 1
    max: int = 0
    frequent_color: str = ""
    for color in result:
        if result[color] > max:
            max = result[color]
            frequent_color = color
    return frequent_color


def count(dict_1: list[str]) -> dict[str, int]:
    """This function produces a dictionary where each key is a unique value."""
    result: dict[str, int] = {}
    for key in dict_1:
        if key in result:
            result[key] = result[key] + 1
        else:
            result[key] = 1
    return result