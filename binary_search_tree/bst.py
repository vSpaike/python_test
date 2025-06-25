
class BinarySearchTree: 

    def __init__(self,array):
        self.bst=array


    def to_bst(self,array):
        if len(array)==0:
            return []
        #TO FINISH


    def valid(self):
        for i in range(len(self.bst)//2):
            if((self.bst[2*i + 1] != None) and (self.bst[i] < self.bst[2*i + 1])) or ((self.bst[2*i + 2] != None) and (self.bst[i] > self.bst[2*i + 2])):
                return False
        return True


    def exists(self,value):
        current_index = 0
        
        while (current_index < len(self.bst)):
            if value > self.bst[current_index]:
                current_index= current_index *2+2
            elif value < self.bst[current_index]:
                current_index= current_index *2+1
            else:
                return True
        
        return False


    def smallest(self):
        if self.bst[len(self.bst)//2] == None:
            return self.bst[(len(self.bst)//2-1)//2]
        if (len(self.bst)+1)%2 == 0:
            return self.bst[(len(self.bst)+1)//2]
        return self.bst[len(self.bst)//2]


    def biggest(self):
        if(self.bst[-1] == None):
            return self.bst[((len(self.bst)-1)//2)-1]
        return self.bst[-1]


    def sorted_array(self): 
        final= []
        current=[self.bst[0]]
        index=0
        for i in range (len(self.bst)//2):
            pass


if __name__ == "__main__":
    a= BinarySearchTree([6,3,7])
    print(a.exists(98))