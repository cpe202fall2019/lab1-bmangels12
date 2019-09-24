import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    # Add more tests!

    def test_repr1(self):
        loc = Location("Sac", -123.2, 34.2)
        self.assertEqual(repr(loc),"Location('Sac', -123.2, 34.2)")


if __name__ == "__main__":
        unittest.main()
