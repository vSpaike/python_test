import unittest 
from prime_number import split_conseq

class TestSplitNumber(unittest.TestCase):

    def test_split_seq(self):
        self.assertEqual(split_conseq([1,2,3,10]), [[1,2,3],[10]])

    def test_negative_conseq(self):
        self.assertEqual(split_conseq([-12,-3,-2,-1,9]), [[-12],[-3,-2,-1],[9]])
    
    def test_not_split(self):
        self.assertEqual(split_conseq([1,2,3,4,5,6,7,8,9]), [[1,2,3,4,5,6,7,8,9]])
    
    def test_empty_list(self):
        self.assertEqual(split_conseq([]), [])

    def test_unsorted_list(self):
        self.assertEqual(split_conseq([9,5,7,3,4,42,80,99]), [[9], [5], [7], [3, 4], [42], [80], [99]])
    
if __name__ == "__main__":
    unittest.main()