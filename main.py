from number_operation import generatePrimeNumber, split_conseq
from binary_search_tree import BinarySearchTree

#----------------------------------------------------------------
# Demonstration first part
#----------------------------------------------------------------

#The limit of prime number generated
number_to_stop = 30
prime_number = generatePrimeNumber(number_to_stop)

print("\nThe first",number_to_stop,"numbers:",prime_number,"\n")

#List of number to split
number_to_split=[1,2,3,6,9,42,89,90,99]
split_number= split_conseq(number_to_split)

print("These consequent numbers are:",split_number,"\n")


#----------------------------------------------------------------
# Demonstration second part
#----------------------------------------------------------------

simple_array=[1,2,3,4,5,6,7]

bst=BinarySearchTree(simple_array)
new_array=bst.to_bst()

print("The array in binary search tree form:", new_array)
bst.setArray(new_array)

print("The biggest and smallest element are:",bst.biggest(),",",bst.smallest())





