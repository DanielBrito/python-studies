def isValidWord(word, hand, wordList):
    output = hand.copy()
    word_check = False
    if word in wordList:
        word_check = True
 
    letter_check = set(list(word)) <= set(output.keys())
 
    for letter in word:
        if letter in output.keys():
            output[letter] -= 1
 
    value_check = all(i >= 0 for i in output.values())
    
    if word_check == True and letter_check == True and value_check == True:
        return True
    else:
        return False