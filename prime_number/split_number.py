"""def split_conseq(l):
    if(len(l)==0):
        return []
    final=[]
    nbc=l[0]
    current=[]
    for i in l[1:]:
        current.append(nbc)
        if i != (nbc+1):
            final.append(current)
            current=[]
        nbc=i
    if len(current)>0:
        final.append(current)
    final.append([nbc])
    return final 
"""
#----------------------------
def split_conseq(l):
    if(len(l)==0):
        return []
    final=[]
    nbc=l[0]
    current=[]
    for i in range(1,len(l)):
        current.append(nbc)
        if(l[i] != nbc+1):
            final.append(current)
            current=[]
        nbc=l[i]

    #processes the last number
    if(len(current)>0):
        if current[-1]+1 == nbc:
            current.append(nbc)
            final.append(current)
    else:
        final.append([nbc])
    return final 

if __name__ == "__main__":
    list_number=[]
    number=""
    while number !="stop":
        print(f"\nThe number list: {list_number}")
        number=input('Type the number to add to the list. Type "stop" when you have finish: ')
        if number.isdigit():
            list_number.append(int(number))
    
    print(f"\nThe list split: {split_conseq(list_number)}")