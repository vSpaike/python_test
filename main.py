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

print("Those number consequent are:",split_number)