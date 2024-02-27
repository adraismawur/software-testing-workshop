"""Contains utility functions for the workshop"""


def find_stat(pop_stats, place):
    """Returns the population of a place or None if it is not found

    Args:
        pop_stats (dict): A dictionary containing the population stats
        place (str): The name of the place to look for

    Returns:
        int: The population of the place or None if it is not found
    """

    if not pop_stats:
        raise ValueError("pop_stats cannot be empty")

    if not isinstance(pop_stats, dict):
        raise TypeError("pop_stats must be a dictionary")

    if not place:
        raise ValueError("place cannot be empty")

    if not isinstance(place, str):
        raise TypeError("place must be a string")

    return pop_stats.get(place)
