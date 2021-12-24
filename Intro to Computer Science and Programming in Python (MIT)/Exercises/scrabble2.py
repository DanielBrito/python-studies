def updateHand(hand, word):
    output = hand.copy()
    for letter in word:
        if letter in output.keys():
            output[letter] -= 1
    return output
