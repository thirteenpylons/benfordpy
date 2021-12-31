"""
Helper functions for benfordpy

What I need to do...
Figure out how the data is typically stored. {
    working with .csv;
    at times data starts in second column and in first column other times.
    maybe I can iterate through each column and analyze the data to see if it is
    numerical. If it is I can create a variable to store the dict of counted occurences.

    This could create a variable for each column.

    maybe further I could analyze the data that has been extracted and counted
    pushing it through to take the percentages of each dict() and if the dict()
    is within a percentile of following benfords law I can return the values/graph.
    If not I can return that the data did not follow benfords law.
}
-Come up with global way of extracting the data(or more than one)
    and store that data in a list()

Push the extracted data into a function that will slice the list if it isdigit
return a dict() of counts for first digit occurences

Author: Christian M. Fulton
Date: 23.Dec.2021
Modified: 28.Dec.2021
"""
import csv
import pandas as pd


def iterateColumns(headers, dataset):
    """
    Iterate through the columns using the headers extracted

    # expect this::
    result = {
            "header_name": {
                            1: 50,
                            2...,
                            }
            "other_header":...
            }

    Parameter headers: Must be non empty list of headers in dataset
    Preconditions:

    Parameter dataset: Must be valid csv dataset
    Preconditions:
    """
    header_count = len(headers)
    # for the range(header_count):

    datasets = {
                
    }
    for h in headers:
        d = pd.read_csv(dataset)[headers].values
    
    # figure out how to return multiple sets
    # maybe have them in nested lists in dict



def extractHeaders(dataset) -> list:
    """
    Extract the headers from the dataset

    Parameter dataset: This must be a dataset
    Preconditions: Non empty csv dataset
    """
    df = pd.read_csv(dataset)
    return list(df.columns)


def countLeading(dataset) -> dict:
    """
    Take the dataset and slice the leading digit and count the 
    occurrences and return as a dict
    """
    count = {
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

    for d in dataset:
        while (d >= 10):
            d = d // 10
        count[d] += 1

    return count


def extractData(dataset) -> list:
    """
    Pass a list through this function

    Identify the depth of the list and break it down.
    """

    result = []
    for data in dataset:
        for d in data:
            if d.isdigit():
                result.append(int(d))
    result = result or "Failed to find integer values."
    return result


def readCsv(filename) -> list:
    """
    Returns the contents read from the CSV file filename as list.
    
    This function reads the contents of the file filename and returns the contents as
    a 2-dimensional list. Each element of the list is a row, with the first row being
    the header. Cells in each row are all interpreted as strings; it is up to the 
    programmer to interpret this data, since CSV files contain no type information.
    
    Parameter filename: The file to read
    Precondition: filename is a string, referring to a file that exists, and that file 
    is a valid CSV file
    """
    with open(filename) as f:
        wrap = csv.reader(f)
        data = list(wrap)
    return data


# TODO: calculate percent
def percent(numbers):
    s = sum(numbers)
    for k, v in numbers.items():
        pct = v * 100.0 / s
        print(k, pct)


class Counts:
    """
    Return dict per obj
    """
    def __init__(self):
        NotImplementedError