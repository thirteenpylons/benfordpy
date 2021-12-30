"""
Unit tests for module benford

When run as a script, this module invokes several procedures
that test the various functions in the module benford.

Author:     Christian M. Fulton
Date:       23/04/2021
Modified:   29/12/2021
"""
import pytest
import helpers


def test_extractData():
    """
    Extracting the data

    ExtractData must iterate through columns of dataset and check if the value
    is numerical.

    Must return a list type if numerical values exist; else: return string notice

    This must take a dataset stored in .csv
    """
    # I need to use a test csv
    # this will be done outside of the extractData function to ensure flexability
    # first test a dataset that will fail...
    print("Testing extractData with failing csv dataset...")
    dataset_location = "./testData/test_data_failing.csv"
    raw_data = helpers.read_csv(dataset_location)
    result = helpers.extractData(raw_data)
    assert type(result) == str
    assert result == "Failed to find integer values."

    # test against wrong file type too
    # dataset_location = "./testData/test_wrong_data.json"

    print("Testing extractData with passing csv dataset...")
    dataset_location = "./testData/test_data_passing.csv"
    raw_data = helpers.read_csv(dataset_location)
    result = helpers.extractData(raw_data)

    assert type(result) == list

    # must return a list
    # else string fail


@pytest.mark.skipif(True, "Not implemented")
def test_readCsv():
    """
    Validate csv
    """
    NotImplementedError


print("Testing extractData...")
test_extractData()
print("All tests completed successfully.")