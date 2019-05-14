import concurrent.futures
import logging
import threading


class PrimeCounter:

    def is_prime_check(self, givenNumber, name):


        if givenNumber >= 1:
            for i in range(2, givenNumber):
                #logging.info("Thread %s, Given Number: %s, i: %s", name, givenNumber, i)
                if (givenNumber % i) == 0:

                    break
            else:
                print(givenNumber, end=',  ')




    def __init__(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=1000000) as executor:
            executor.map(self.is_prime_check, range(1000000))


        while True:
            try:
                self.number = int(input("\nTo what number you want primes to be computed:\n"))


                threads = list()
                for index in range(self.number):
                    if self.number == index:
                        break
                    else:
                        #logging.info("Main    : create and start thread %d.", index)
                        x = threading.Thread(target=self.is_prime_check, args=(0+index, index))
                        threads.append(x)
                        x.start()
                        index+=1





                #except:
                    #print("Failed to create threads!")




            except ValueError:
                print("Invalid Input!")

if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    PrimeCounter()
