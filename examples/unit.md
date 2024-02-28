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

- assert true/false
- assert equal


## Important asserts for certain types

- List
- Dict
- almostequal

## expecting errors

- assertraises

## expecting logs

- assertlogs
