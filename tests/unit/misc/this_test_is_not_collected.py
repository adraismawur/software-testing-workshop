"""Contains a perfectly functional test that does not get executed because the
file is not named correctly
"""

import unittest


class TestThis(unittest.TestCase):
    def test_this(self):
        """This test is not going to be collected because the file is not
        named correctly
        """
        self.assertTrue(True)
