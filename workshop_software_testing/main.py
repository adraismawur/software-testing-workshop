import workshop_software_testing.io.stats as stats

from workshop_software_testing.math.sum_squares import sum_squares


def run(argv):
    if len(argv) != 4:
        print("Usage: python main.py <filename> <place> <output>")
        exit(1)

    filename = argv[1]
    place = argv[2]
    output = argv[3]

    pop_stats = stats.read_population_stats(filename)

    interesting_place_a = "wageningen"
    interesting_place_b = "sneek"

    pop_a = pop_stats.get(interesting_place_a)
    pop_b = pop_stats.get(interesting_place_b)

    if pop_a is None:
        print(f"Population of {interesting_place_a} is unknown")
        exit()

    if pop_b is None:
        print(f"Population of {interesting_place_b} is unknown")
        exit()

    cool_number = sum_squares(pop_a, pop_b)
    print(f"Sum of squares of {pop_a} and {pop_b} is {cool_number}")

    find_pop = pop_stats.get(place)

    if find_pop is None:
        print(f"Population of {place} is unknown")
        exit()

    print(f"Population of {place} is {find_pop}")

    stats.write_population_stats(output, pop_stats)
