"""
Unit tests for module benford

When run as a script, this module invokes several procedures
that test the various functions in the module benford.

Author:     Christian M. Fulton
Date:       23/04/2021
Modified:   29/12/2021
"""
import pytest
import random
import benford
import helpers

pytest.mark.skipif(True, "Not Implemented")
def test_firstNumber():
    """
    Test procedure for firstNumber.
    Extract the first number from list of extracted data and store number of
    occurrences of each number(1 through 9) in dict.
    Verify that dict is zero value when it is and other when not.
    Verify that first number is extracted against dataset.
    Must return dict() type.
    """
    print("Testing firstNumber...")
    nums = [123, 321, 231, 423, 567, 65]
    result = benford.firstNumber(nums)
    assert result == {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 0, 8: 0, 9: 0}
    
    #nums = [random.randrange(1, 10000, 1) for i in range(9)]
    #firstNums = [x for i in nums[:1]]
    #result = benford.firstNumber(nums)
    #print(nums, result)

    # need production test case

@pytest.mark.skipif(True, "Not Implemented")
def test_thisList():
    """
    """
    count = {
        0: 0, # I don't need to count zeros...(temp workaround)
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0
        }

    table = [[1, 11, 18, 30, 41],
            [6, 12, 17, 18, 42],
            [7, 12, 21, 25, 31],
            [11, 16, 32, 37, 39],
            [4, 7, 11, 25, 40],
            [9, 28, 40, 42, 44],
            [6, 17, 22, 27, 34],
            [9, 17, 19, 40, 41],
            [1, 4, 26, 35, 42],
            [11, 15, 35, 39, 40],
            [10, 12, 14, 20, 26]]

    answer = {0: 0, 1: 19, 2: 9, 3: 9, 4: 12, 5: 0, 6: 2, 7: 2, 8: 0, 9: 1}

    result = helpers.thisList(table)
    assert answer == result

test_firstNumber()
print("All tests completed successfully.")