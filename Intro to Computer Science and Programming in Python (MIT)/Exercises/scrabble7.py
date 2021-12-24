def playGame(wordList):
    while True:
        user_input = str(input('Enter n to deal a new hand, r to replay the last hand, or e to end game: '))
        if user_input == 'e':
            break
        elif user_input == 'n':
            while True:
                play_mode = str(input('Enter u to have yourself play, c to have the computer play: '))
                if play_mode == 'u':
                    hand = dealHand(HAND_SIZE)
                    playHand(hand, wordList, HAND_SIZE)
                    break
                elif play_mode == 'c':
                    hand = dealHand(HAND_SIZE)
                    compPlayHand(hand, wordList, HAND_SIZE)
                    break
                else:
                    print('Invalid command.')            
        elif user_input == 'r':
            try:
                hand
                play_mode = str(input('Enter u to have yourself play, c to have the computer play: '))
                if play_mode == 'u':
                    playHand(hand, wordList, HAND_SIZE)
                elif play_mode == 'c':
                    compPlayHand(hand, wordList, HAND_SIZE)
                else:
                    print('Invalid command.')
            except:
                print('You have not played a hand yet. Please play a new hand first!')
        else:
            print('Invalid command.')