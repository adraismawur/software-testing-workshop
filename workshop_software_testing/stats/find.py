"""Contains utility functions for the workshop"""


def find_stat(pop_stats, city):
    """Returns the population of a city or None if it is not found

    Args:
        pop_stats (dict): A dictionary containing the population stats
        city (str): The name of the city to look for

    Returns:
        int: The population of the city or None if it is not found
    """

    if not pop_stats:
        raise ValueError("pop_stats cannot be empty")

    if not isinstance(pop_stats, dict):
        raise TypeError("pop_stats must be a dictionary")

    if not city:
        raise ValueError("city cannot be empty")

    if not isinstance(city, str):
        raise TypeError("city must be a string")

    return pop_stats.get(city)
