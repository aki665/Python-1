def prime_counter(givenNumber):
    # Initialize a list
    primes = []
    for possiblePrime in range(2, givenNumber + 1):
        # Assume number is prime until shown it is not.
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            print((possiblePrime), end=',  ')



while True:
    try:
        number = int(input("\nTo what number you want primes to be computed:\n"))
        prime_counter(number)
    except ValueError:
        print("Invalid Input!")