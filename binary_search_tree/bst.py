import math

class BinarySearchTree: 

    def __init__(self,array):
        """
        Define a class for binary search tree (bst) with only an array 
        """
        self.bst=array
        self.size=len(array)

    def to_bst(self):
        """
        Transform an array into a bst recursively        
        """
        if not len(self.bst):
            return []
        self.bst.sort()
        final = self.bst.copy()

        def create_rec_bst(start, index, end, prec):
            if start>end or index>=self.size:
                return None
            
            middle = (start+end)//2
            final[index] = self.bst[middle]                 

            #left part
            create_rec_bst(start, 2*index+1, middle - 1, self.bst[middle])
            
            #right part
            create_rec_bst(middle + 1, 2*index+2, end,self.bst[middle])

        create_rec_bst(0, 0,self.size-1, None)
        return final
        

    def valid(self):
        """
        Verify is the array is a bst or no
        """
        for i in range(self.size//2):
            if((self.bst[2*i + 1] != None) and (self.bst[i] < self.bst[2*i + 1])) or ((self.bst[2*i + 2] != None) and (self.bst[i] > self.bst[2*i + 2])):
                return False
        return True


    def exists(self,value):
        """
        Verify if the parameter 'value' is in the bst
        """
        current_index = 0
        
        while (current_index < self.size):
            if value > self.bst[current_index]:
                current_index= current_index *2+2
            elif value < self.bst[current_index]:
                current_index= current_index *2+1
            else:
                return True
        return False


    def smallest(self):
        """
        Find the smallest element of the tree
        """
        size= int(math.log2(self.size))+1
        if size==2:
            size-=1
        current = self.bst[0]
        for i in range(size):
            if self.bst[2*i+1] != None:
                current = self.bst[2*i+1]  
        return current

    def biggest(self):
        """
        find the biggest element of the tree
        """
        if(self.bst[-1] == None):
            return self.bst[((self.size-1)//2)-1]
        return self.bst[-1]


    def sorted_array(self):
        """
        Transform the bst into an sorted array 
        """
        if not len(self.bst):
            return []
        
        final=self.bst.copy()

        def sorted_rec(start, index, end):
            if start>end or index>=self.size:
                return None
            
            middle = (start+end)//2
            #Change the ordre compare to to_bst because we want the opposite function 
            final[middle] = self.bst[index]
            #left part
            sorted_rec(start, 2*index+1, middle - 1)
            
            #right part
            sorted_rec(middle + 1, 2*index+2, end)
        
        sorted_rec(0, 0, self.size-1)
        return final

    def setArray(self, array):
        """
        Setter for the array 
        """
        self.bst=array

if __name__ == "__main__":
    print("Hello, World")