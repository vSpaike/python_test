import unittest
from binary_search_tree import BinarySearchTree 

class TestBinarySearchTree(unittest.TestCase):

    # def test_to_bst(self):

    def test_valid_bst(self):
        self.assertEqual(BinarySearchTree([6,3,7,2,4,None,9]).valid(), True)
        
    def test_not_valid_bst(self):
        self.assertEqual(BinarySearchTree([6,3,7,2,4,8,9]).valid(), False)
    
    def test_one_leaf_bst(self):
        self.assertEqual(BinarySearchTree([6]).valid(), True)

    def test_number_in_bst(self):
        self.assertEqual(BinarySearchTree([6,3,7,2,4,None,9]).exists(4), True)

    def test_number_not_in_bst(self):
        self.assertEqual(BinarySearchTree([6,3,7,2,4,None,9]).exists(8), False)

    def test_smallest_odd_bst(self): 
        self.assertEqual(BinarySearchTree([6,3,7,2,4,None,9]).smallest(), 2)

    def test_smallest_even_bst(self): 
        self.assertEqual(BinarySearchTree([6,3,7,1,4,None,10,0,2,None,5,9,11]).smallest(), 0)

    def test_smallest_with_none_bst(self): 
        self.assertEqual(BinarySearchTree([6,3,7,None,4,None,9]).smallest(), 3)

    def test_biggest_bst(self): 
        self.assertEqual(BinarySearchTree([6,3,7,2,4,None,9]).biggest(), 9)

    def test_biggest_with_none_bst(self): 
        self.assertEqual(BinarySearchTree([6,3,7,2,4,None,None]).biggest(), 7)

    def test_biggest_one_leaf_bst(self): 
        self.assertEqual(BinarySearchTree([6]).biggest(), 6)