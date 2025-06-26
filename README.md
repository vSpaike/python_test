## Run
To run it enter the line below in the main folder and run the file **main.py**:
   - pip install -r requirements.txt

## Binary search tree
### Method to_bst
In order for the method to work correctly, it is essential that the binary tree be complete on each floor. The goal during its design was to use the properties indicated in the instructions.  However, the implementation of *None* when a number is absent caused a problem and i didn't achieve to put a *None* in the list. The method works, but it does not generate a binary search tree if the list provided as a parameter is not complete.

### Method valid et exists
For *exists*, the objective was to use the tree to do a dichotomic search. It's complexity is O(log(n)) with n the size of the array.
As for *valid*, the goal ensure that the tree was indeed a binary search tree. The complexity is O(1/2*n)~O(n) since we check half of the values in the tree. 


### Method biggest
The complexity is O(1) because we only do a comparison and a few mathematical operations. This method could be optimized in my opinion but my priority wasn't this.

### Method smallest
For the method smallest i think there is a possibility to have a complexity of O(1) like the method biggest but i don't know how to write it. I spent too much time trying things so I decided to write it in another way with more complexity. The complexity if O(log2(n)) with n is the size of the list because we cross each layer once.

## Number operations
The main objective there was to optimize the program as much as i can by removing the cases where we know a number couldn't be prime like when it ended with a 2 or a 5.\
For the second question, I didn't know how I could optimize it because of the complexity. We need to go through every number on the list, and the program already has a complexity of O(n). Maybe there is a posibilty of checking the 2 numbers at the same time which could avoid going to the next in front if he's consequent.

## Tests
### Start tests
Copy the lines below and place them in the terminal, make sure to be in the main folder:
 - python -m unittest tests/test_generate.py
 - python -m unittest tests/test_split_conseq.py
 - python -m unittest tests/test_bst.py

PS: Désolé pour les fautes de grammaire ou d'orthographe, j'ai essayé de faire mon maximum mais j'ai dû en oublier