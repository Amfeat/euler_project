import time

start_time = time.process_time() 

def sum_of_primes(n):
    '''
    OUTPUT: Returns sum of prime numbers in range(1, n)
    '''
    # list to store prime numbers 
    prime = [True] * (n + 1) 
      
    p = 2
    while p * p <= n: 
 #       print(p)
        # If prime[p] is not changed, then 
        # it is a prime 
        if prime[p] == True: 
            # Update all multiples of p that are >= p**2 
            i = p ** 2
            while i <= n: 
                prime[i] = False
                i += p 
        p += 1    
           
    # Return sum of primes generated through 
    # Sieve. 
    sum = 0
    for i in range (2, n + 1): 
        if(prime[i]): 
            sum += i 

    return sum

print(sum_of_primes(200000000))

print("--- %s seconds ---" % (time.process_time() - start_time))
print('\a')