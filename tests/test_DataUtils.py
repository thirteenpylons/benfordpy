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
    """
    """
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
    """
    """
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
    """
    """
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
    """
    """
    pass


@pytest.fixture(scope="module")
def powerball_dataset():
    return Dataset("./testData/partial_powerball.csv")


def test_iterateColumns(powerball_dataset):
    """
    """
    pass


def test_extractHeaders(powerball_dataset):
    expected_result = [
                        'DrawingNumbers',
                        'Powerball',
                        'Result',
                        'Jackpot',
                        'Weekday',
                        'Date',
                        'Unnamed: 6'
                        ]


    assert powerball_dataset.extractHeaders() == expected_result, repr(f"Expected {expected_result} and got {powerball_dataset}")


def test_countLeading(powerball_dataset):
    """
    """
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
    assert powerball_dataset.countLeading() == expected_result


def test_extractData(powerball_dataset):
    """
    """
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

    assert powerball_dataset.extracted_data == expected_result


def test_readCsv(powerball_dataset):
    """
    """
    pass


def create_dataset_obj(name: str = None) -> Dataset:
    dataset = "test_data_passing.csv" if name is None else name


# Where I left off...
# Trying to extract each column from the dataset and thinking about
# placing each column in dict() or assigning it's on variable.
# dict { header1: {1:0,2:...}, header2:...} 2d dict is looking most likely.
columns = []
count = len(passing_dataset.headers)
for i in range(count):
    columns.append(passing_dataset.extractColumn(i))