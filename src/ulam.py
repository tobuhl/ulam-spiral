#ulam.py

import numpy

class Ulam:

    def __init__(self,size):
        if isEven(size): 
            raise ValueError("Error: size must be odd!")
        self.size = size
        self.grid = numpy.full((size,size), 255)

    def isOdd(self,n):
        return n % 2 != 0
    
    def isEven(self,n):
        return n % 2 == 0

    def isPrime(self,n):
        if n == 2 or n == 3: return True
        if n < 2 or n%2 == 0: return False
        if n < 9: return True
        if n%3 == 0: return False

        #iterate limit is square root of n
        r = int(n**0.5)

        #iterate with steps of 5  
        f = 5
        while f <= r:
            #print '\t',f
            if n%f == 0: return False
            if n%(f+2) == 0: return False
            f +=6
        return True

        









       
        
