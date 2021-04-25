"""
Unit tests for module benford

When run as a script, this module invokes several procedures
that test the various functions in the module benford.

Author:     Christian M. Fulton
Date:       23/04/2021
Modified:   25/04/2021
"""

import benford
import random


def test_firstNumber():
    """
    Test procedure for firstNumber
    """
    print("Testing firstNumber...")
    nums = [123, 321, 231, 423, 567, 65]
    result = benford.firstNumber(nums)
    assert result == {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 0, 8: 0, 9: 0}
    #nums = [random.randrange(1, 10000, 1) for i in range(9)]
    #firstNums = [x for i in nums[:1]]
    #result = benford.firstNumber(str(nums))
    #print(nums, result)
    print(result)


test_firstNumber()
print("All tests completed successfully.")