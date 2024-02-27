"""Contains the reading, parsing and writing workflow of this application
"""

from workshop_software_testing.io.csv import read_csv, write_population_stats
from workshop_software_testing.stats.parse import parse_cities
from workshop_software_testing.math.sum_squares import sum_squares

from workshop_software_testing.classes.city import City


def print_population_stats(filename):
    """Prints the population stats of a city

    Args:
        filename (str): The name of the file to read from
    """
    data = read_csv(filename)
    cities = parse_cities(data)

    for city in cities:
        print(city)


def find_and_write_stats(filename, city):
    """Finds the population stats of a city and writes the stats to a file

    Args:
        filename (str): The name of the file to read from
        city (str): The name of the city to find the population stats of
    """
    data = read_csv(filename)
    cities = parse_cities(data)

    city = City.find(city, cities)

    if city is None:
        print(f"Population of {city} is unknown")
        return

    print(city)

    write_population_stats("output.txt", cities)


def sum_square_of_the_nicest_places(filename):
    """Finds the population stats of the nicest cities and returns the sum of
    the squares of their populations

    Args:
        filename (str): The name of the file to read from

    Returns:
        int: The sum of the squares of the populations of the nicest cities
    """
    data = read_csv(filename)
    stats = parse_cities(data)

    nice_place_a = "wageningen"
    nice_place_b = "sneek"

    place_a = City.find(nice_place_a, stats)
    place_b = City.find(nice_place_b, stats)

    if place_a is None:
        print(f"Population of {nice_place_a} is unknown")
        exit()

    if place_b is None:
        print(f"Population of {nice_place_b} is unknown")
        exit()

    cool_number = sum_squares(place_a.population, place_b.population)
    print(f"Sum squares of {place_a.name} and {place_b.name} is {cool_number}")
