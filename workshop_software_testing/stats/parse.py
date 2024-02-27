"""Contains code to parse a population data
"""

from workshop_software_testing.classes.city import City


def parse_cities(data):
    """Parses a list of lists into a list of city objects

    list is expected to be in the format:
    [
        ["name", "population"],
        ["name", "population"],
        ...
    ]

    Args:
        data (list): A list of lists containing the population data

    Returns:
        list: A list of city objects
    """
    cities = []

    for row in data:
        name, population = row

        cities.append(City(name, int(population)))

    return cities
