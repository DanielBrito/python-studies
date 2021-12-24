import string
alph = string.ascii_lowercase

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    remain = []
    for i in alph:
        if i not in lettersGuessed:
            remain.append(i)
    return ''.join(remain)