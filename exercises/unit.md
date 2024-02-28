# Unit testing guide

This file contains some pointers you may be able to use when creating unit tests.

These are supposed to teach you more specifically about ways of asserting and how to construct a test suite.

## Sample application

All of these exercises revolve around the set of methods and classes under the workshop_software_testing/ folder

This application consists of a few workflows that (inefficiently) read a list of cities and populations in the following format:

```
wageningen,38774
sneek,33855
```

This application has a script to run the main function in the root folder (`workshop.py`), which calls a function in `workshop_software_testing/main.py`.

The application contains a number of simple submodules
- classes: contains the city class
- io: contains functions to read and write files
- math: contains functions to do some math
- stats: contains a parser that converts rows and columns in the population file to city classes

For these exercises, you mostly be writing tests for existing functions.
Only in the test-driven-development example will you be guided in writing a function.


## Simple asserts

### Asserting simple types

Often you will want to check if a function returns a particular value, or if a function has changed a property on a class.

There are a lot of assert methods that you can use in order to check if this is the case.

1. Create a new test suite for the cities class.
    - Make sure that the python file starts with `test`, and that the test method is in a test class which extends `unittest.TestCase`
    - Also make sure the name of method within the class starts with `test` and is descriptive
    - If you are unsure what to write, you can copy the sample test under `tests/unit/math/test_functions.py`

2. In the test method, create a new `City` object: 
    - You will need to import the city module using `import workshop_software_testing.classes.city as city` or `from workshop_software_testing.classes.city import City`
    - Instantiate the city using `test_city = City(name, population)`
3. check if the `test_city.population` method contains the number you expect using `self.assertEqual`

But this is not a very useful test.
Usually you can trust constructor (the `__init__` method in a class, see `workshop_software_testing/classes/city.py`) to work correctly.

The only reason you would really want to test a constructor is if you are doing something fancy, like calling another method inside the constructor, or if you have some if-else logic built into the constructor.

A more useful test would be to see if the `has_people_in_it` method on the `City` class returns an expected value.

1. Create a new test method
2. In this new method, create a city object using `test_city = City(name, population)` 
3. Check if the `test_city.has_people_in_it()` method returns an expected value with `self.assertTrue` or `self.assertFalse`
4. Does the test behave according to what you expect?

In this case, if your test does not do what you expect it to do, check if the code it is testing is correct.
The code being tested exists in `workshop_software_testing/classes/city.py`.


## Important asserts for specific types

There are specific assert methods which are more appropriate for certain types than an assertEqual.
These have a built-in tolerance range or give you more information about what the difference is between an expected value and an actual value.

In this example, we will explore two such asserts:
- AssertAlmostEqual
- AssertListEqual

In your work you will likely encounter data in the form of floating-point numbers (containing decimals) as opposed to whole integers.
Because of technical reasons very much beyond the scope of this exercise, floating point numbers


## Expecting certain types from methods

## expecting errors

- assertraises

## expecting logs

- assertlogs

## Using setup and teardown
