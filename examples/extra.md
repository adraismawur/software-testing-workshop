# Extra testing exercises

These are some extra exercises for if you have extra time.
The following concepts are not strictly necessary but can be very useful.

### Filtering tests

If you have a lot of tests, you may want to limit the tests you run while developing to only those which you consider relevant to your current work.

Test runners have ways of matching the names of test classes and methods to a specified string.
In `unittest` (used here) and `pytest` for example, this is done by adding `-k <pattern>` to the command.

You can try running only the math tests by running `python -m unittest -k math`.
Then try searching for tests that do not exist by running `python -m unittest -k foo`.
You should see something like this:

```
$ python -m unittest -k foo
----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
```

Since there is no test that contains 'foo' in any class or method, no tests are executed.


### Getting more information from a test run

The default output for testing is pretty minimal.
Try running `python -m unittest -v` to get a verbose output so that you can see if all tests are being executed. The output if you have not added any additional tests should be something like this:

```
$ python -m unittest -v
test_sum_squares_both_positive (tests.unit.math.test_functions.TestMath)
Tests the sum_squares function when both numbers are positive ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

The above output indicates that one test was executed, under `tests/unit/math/test_functions.py` in the class `TestMath`.

`unittest` also shows you the docstring under the method definition.
This is a good reason to make those docstrings descriptive.

## Skipping tests

As a final basic testing exercise, we will skip a test.
Skipping tests is useful if you want to add a bunch of test methods in advance of creating some code, but do not yet want to implement the actual tests.
Skipping tests can also be useful if you changed some functionality in a way that breaks a test, but do not want to fix it yet.

In order to see what this looks like, go to the four failing tests you just fixed, and add `self.skipTest("Expected to fail") to the beginning of each test method, as follows:

```py
class TestFail(unittest.TestCase):
    def testFailBoolean(self):
        """A simple test that fails as long as the universe is still operating normally"""
        self.skipTest("Expected to fail")

        self.assertTrue(False)
```

If you are using an IDE, you may see that the `self.assertTrue` call is now greyed out because it no longer is accessible ("dead code").

This is because `self.skipTest` will halt execution of the rest of this method.
This is very useful if you do not want to throw away all the test code.

Now, when you run `python -m unittest` you should see something like this:

```
$ python -m unittest
.ssss
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK (skipped=4)
```

As you can see, all tests are OK but four were skipped.

The argument passed to `self.skipTest` is a message you can add so that you can indicate why a test was skipped. This information is included if you run `python -m unittest -v`

```
$ python -m unittest -v
test_sum_squares_both_positive (tests.unit.math.test_functions.TestMath)
Tests the sum_squares function when both numbers are positive ... ok
testFailBoolean (tests.unit.misc.test_failing.TestFail)
A simple test that fails as long as the universe is still operating normally ... skipped 'Expected to fail'
testFailDict (tests.unit.misc.test_failing.TestFail)
A test that fails because two dictionaries are not equal ... skipped 'Expected to fail'
testFailEquality (tests.unit.misc.test_failing.TestFail)
A more complex test that fails when maths is still maths ... skipped 'Expected to fail'
testFailList (tests.unit.misc.test_failing.TestFail)
A test that fails because two lists are not equal ... skipped 'Expected to fail'

----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK (skipped=4)
```