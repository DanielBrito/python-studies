def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if(aStr==''):
        return False
    
    if(len(aStr)==1):
        return char==aStr    
    
    middlePosition = len(aStr)//2
    middleChar = aStr[middlePosition]
    
    if(char==middleChar):
        return True
    elif(char<middleChar):
        return isIn(char, aStr[:middlePosition])
    else:
        return isIn(char, aStr[middlePosition+1:])