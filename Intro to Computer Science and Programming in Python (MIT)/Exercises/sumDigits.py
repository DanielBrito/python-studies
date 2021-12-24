def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    if N<10:
      return N
    
    return N%10 + sumDigits(N//10)