"""
Functions for measuring occurrence of integer.

Author: Christian M. Fulton
Date: 23/04/2021
"""
import csv


def openDataset(file):
    """
    Used to open the dataset that will be used

    Example:

    Parameter file: Must be existing csv file and correct path
    Precondition:
    """
    with open(file) as f:
        er = csv.reader(f)
        ed = list(er)
        return ed


def firstNumber(dataset):
    """
    Calculates the total occurrences of integers(1:9)
    within the given dataset.

    Example:

    Parameter dataset: a set of numbers
    Precondition: must integers and not empty

    """

    numbers = {
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
    for data in dataset:
        if str(data)[:1] == "1":
            numbers[1] = numbers[1] + 1
        elif str(data)[:1] == "2":
            numbers[2] = numbers[2] + 1
        elif str(data)[:1] == "3":
            numbers[3] = numbers[3] + 1
        elif str(data)[:1] == "4":
            numbers[4] = numbers[4] + 1
        elif str(data)[:1] == "5":
            numbers[5] = numbers[5] + 1
        elif str(data)[:1] == "6":
            numbers[6] = numbers[6] + 1
        elif str(data)[:1] == "7":
            numbers[7] = numbers[7] + 1
        elif str(data)[:1] == "8":
            numbers[8] = numbers[8] + 1
        elif str(data)[:1] == "9":
            numbers[9] = numbers[9] + 1
    return numbers