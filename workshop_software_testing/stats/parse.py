"""Contains code to parse a population data
"""


def parse_stats(data):
    """Parses a list of lists into a dictionary

    list is expected to be in the format:
    [
        ["name", "population"],
        ["name", "population"],
        ...
    ]

    Args:
        data (list): A list of lists containing the data to parse

    Returns:
        dict: A dictionary containing the parsed data
    """
    stats = {}
    for row in data:
        name, population = row

        if name in stats:
            raise ValueError(f"Duplicate entry for {name}")

        stats[name] = int(population)

    return stats
