from math import floor, sqrt
from time import time
start = time()

def prime_sieve(upperlimit):
    primality = [True for i in range(upperlimit+1)]
    primality[0] = False
    primality[1] = False

    for i in range(2,floor(sqrt(upperlimit))+1):
 #       if primality[i]:
            j = i**2
            while j <= upperlimit:
                primality[j] = False
                j += i

    return [p for p in range(upperlimit+1) if primality[p]] 

target = 2000000

print("Answer: ", sum(prime_sieve(target)))
print("Time: ", time() - start)