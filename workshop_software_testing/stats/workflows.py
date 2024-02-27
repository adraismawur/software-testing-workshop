"""Contains the reading, parsing and writing workflow of this application
"""

from workshop_software_testing.io.csv import read_csv, write_population_stats
from workshop_software_testing.stats.parse import parse_stats
from workshop_software_testing.math.sum_squares import sum_squares


def find_and_write_stats(filename, place):
    """Finds the population stats of a place and writes the stats to a file

    Args:
        filename (str): The name of the file to read from
        place (str): The name of the place to find the population stats of
    """
    data = read_csv(filename)
    stats = parse_stats(data)

    pop = stats.get(place)

    if pop is None:
        print(f"Population of {place} is unknown")
        return

    print(f"Population of {place} is {pop}")

    write_population_stats("output.txt", stats)


def sum_square_of_the_nicest_places(filename):
    """Finds the population stats of the nicest places and returns the sum of
    the squares of their populations

    Args:
        filename (str): The name of the file to read from

    Returns:
        int: The sum of the squares of the populations of the nicest places
    """
    data = read_csv(filename)
    stats = parse_stats(data)

    nice_place_a = "wageningen"
    nice_place_b = "sneek"

    pop_a = stats.get(nice_place_a)
    pop_b = stats.get(nice_place_b)

    if pop_a is None:
        print(f"Population of {nice_place_a} is unknown")
        exit()

    if pop_b is None:
        print(f"Population of {nice_place_b} is unknown")
        exit()

    cool_number = sum_squares(pop_a, pop_b)
    print(f"Sum of squares of {pop_a} and {pop_b} is {cool_number}")
