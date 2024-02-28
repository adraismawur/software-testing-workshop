"""Contains the city class"""


class City:
    name = ""
    population = 0

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __str__(self):
        """Returns a string representation of the city object"""
        return f"{self.name} has a population of {self.population}"

    def has_people_in_it(self):
        """Returns True if the city has people in it, False otherwise"""
        return self.population == 0

    def is_nice(self):
        """Returns True if the city is nice, False otherwise"""
        return self.name in ["wageningen", "sneek"]

    @staticmethod
    def find(city_name, cities):
        """Finds a city by name in a list of cities

        Args:
            city_name (str): The name of the city to find
            cities (list): A list of city objects

        Returns:
            city: The city object if found, None otherwise
        """
        for city in cities:
            if city.name == city_name:
                return city
        return None

    @staticmethod
    def to_dict(cities):
        """Converts a list of cities to a dictionary

        Args:
            cities (list): A list of city objects

        Returns:
            dict: A dictionary containing the cities
        """
        city_dict = {}
        for city in cities:
            city_dict[city.name] = city.population
        return city_dict
