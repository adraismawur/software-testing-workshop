"""This module contains functions for reading and writing CSV files"""

from pathlib import Path


def read_csv(filename):
    """Reads a CSV file and returns the contents as a list of lists

    Args:
        filename (str): The name of the file to read from

    Returns:
        list: A list of lists containing the contents of the CSV file
    """
    if not filename:
        raise ValueError("filename cannot be empty")

    if not isinstance(filename, str):
        raise TypeError("filename must be a string")

    file_path = Path(filename)

    if not file_path.exists():
        raise FileNotFoundError(f"File '{filename}' not found")

    lines = []

    with open(file_path, "r") as file:
        for line in file:
            lines.append(line.strip().split(","))

    return lines


def write_population_stats(filename, cities):
    """Writes the population stats to a file

    Args:
        filename (str): The name of the file to write to
        cities (list): A list of city objects
    """
    if not filename:
        raise ValueError("filename cannot be empty")

    if not isinstance(filename, str):
        raise TypeError("filename must be a string")

    if not cities:
        raise ValueError("cities cannot be empty")

    if not isinstance(cities, list):
        raise TypeError("cities must be a list")

    file_path = Path(filename)

    with open(file_path, "w") as file:
        for city in cities:
            file.write(f"{city.name},{city.population}\n")
