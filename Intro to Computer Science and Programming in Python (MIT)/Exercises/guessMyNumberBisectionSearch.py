print("Please think of a number between 0 and 100!")

hi = 100
lo = 0
guessed = False

while not guessed:

    guess = (hi + lo)//2

    print("Is your secret number " + str(guess)+ "?")

    user_inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if user_inp == 'c':
        guessed = True

    elif user_inp == 'h':
        hi = guess

    elif user_inp == 'l':
        lo = guess
        
    else:
        print("Sorry, I did not understand your input.")

print('Game over. Your secret number was: ' + str(guess))