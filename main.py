from number_operation import generatePrimeNumber, split_conseq
from binary_search_tree import BinarySearchTree

#----------------------------------------------------------------
# Demonstration first part
#----------------------------------------------------------------

print("----------------------------------------------------------------")
print("First Part")
print("----------------------------------------------------------------")

#The limit of prime number generated
number_to_stop = 30
prime_number = generatePrimeNumber(number_to_stop)

print("The first",number_to_stop,"numbers:",prime_number)

#List of number to split
number_to_split=[1,2,3,6,9,42,89,90,99]
split_number= split_conseq(number_to_split)

print("These consequent numbers are:",split_number,"\n")


#----------------------------------------------------------------
# Demonstration second part
#----------------------------------------------------------------
print("----------------------------------------------------------------")
print("Second Part")
print("----------------------------------------------------------------")
simple_array=[1,2,3,4,5,7,6]

bst=BinarySearchTree(simple_array)
new_array=bst.to_bst()

print("The array in binary search tree form:", new_array)
#Set new form of the array
bst.setArray(new_array)
print("Is this new form correcte ?",bst.valid())

print("The biggest and smallest element are:",bst.biggest(),",",bst.smallest())

element_to_verify=8
print("Is",element_to_verify,"in the bst ?",bst.exists(element_to_verify))

print("The new array in an sorted array:", bst.sorted_array())
print("----------------------------------------------------------------")




