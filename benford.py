"""
Functions for measuring occurrence of integer.

Author: Christian M. Fulton
Date: 23/04/2021
Modified: 25/04/2021
"""
import csv


# store occurrences:
NUMBERS = {
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

def main():
    """
    Run main if not imported
    """
    print("Enter path to dataset including file.")
    print("Example: ./testFiles/election2020/house_state.csv")
    userInput = input("path: ")
    ds = openDataset(userInput)
    firstNumber(ds)



def openDataset(file):
    """
    Used to open the dataset that will be used

    Parameter file: Must be existing csv file with correct path
    Precondition: file is a non-empty string
    """
    with open(file) as f:
        er = csv.reader(f)
        ed = list(er)
        return ed


def firstNumber(dataset):
    """
    Calculates the total occurrences of integers(1:9)
    within the given dataset.

    Parameter dataset: a dataset consisting of numbers
    Precondition: integers and not empty

    """

    for data in dataset:
        if str(data)[:1] == "1":
            NUMBERS[1] = NUMBERS[1] + 1
        elif str(data)[:1] == "2":
            NUMBERS[2] = NUMBERS[2] + 1
        elif str(data)[:1] == "3":
            NUMBERS[3] = NUMBERS[3] + 1
        elif str(data)[:1] == "4":
            NUMBERS[4] = NUMBERS[4] + 1
        elif str(data)[:1] == "5":
            NUMBERS[5] = NUMBERS[5] + 1
        elif str(data)[:1] == "6":
            NUMBERS[6] = NUMBERS[6] + 1
        elif str(data)[:1] == "7":
            NUMBERS[7] = NUMBERS[7] + 1
        elif str(data)[:1] == "8":
            NUMBERS[8] = NUMBERS[8] + 1
        elif str(data)[:1] == "9":
            NUMBERS[9] = NUMBERS[9] + 1
    return NUMBERS

def percent():
    s = sum(NUMBERS)
    for k, v in NUMBERS.items():
        pct = v * 100.0 / s
        print(k, pct)


if __name__ == '__main__':
    main()