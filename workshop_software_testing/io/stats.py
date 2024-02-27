"""Contains code to deal with input of data
"""

from pathlib import Path


def read_population_stats(filename):
    """Reads the population stats from a file

    Args:
        filename (str): The name of the file to read from

    Returns:
        dict: A dictionary containing the population stats
    """
    if not filename:
        raise ValueError("filename cannot be empty")

    if not isinstance(filename, str):
        raise TypeError("filename must be a string")

    file_path = Path(filename)

    if not file_path.exists():
        raise FileNotFoundError(f"File '{filename}' not found")

    stats = {}
    with open(file_path, "r") as file:
        for line in file:
            name, population = line.strip().split(",")

            if name in stats:
                raise ValueError(f"Duplicate entry for {name}")

            stats[name] = int(population)

    return stats


def write_population_stats(filename, stats):
    """Writes the population stats to a file

    Args:
        filename (str): The name of the file to write to
        stats (dict): A dictionary containing the population stats
    """
    if not filename:
        raise ValueError("filename cannot be empty")

    if not isinstance(filename, str):
        raise TypeError("filename must be a string")

    if not stats:
        raise ValueError("stats cannot be empty")

    if not isinstance(stats, dict):
        raise TypeError("stats must be a dictionary")

    file_path = Path(filename)

    with open(file_path, "w") as file:
        for name, population in stats.items():
            file.write(f"{name},{population}\n")
