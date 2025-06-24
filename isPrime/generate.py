def isPrime(n):
    if n>1:
        for i in range(2//n+1):
            if n/i==1:
                return False
        return True
    return False