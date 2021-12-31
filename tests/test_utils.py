"""
Unit tests for module benford

When run as a script, this module invokes several procedures
that test the various functions in the module benford.

Author:     Christian M. Fulton
Date:       23/04/2021
Modified:   29/12/2021
"""
import pytest
from benfordpy import utils

def test_extractData():
    """
    Extracting the data

    ExtractData must iterate through columns of dataset and check if the value
    is numerical.

    Must return a list type if numerical values exist; else: return string notice

    This must take a dataset stored in .csv
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
    print("Testing extractData with passing csv dataset...")
    dataset_location = "./testData/test_data_passing.csv"
    raw_data = utils.readCsv(dataset_location)
    result = utils.extractData(raw_data)
    assert type(result) == list, repr(f"Invalid datatype {type(result)}... Must be list.")
    assert result == expected_result, repr(f"Got {result} instead of {expected_result}")

    # I need to use a test csv
    # this will be done outside of the extractData function to ensure flexability
    # first test a dataset that will fail...
    print("Testing extractData with failing csv dataset...")
    dataset_location = "./testData/test_data_failing.csv"
    raw_data = utils.readCsv(dataset_location)
    result = utils.extractData(raw_data)
    assert type(result) == str, repr(f"Invalid datatype {type(result)}... expecting str for failing set.")
    assert result == "Failed to find integer values."

    # test against wrong file type too
    # dataset_location = "./testData/test_wrong_data.json"

    # must return a list
    # else string fail


@pytest.mark.skip("Not implemented")
def test_readCsv():
    """
    Validate csv
    """
    NotImplementedError


print("Testing extractData...")
test_extractData()
print("All tests completed successfully.")