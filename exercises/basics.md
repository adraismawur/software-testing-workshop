# Basic information

This file contains instructions for the basics of unit testing.
Reading these sections should tell you all you need to know to write test methods that test runners can find and run.

## Test runners

These exercises use unittest by running `python -m unittest`, the built-in test module for python.
In order to see arguments that you can pass to the test runners, try `python -m unittest --help`

There are other test runners that you can use e.g. `pytest` that you can install using PIP.
However note that these exercises all use `python -m unittest`

Most test runners behave the same, in that they will try to discover any tests in the same directory this readme is in (the root directory).
However, some test runners do behave differently or display results differently.
Exploring these differences is beyond the scope of this workshop.


## Folder structure

The folder structure presented here is relatively common, and the same as the python template at https://github.com/adraismawur/python-template-maxi

You may note that the tests/ folder contains a blank `__init__.py`, making it a module.
This is necessary in order for the tests to be discovered.
If you find that your tests are not being discovered, check if your test folder and subfolders have an `__init__.py`

Some projects prefer to put tests next to the code that is being tested, which is also a valid way to structure test code.
It is up to you to decide what you prefer.

# exercises

The following sections contain practical exercises

## Discovering tests

Test runners rely on naming files, classes and methods correctly (usually starting with 'test') in order to distinguish between test code and source code

Note that what criteria there are for tests depends on the test runner.
The unittest module we are using in these exercises expect files and methods to begin with 'test'.
Classes are more flexible, as long as they extend the `unittest.TestCase` class.

If you explore the tests/unit directory, you may find that there are actually __four__ uncommented tests that exist in the following files, but the runner only finds one!
- tests/unit/math/test_functions.py (1 test)
- tests/unit/misc/this_test_is_not_collected.py (1 test)
- tests/unit/misc/test_name_correct_but_no_collect.py (2 tests!)

The reasons why are as follows:

- The test in `this_test_is_not_collected.py` is not collected by the test runners because the filename does not begin with 'test'
- Then, in the `test_name_correct_but_no_collect.py` file:
    - The `TestThisPlease.this_is_a_test` test is not collected because the method does not start with 'test'
    - the `TestThisAlsoPlease.test_this_also` test is not collected because the class does not extend `unittest.TestCase`

#### Exercise

Try fixing these tests by giving the file and method correct names, and adding the missing class extension.
Then run `python -m unittest`. You should see something like this:

```
$ python -m unittest
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

It can be frustrating when test runners do not detect your tests.
- Make sure that your tests are under a module (includes an `__init__.py`)
- and are detected by the test runner (names of files, classes and methods start with `test`, classes extend `unittest.TestCase`)


⚠️ __Before continuing to the next exercise, reset the repository state with `git reset --hard`__

⚠️ __You may also need to remove untracked files by running `git clean -f`__


### Getting used to failing tests

The output of unit test runners can quickly be overwhelming when there are a lot of failed tests.
To get used to what failing tests look like, uncomment any code in `test/unit/misc/test_failing.py`, then run `python -m unittest`

We can break the output down bit by bit, top to bottom.

On the first line unittest reports how many tests were run.
A dot indicates a successful run, an F indicates a failure.
If you have not fixed the other tests, it should look something like this:

```
.FFFF
```

The rest of the output from unittest reports the error for each individual test.
Each failed test report starts with a bunch of equal signs, then shows the name and location of the test, then closes off with a bunch of dashes:

```
======================================================================
FAIL: testFailBoolean (tests.unit.misc.test_failing.TestFail)
A simple test that fails as long as the universe is still operating normally
----------------------------------------------------------------------
```

Then it shows you the python output that generated an error in that code.
This could be an error in the python code of the test itself, but should hopefully be an AssertionError:

```
Traceback (most recent call last):
  File "/home/drais008/src/workshop-software-testing/tests/unit/misc/test_failing.py", line 9, in testFailBoolean
    self.assertTrue(False)
AssertionError: False is not true
```

This particular assertion error indicates that False is not true.
This is not a very useful test, but you will see a similar error if you expect the output of a function to be true but it returns false, for example.

In order to fix these errors, see if you can go through each failed test and change the `actual_value` such that they no longer fail the test.

⚠️ __Before continuing to other exercises, reset the repository state with `git reset --hard`__

### Next up

This concludes the basic testing material.
Proceed onto unit.md for the implementation of these concepts.

If you have extra time afterwards, there are additional concepts in extra.md that are useful for developing and running tests.
