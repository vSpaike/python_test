def isPrime(n):
    """
    Verify if the number in parameter is prime 
    """
    #Do execption for number 5 and 2 and remove number that we know will not be prime 
    if(n%10!=5 or n==5) and (n%2!=0 or n==2):
        #Compare up to the root of the parameter because above it's useless 
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
    return False


def generatePrimeNumber(n):
    """
    Generate a stream of prime number up to the parameter n
    """
    list_prime=[]
    for i in range(2,n+1):
        if isPrime(i):
            list_prime.append(i)
    return list_prime

if __name__=="__main__":
    number = -1
    while(number <0):
        number = int(input("Type a number to stop the prime flow: "))
    print(f"The prime number are: {generatePrimeNumber(number)}")
