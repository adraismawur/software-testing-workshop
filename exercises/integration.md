# Integration testing guide

Integration tests are much more difficult to write than unit tests.

This is because within a unit test we can examine all the different branches, input values and return values to figure out which things we want to test.
However with integration tests, we combine units which dramatically increases the total number of routes an application can take to perform a certain task.

It is essential that before we start implementing an integration test that we first ask ourselves what we want to test.

## Testing a common combination of units

In our example application, we pretty much always want to read some sort of file from a disk, parse the contents, and do something with those contents.
Limiting ourselves to those tasks, we can design our unit test:

Step 1: load a file from disk with valid data
Step 2: parse the contents of that file into objects
Step 3: return the string representations of these three cities

Our expected input is some valid data, let's say three cities named a, b, c with popuations of 1, 2, 3

Our expected output is three strings:
- `a has a population of 1`
- `b has a population of 2`
- `c has a population of 3`

What we should be able to prove, if the test passes, is that the application can perform the three steps correctly to get to the correct output.

1. Create a new test suite under tests/integration.
Feel free to structure this folder as you see fit.
2. Within this test suite, imitate the `print_population_stats` workflow in `workshop_software_testing/stats/workflows.py`
3. Instead of printing the three lines as is done in the workflow, think of a way to collect these three lines and assert whether they are according to your expectations

Since the integration test is combining several components into one test, it is fair to use multiple assert statements if you need to, or to assert whether something has broken between unit tests.
