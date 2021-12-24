def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    minValue = min(a, b)
    gcd = 0
    
    for i in range(1, minValue+1):
        if(a%i==0 and b%i==0):
            gcd = i
            
    return gcd