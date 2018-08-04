import math


def getFactors(num=13195):
    facts=[]
    for i in range(2,num):
        if num%i==0:
            facts.append(i)
    return facts

def getPrimes(limit):
    primes=[2]
    for i in range(3,limit,2):
        j=0
        isPrime=True
        while primes[j] * primes[j] <= i:
            if i % primes[j] == 0:
                isPrime=False
                break
            j+=1
        if isPrime:
            primes.append(i)
    return primes

def primesfrom2to(n):
    import numpy as np
    # primes https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

def getPrimesA(max=13195):
    primes=[2]
    for i in range(3,max):
        isPrime=True
        for p in primes:
            if i%p==0:
                isPrime=False
        if isPrime:
            primes.append(i)
    return primes

def isPrime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i=5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i+=6
    return True

def getPrimeFactor(num=13195):
    maxFact=2
    for i in range(2,int(math.ceil(math.sqrt(num)))):
        if num%i==0 and isPrime(i):
            maxFact = i
    return maxFact

def main():
    return getPrimeFactor(600851475143)

if __name__ == '__main__':
    # print main()
    from timeit import default_timer as timer
    start = timer()
    a=primesfrom2to(10000)
    end = timer()
    print str(end-start)+"\n\t"+str(a)
    start = timer()
    a=getPrimes(10000)
    end = timer()
    print str(end-start)+"\n\t"+str(a)