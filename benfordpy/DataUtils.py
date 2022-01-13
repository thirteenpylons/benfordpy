"""
Try this as OOP

Author: Christian M. Fulton
Date: 31.Dec.2021
Modified: 03.Jan.2022
"""
import csv
import pandas as pd
from typing import AbstractSet, Iterator, ValuesView


class Dataset:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        
        self.dataset = self.readCsv(self.filename)
        self.panda_data = pd.read_csv(self.filename)
        self.headers = self.extractHeaders()
        self.extracted_data = self.extractData()

    
    def __str__(self) -> str:
        return f"{self.dataset}"


    def checkForEmbeddedList(self, data: list) -> bool:
        """
        Determine whether the data consists of multi dimensional list
        """
        return type(data[0]) == list
        

    def extractColumn(self, column_index: int):
        """
        Will extract columns that contain integer values.

        Parameter column_index: Index of column to extract.
        Precondition: column_index must be a non empty integer
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


    # TODO: calculate percent --Should this be in a different class?
    def getPercent(numbers: dict) -> dict:
        """
        @param numbers: dict of numbers to compute percentage
        Precondition numbers: must be a dict
        """
        total = sum(numbers.values())
        for key, value in numbers.items():
            percent = value * 100.0 / total
            print(key, percent)
            

    def keys(self) -> AbstractSet[BaseTag]:
        """Return the :class:`Dataset` keys to simulate :meth:`dict.keys`.

        Returns
        -------
        dict_keys
            The :class:`~benfordpy.tag.BaseTag` of all the elements in
            the :class:`Dataset`.
        """
        return self._dict.keys()


    def values(self) -> ValuesView[_DatasetValue]:
        """Return the :class:`Dataset` values to simulate :meth:`dict.values`.

        Returns
        -------
        dict_keys
            The :class:`DataElements<benfordpy.dataelem.DataElement>` that make
            up the values of the :class:`Dataset`.
        """
        return self._dict.values()
        

    def __iter__(self) -> Iterator[DataElement]:
        """Iterate through the top-level of the Dataset, yielding DataElements.

        Examples
        --------

        >>> ds = Dataset()
        >>> for elem in ds:
        ...     print(elem)

        The :class:`DataElements<benfordpy.dataelem.DataElement>` are returned in
        increasing tag value order. Sequence items are returned as a single
        :class:`~benfordpy.dataelem.DataElement`, so it is up
        to the calling code to recurse into the Sequence items if desired.

        Yields
        ------
        dataelem.DataElement
            The :class:`Dataset`'s
            :class:`DataElements<benfordpy.dataelem.DataElement>`, sorted by
            increasing tag order.
        """
        # Note this is different than the underlying dict class,
        #        which returns the key of the key:value mapping.
        #   Here the value is returned (but data_element.tag has the key)
        taglist = sorted(self._dict.keys())
        for tag in taglist:
            yield self[tag]
