"""
Unit tests for module DataUtils

When run as a script, this module invokes several procedures
that test the various functions in the module benford.

TODO: 
    Test for integers in multiple columns(These should be treated as an instance)
        (possible refactoring just for that)
    Working with 2d lists.
    for len(dataset) to determine how many instantiations

Author:     Christian M. Fulton
Date:       02.Jan.2022
Modified:   03.Jan.2022
"""
import pytest
from benfordpy.DataUtils import Dataset


@pytest.fixture(scope="module")
def passing_dataset():
    return Dataset("./testData/test_data_passing.csv")


def test_iterateColumns(passing_dataset):
    pass


def test_extractHeaders(passing_dataset):
    expected_result = [
                        'state',
                        'county',
                        'candidate',
                        'party',
                        'votes',
                        'won',
                        'Unnamed: 6'
                        ]

    assert passing_dataset.extractHeaders() == expected_result, repr(f"Expected {expected_result} and got {passing_dataset}")


def test_countLeading(passing_dataset):
    expected_result = {
                        1: 3,
                        2: 1,
                        3: 2,
                        4: 1,
                        5: 1,
                        6: 2,
                        7: 0,
                        8: 1,
                        9: 1
                        }
    assert passing_dataset.countLeading() == expected_result


def test_extractData(passing_dataset):
    expected_result = [
                        44352,
                        39332,
                        1115,
                        616,
                        191678,
                        82545,
                        3785,
                        2031,
                        9,
                        53,
                        1250,
                        623
                        ]
    assert passing_dataset.extracted_data == expected_result


def test_readCsv(passing_dataset):
    pass


@pytest.fixture(scope="module")
def partial_powerball_dataset():
    return Dataset("./testData/partial_powerball.csv")


def test_iterateColumns(partial_powerball_dataset):
    pass


def test_extractHeaders(partial_powerball_dataset):
    expected_result = [
                        'DrawingNumbers',
                        'Powerball',
                        'Result',
                        'Jackpot',
                        'Weekday',
                        'Date',
                        'Unnamed: 6'
                        ]


    assert partial_powerball_dataset.extractHeaders() == expected_result, repr(f"Expected {expected_result} and got {partial_powerball_dataset}")


def test_countLeading(partial_powerball_dataset):
    expected_result = {
                        1: 3,
                        2: 1,
                        3: 2,
                        4: 1,
                        5: 1,
                        6: 2,
                        7: 0,
                        8: 1,
                        9: 1
                        }
    assert partial_powerball_dataset.countLeading() == expected_result


def test_extractData(partial_powerball_dataset):
    expected_result = [
                        44352,
                        39332,
                        1115,
                        616,
                        191678,
                        82545,
                        3785,
                        2031,
                        9,
                        53,
                        1250,
                        623
                        ]

    assert partial_powerball_dataset.extracted_data == expected_result


def test_readCsv(partial_powerball_dataset):
    pass


def create_dataset_obj(name: str = None) -> Dataset:
    dataset = "test_data_passing.csv" if name is None else name


def test_sortByColumn(partial_powerball_dataset):
    expected_result = [
                        1, 11, 18, 30, 41, 6, 12, 17, 18, 42, 7, 12, 21, 25, 31,
                        11, 16, 32, 37, 39, 4, 7, 11, 25, 40, 9, 28, 40, 42, 44,
                        6, 17, 22, 27, 34, 9, 17, 19, 40, 41, 1, 4, 26, 35, 42,
                        ]
    result = partial_powerball_dataset.sorted_column[0]
    assert expected_result == result
