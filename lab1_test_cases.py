import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
    def test_max_list_iter2(self):
        # checking if the function works correctly, should result in 4
        list = [1, 2, 3, 4]
        self.assertEqual(max_list_iter(list), 4)
    def test_max_list_iter3(self):
        # checking if an empty list results in None
        list = []
        self.assertEqual(max_list_iter(list), None)


    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
    def test_reverse_rec2(self):
        #second test of list   
        self.assertEqual(reverse_rec([3,2,1]),[1,2,3])    
    def test_reverse_rec3(self):
        #to test for value error
        tlist = None
        with self.assertRaises(ValueError):
            reverse_rec(tlist)

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
    def test_bin_search2(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(1, 2, 3, tlist)
    def test_bin_search3(self):
        list_val = [1,2,3,4]
        low = 1
        high = 3
        self.assertEqual(bin_search(1, low, high, list_val), None)


if __name__ == "__main__":
        unittest.main()

    
