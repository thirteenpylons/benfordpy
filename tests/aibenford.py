import csv
from typing import List, Dict
import matplotlib.pyplot as plt

class IntegerOccurrenceAnalyzer:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.data = self.read_csv_data()
        self.occurrences = self.get_first_place_value_occurrences()

    def read_csv_data(self) -> List[int]:
        data = []
        with open(self.file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.extend([int(x) for x in row])
        return data

    def get_first_place_value_occurrences(self) -> Dict[int, int]:
        occurrences = {i: 0 for i in range(1, 10)}
        for num in self.data:
            first_digit = int(str(abs(num))[0])
            if first_digit in occurrences:
                occurrences[first_digit] += 1
        return occurrences

    def plot_occurrences(self) -> None:
        plt.bar(self.occurrences.keys(), self.occurrences.values())
        plt.xlabel("First Place Value")
        plt.ylabel("Occurrences")
        plt.title("Occurrences of Integers 1 through 9 in First Place Value")
        plt.show()

def main() -> None:
    file_path = input("Enter the path to your CSV file: ")
    analyzer = IntegerOccurrenceAnalyzer(file_path)
    print("Occurrences of integers 1 through 9 in the first place value:", analyzer.occurrences)
    analyzer.plot_occurrences()

if __name__ == "__main__":
    main()