def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    result = ()
    for i in range(0, len(aTup)):
        if(i%2==0):
            result = result + (aTup[i],)
    
    return result

print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))