"""EX07 - Where Functions from Dictionary File are Tested!"""

__author__ = "730402453"

from dictionary import invert
from dictionary import favorite_color
from dictionary import count


def test_favorite_color_multiple() -> None:
    """This function tests the favorite color function with mulitple names and colors inputed."""
    test: dict[str, str] = {"Sholeh": "yellow", "John": "red", "Merida": "yellow", "Harry": "yellow", "Ian": "purple"}
    assert favorite_color(test) == "yellow"


def test_favorite_color_single_name() -> None:
    """This function tests the favorite_color function when there is only one name and color."""
    test: dict[str, str] = {"Sholeh": "Purple"}
    assert favorite_color(test) == "Purple"


def test_favorite_color_tied() -> None:
    """This function tests the favorite color function when two colors have the same amout of counts as each other."""
    test: dict[str, str] = {"Sholeh": "yellow", "Lila": "yellow", "Harry": "purple", "Ian": "purple"}
    assert favorite_color(test) == "yellow"


def test_favorite_color_empty_dict() -> None:
    """This function tests the favorite color function when there is an empty dictionary."""
    test: dict[str, str] = {}
    assert favorite_color(test) == ""


def test_count_single() -> None:
    """This function tests the count function when it has to count a single item."""
    test: list[str] = ["yellow"]
    for key in count(test):
        assert count(test)[key] == 1


def test_count_multiple() -> None:
    """This function tests the count function when it has to count multiple items."""
    test: list[str] = ["red", "orange", "yellow"]
    for key in count(test):
        assert count(test)[key] == 1


def test_invert_single() -> None:
    """This function tests the invert function when it has one key and value."""
    test: dict[str, str] = {"purple": "orange"}
    test2: dict[str, str] = {"orange": "purple"}
    assert invert(test) == test2


def test_invert_multiple() -> None:
    """This function tests the invert function when it has to invert a dictionary that contains multiple keys and corresponding values."""
    test: dict[str, str] = {'purple': 'black', 'green': 'white', 'red': 'yellow'}
    test2: dict[str, str] = {'black': 'purple', 'white': 'green', 'yellow': 'red'}
    assert invert(test) == test2


def test_count_multiple_repeat() -> None:
    """This function tests the count function when it has to count multiple items."""
    test: list[str] = ["yellow", "red", "yellow", "purple", "yellow", "yellow"]
    assert (count(test)) == {"yellow": 4, "purple": 1, "red": 1}


def test_invert_empty() -> None:
    """This function tests the invert function when it has to invert an empty dictionary."""
    test: dict[str, str] = {}
    assert len(invert(test)) == 0


def test_count_empty_list() -> None:
    """This function tests the count function when it has an empty list."""
    test: list[str] = []
    assert (count(test)) == {}
