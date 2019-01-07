#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Khlood Alluhaib

Finding all possible primes up to 60 mins. 
I forgot to add counter to count how many primes I optained during 60 mins
but I printed out the last three ones which were:
    75727829
    75727837
    75727849
and checked them online to make sure they are prime numbers.
"""
import time
import math
def primeFinder(p):
    isPrime = p
    exitLoop = time.time() + 60*60
    while (time.time() < exitLoop):
        for x in range(2, int(math.sqrt(isPrime) + 1)):
            if isPrime % x == 0:
                break

        else:
            print(isPrime,"is prime")
        isPrime= isPrime+1

    #print("Done")

print(primeFinder(1)) #start checking primes from 1 and increase number by 1
