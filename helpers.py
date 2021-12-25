"""
Helper functions for benfordpy

Author: Christian M. Fulton
Date: 23.Dec.2021
"""
import csv


def thisList(l):
    """
    Pass a list through this function

    Identify the depth of the list and break it down.
    """


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