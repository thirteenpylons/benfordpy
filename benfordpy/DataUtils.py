"""

TODO::Just work on extracting the first column and then extend

When iterating determine the data type...
    if data is a list: iterate the lists
    if data is int: iterate through the integers

Author: Christian M. Fulton
Date: 31.Dec.2021
Modified: 03.Jan.2022
"""
import csv
import pandas as pd
from typing import AbstractSet, Any, Iterator, ValuesView


class Dataset:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        
        self.dataset = self.readCsv(self.filename)
        self.panda_data = pd.read_csv(self.filename)
        self.headers = self.extractHeaders()
        #self.extracted_data = self.extractData()
        self.sorted_column = self.sortByColumn()

    
    def __str__(self) -> str:
        return f"{self.dataset}"

    
    def sortByColumn(self) -> list:
        """
        Sort each column into their own row and returns as a list.
        """
        number_of_rows = len(self.dataset)
        number_of_columns = len(self.dataset[0])
        grouped_by_column = []
        for index_of_column in range(number_of_columns):
            new_row_of_n_column = []
            for index_of_row in range(number_of_rows):
                new_row_of_n_column.append(self.dataset[index_of_row][index_of_column])
            grouped_by_column.append(new_row_of_n_column)
        return grouped_by_column


    def extractColumn(self, data: list) -> list:
        """
        Extract the data from self.dataset[0]
        if data is a list iterate the list and combine the lists into one
        if the data is integers, put integers in list

        return list
        """
        return list(data[0])

    
    def removeHeaderReturnColumn(self, data: list) -> list:
        return data[1:] 
        

    def checkForEmbeddedList(self, data: list) -> bool:
        """
        Determine whether the data consists of multi dimensional list

        This may be replaced with just checking to see if type is list...
            After working with lists I'll determine this.
        """
        return type(data[0]) == list
        

    def iterateColumns(self):
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
        NotImplementedError
        header_count = len(self.headers)
        # for the range(header_count):

        datasets = {
                    
        }
        for h in self.headers:
            d = self.panda_data[self.headers].values
        
        # figure out how to return multiple sets
        # maybe have them in nested lists in dict


    def extractHeaders(self) -> list:
        """
        Extract the headers from the dataset

        Parameter dataset: This must be a dataset
        Preconditions: Non empty csv dataset
        """
        df = self.panda_data
        return list(df.columns)


    def countLeading(self) -> dict:
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

        for d in self.extracted_data:
            while (d >= 10):
                d = d // 10
            count[d] += 1

        return count


    def readCsv(self, filename: str) -> list:
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


    # Should this be in a different class?
    def getPercent(numbers: dict) -> dict:
        """
        @param numbers: dict of numbers to compute percentage
        Precondition numbers: must be a dict
        """
        total = sum(numbers.values())
        for key, value in numbers.items():
            percent = value * 100.0 / total
            print(key, percent)
