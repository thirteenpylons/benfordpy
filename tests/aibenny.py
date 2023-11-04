import sys
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict


def load_data(file_path: str) -> pd.DataFrame:
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_path.endswith(".json"):
        with open(file_path, "r") as f:
            data = json.load(f)
        return pd.DataFrame(data)
    else:
        raise ValueError("Invalid file format. Please provide a CSV or JSON file.")


def benfords_law(data: pd.DataFrame, column: str) -> Dict[int, float]:
    first_digits = data[column].apply(lambda x: int(str(abs(x))[0]))
    benford_counts = first_digits.value_counts(normalize=True).sort_index()
    return benford_counts.to_dict()


def plot_benfords_law(benford_counts: Dict[int, float]):
    benford_theoretical = [np.log10(1 + 1 / d) for d in range(1, 10)]

    fig, ax = plt.subplots()
    ax.bar(benford_counts.keys(), benford_counts.values(), label="Observed", alpha=0.7)
    ax.plot(range(1, 10), benford_theoretical, label="Theoretical", marker="o", linestyle="--", color="red")
    ax.legend()

    plt.xlabel("First Digit")
    plt.ylabel("Frequency")
    plt.title("Benford's Law Analysis")

    plt.show()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python benfords_law.py <file_path> <column_name>")
        sys.exit(1)

    file_path = sys.argv[1]
    column_name = sys.argv[2]

    data = load_data(file_path)
    benford_counts = benfords_law(data, column_name)
    plot_benfords_law(benford_counts)
