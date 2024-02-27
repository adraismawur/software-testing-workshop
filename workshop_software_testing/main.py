import workshop_software_testing.stats.workflows as workshop_workflow


def run(argv):
    """Runs the application

    Args:
        argv (list): A list of command line arguments
    """
    if len(argv) != 3:
        print("Usage: python main.py <filename> <city_name>")
        exit(1)

    filename = argv[1]
    city_name = argv[2]

    print("All cities:")
    workshop_workflow.print_population_stats(filename)
    print()

    print("Sum of the squares of the populations of the nicest places:")
    workshop_workflow.sum_square_of_the_nicest_places(filename)
    print()

    print(f"Population of {city_name}:")
    workshop_workflow.find_and_write_stats(filename, city_name)
