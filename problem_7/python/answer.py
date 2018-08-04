import os
import imp

f= os.path.dirname(os.path.realpath(__file__))
f+="/../../"

def getNthPrime(n=6):
    nn=n
    primes=[2]
    i=3
    while n>0:
        j=0
        isPrime=True
        while primes[j] * primes[j] <= i:
            if i % primes[j] == 0:
                isPrime=False
                break
            j+=1
        if isPrime:
            primes.append(i)
            n-=1
        i+=2
    return primes[nn-1]

def main():
    return getNthPrime(10001)

def checkAnswer():
    with open(f+"/tester.py") as source:
        ff = imp.load_module("tester", source, "../../", ('', '', imp.PY_SOURCE))
    return ff.getAnswer(7)

if __name__ == '__main__':
    n=main()
    a=checkAnswer()
    if a == str(n):
        print "Correct"
    else: print "Wrong, Correct is: "+a
    print n
