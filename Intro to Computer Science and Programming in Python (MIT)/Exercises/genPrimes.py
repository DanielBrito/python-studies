def genPrimes():
    primes = [2]
    yield primes[0]
    guess = 3
    
    while True:
        if all(guess%x != 0 for x in primes):
            primes.append(guess)        
        if guess == primes[-1]:
            yield primes[-1]
        guess += 2
