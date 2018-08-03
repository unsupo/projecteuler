import math


def getFactors(num=13195):
    facts=[]
    for i in range(2,num):
        if num%i==0:
            facts.append(i)
    return facts

def getPrimes(max=13195):
    primes=[2]
    for i in range(3,int(math.ceil(math.sqrt(max)))):
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
    print main()
