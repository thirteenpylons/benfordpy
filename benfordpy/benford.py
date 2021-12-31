"""
Functions for measuring occurrence of integer.

Author: Christian M. Fulton
Date: 23/04/2021
Modified: 19/12/2021
"""
import csv


def main() -> None:
    """
    Run main if not imported
    """
    print("Enter path to dataset including file.")
    print("Example: ./testFiles/election2020/house_state.csv")
    userInput = input("path: ")
    ds = openDataset(userInput)
    firstNumber(ds)


def openDataset(file) -> list:
    """
    Used to open the dataset that will be used

    Parameter file: Must be existing csv file with correct path
    Precondition: file is a non-empty string
    """
    with open(file) as f:
        er = csv.reader(f)
        return list(er)


def firstNumber(dataset) -> dict:
    """
    Calculates the total occurrences of integers(1:9)
    within the given dataset.

    Parameter dataset: a dataset consisting of numbers
    Precondition: integers and not empty

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

    # TODO: Fix this nonsense... counting str value
    # if value is 40 returning 0
    for data in dataset:
        for d in data[1:2]:
            if d.isdigit():
                first = int(d[0])
                count[first] += 1
    return count

# TODO: push numbers through percent
def percent(numbers):
    s = sum(numbers)
    for k, v in numbers.items():
        pct = v * 100.0 / s
        print(k, pct)


if __name__ == '__main__':
    main()