"""EX08 - Data Utils!"""

__author__ = "730402453"

from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_vals(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    #step through table
    for row in table:
        #save every value under key "header"
        result.append(row[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    #loop through keys of one row of table
    first_row: dict[str, str] = table[0]
    for key in first_row:
        #for each key, make a dictionary entry with all column values
        result[key] = column_vals(table, key)
    return result


def head(table: dict[str, list[str]], num: int) -> dict[str, list[str]]:
    """Producing a new column-based table with only the first n row of data."""
    if num > len(table):
        return table
    result: dict[str, list[str]] = {}
    for column in table:
        list1: list[str] = []
        idx: int = 0
        while idx < num:
            list1.append(table[column][idx])
            idx += 1
        result[column] = list1
    return result


def select(table: dict[str, list[str]], column: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for column in column:
        result[column] = table[column]
    return result


def concat(dict_1: dict[str, list[str]], dict_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for key in dict_1:
        result[key] = dict_1[key]
    for key in dict_2:
        if key in result:
            result[key] += dict_2[key]
        else:
            result[key] = dict_2[key] 
    return result


def count(dict_1: list[str]) -> dict[str, int]:
    """This function produces a dictionary where each key is a unique value."""
    result: dict[str, int] = {}
    for key in dict_1:
        if key in result:
            result[key] = result[key] + 1
        else:
            result[key] = 1
    return result