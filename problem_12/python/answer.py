import os
import imp
import math
from timeit import default_timer as timer


f= os.path.dirname(os.path.realpath(__file__))
f+="/../../"

def getMethod(p,m):
    with open(f+p+"/"+m+".py") as source:
        ff = imp.load_module(m, source, "../", ('', '', imp.PY_SOURCE))
    return ff

def getNumDivisors(t):
    divisors=0
    s=math.sqrt(t)
    for j in range(1,int(math.ceil(s))):
        if t % j == 0:
            divisors+=2
    if s*s == t:
        divisors-=1
    return divisors

def getTriangleNumDivisors(divs=6):
    t=1
    if divs <= 1:
        return t
    i=2
    while getNumDivisors(t) < divs:
        t+=i
        i+=1
    return t

def primeFactorisationNoD(number,primeList):
    #https://www.mathblog.dk/triangle-number-with-more-than-500-divisors/
    nod=1
    remain=number
    for i in range(len(primeList)):
        if primeList[i]**2 > number:
            return nod*2
        exp=1
        while remain % primeList[i] == 0:
            exp+=1
            remain/=primeList[i]
        nod *= exp
        if remain == 1:
            return nod
    return nod

def getFasterTriNumDivs(n=6):
    #https://www.mathblog.dk/triangle-number-with-more-than-500-divisors/
    primes=getMethod("problem_3/python","answer").primesfrom2to(n*2)
    cnt=0
    i=2
    dn=2
    dn1=0
    while cnt < n:
        if i % 2 == 0:
            dn = primeFactorisationNoD(i+1,primes)
            cnt=dn * dn1
        else:
            dn1=primeFactorisationNoD((i+1)/2,primes)
            cnt=dn*dn1
        i+=1
    return i*(i-1)/2

def main():
    return  getFasterTriNumDivs(500) #getTriangleNumDivisors(500)

def checkAnswer():
    return getMethod("/","tester").getAnswer(12)

if __name__ == '__main__':
    start = timer()
    n=str(main())
    end = timer()
    a=checkAnswer()
    if a == str(n):
        print "Correct"
        print "\tTotal Time:\t"+str(end - start)
    else: print "Wrong, Correct is: "+a
    print n
