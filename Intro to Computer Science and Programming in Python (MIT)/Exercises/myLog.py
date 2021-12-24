def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    exp = 1
    result = -1
    
    while result <= x:
      result = b**exp
      exp += 1
      
    return exp-2