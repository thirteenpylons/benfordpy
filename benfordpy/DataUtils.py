"""
Try this as OOP

Using the Dataset class:
    e

Author: Christian M. Fulton
Date: 31.Dec.2021
Modified: 03.Jan.2022
"""
import csv
import pandas as pd


class Dataset:
    def __init__(self, filename):
        self.filename = filename
        
        self.dataset = self.readCsv(self.filename)
        self.panda_data = pd.read_csv(self.filename)
        self.headers = self.extractHeaders()
        self.extracted_data = self.extractData()


    def extractColumn(self, i):
        """
        Will extract columns that contain integer values.

        Parameter i: Index of column to extract.
        Precondition: i must be a non empty integer
        """
        NotImplementedError

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


    def extractData(self) -> list:
        """
        Pass a list through this function

        TODO::FIX THIS

        Identify the depth of the list and break it down.
        """

        result = []
        for data in self.dataset:
            for d in data:
                if d.isdigit():
                    result.append(int(d))
        result = result or "Failed to find integer values."
        return result


    def readCsv(self, filename) -> list:
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
