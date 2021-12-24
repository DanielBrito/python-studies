def playHand(hand, wordList, n):
    score = 0
    while calculateHandlen(hand) > 0:
        print('Current Hand:', end=' '); displayHand(hand)     
        guess = str(input('Enter word, or a "." to indicate that you are finished: '))        
        if guess == '.':        
            break            
        else:        
            if isValidWord(guess, hand, wordList) == False:            
                print('Invalid word, please try again.', '\n')
            else:
                score += getWordScore(guess, n)
                print('"'+guess+'"', "earned", getWordScore(guess, n), "points. Total:", score, "points", '\n')
                hand = updateHand(hand, guess)               

    if guess == '.':
        print('Goodbye! Total score:', score, 'points.')
    else:
        print('Run out of letters. Total score:', score, 'points.')