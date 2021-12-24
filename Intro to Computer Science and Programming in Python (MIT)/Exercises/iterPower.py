def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp==0:
        return 1
    
    result = 1
        
    for i in range(0, exp):
        result *= base
    
    return result