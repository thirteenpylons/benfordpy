"""
Functions for measuring occurrence of leading integers.

Author: Christian M. Fulton
Date: 23/04/2021
Modified: 19/12/2021
"""
import utils

def main() -> None:
    """
    Run main if not imported
    """
    print("Enter path to dataset including file.")
    print("Example: ./testFiles/election2020/house_state.csv")
    userInput = input("path: ")

    raw_data = utils.readCsv(userInput)
    list_data = utils.extractData(raw_data)
    result = utils.countLeading(list_data)
    print(result)



if __name__ == '__main__':
    main()