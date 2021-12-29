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


def main():
    """
    not the real main func...
    test helpers here.
    """
    # assign path
    data_path = './testFiles/powerball_usa.csv'
    # extract raw data
    raw_data = read_csv(data_path)
    # clean data into list
    as_list = extractData(raw_data)
    # work with that embedded list.


def extractData(dataset):
    """
    Pass a list through this function

    Identify the depth of the list and break it down.
    """

    result = []
    for data in dataset:
        for d in data[:1]:
            result.append(d)
    return result


def read_csv(filename):
    """
    Returns the contents read from the CSV file filename.
    
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