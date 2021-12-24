def playGame(wordList):
    while True:
        user_input = str(input('Enter n to deal a new hand, r to replay the last hand, or e to end game: '))
        if user_input == 'e':
            break
        elif user_input == 'n':
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
        elif user_input == 'r':
            try:
                playHand(hand, wordList, HAND_SIZE)
            except:
              print('You have not played a hand yet. Please play a new hand first!')                           
        else:
            print('Invalid command.')