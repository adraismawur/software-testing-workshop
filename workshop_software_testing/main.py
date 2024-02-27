import workshop_software_testing.stats.workflows as workshop_workflow


def run(argv):
    if len(argv) != 3:
        print("Usage: python main.py <filename> <place>")
        exit(1)

    filename = argv[1]
    place = argv[2]

    workshop_workflow.sum_square_of_the_nicest_places(filename)

    workshop_workflow.find_and_write_stats(filename, place)
