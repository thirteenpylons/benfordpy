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
Modified:   02.Jan.2022
"""
import pytest
from benfordpy import DataUtils


@pytest.fixture(scope="module")
def dataset():
    return DataUtils.Dataset("./testData/test_data_passing.csv")


def test_iterateColumns(dataset):
    """
    """
    pass


def test_extractHeaders(dataset):
    expected_result = [
                        'state',
                        'county',
                        'candidate',
                        'party',
                        'votes',
                        'won',
                        'Unnamed: 6'
                        ]

    assert dataset.extractHeaders() == expected_result, repr(f"Expected {expected_result} and got {dataset}")


def test_countLeading(dataset):
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
    assert dataset.countLeading() == expected_result


def test_extractData(dataset):
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
    assert dataset.extracted_data == expected_result


def test_readCsv(dataset):
    """
    """
    pass