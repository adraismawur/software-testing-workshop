"""Contains a perfectly functional test that does not get executed because of
an incorrectly named method
"""

import unittest


class TestThisPlease(unittest.TestCase):
    def this_is_a_test(self):
        """This test is not going to be collected because it does not start
        with the word test
        """
        self.assertTrue(True)


class TestThisAlsoPlease:
    def test_this_also(self):
        """This test is not going to be collected because it is not a subclass
        of TestCase
        """
        self.assertTrue(True)
