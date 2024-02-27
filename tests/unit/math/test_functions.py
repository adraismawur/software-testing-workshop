"""Contains unit tests for the math module
"""

# this file contains a very basic test, just to make sure everything works OK.
# you can use this file as a template for your own tests by removing all the helpful comments :)

# unittest is a built-in module, you don't need to install it
import unittest

# every module we want to test must be imported
# put this import under the import for unittest or other libraries
import workshop_software_testing.math.sum_squares as sum_squares


# every test class must start with the word "Test" or end with the word "Test"!
# this is used by the test runner to identify which classes are tests
class TestMath(unittest.TestCase):
    """Contains tests for the math module"""

    # every test method must also start with the word "test"
    def test_sum_squares_both_positive(self):
        """Tests the sum_squares function when both numbers are positive"""
        # the test can contain any code you want, but it should end in one and only one assertion
        # the test should also be isolated, meaning that it should not depend on any external state

        # personally I like to separate the setup, execution and assertion of the test

        # this bit is the setup. it should contain any code that is necessary for the test to run
        a = 2
        b = 4

        # this bit would be the execution
        # I prefer to have the definitions for the expected and actual results defined like this
        # right next to each other at the end so I always know where to find them
        expected_result = 20
        actual_result = sum_squares.sum_squares(a, b)

        # finally, we have the assertion. this should be the last line of the test
        self.assertEqual(expected_result, actual_result)
