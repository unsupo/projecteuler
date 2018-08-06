import os
import imp
import math
from timeit import default_timer as timer


f= os.path.dirname(os.path.realpath(__file__))
f+="/../../"

def getMethod(p,m):
    with open(f+p+"/"+m+".py") as source:
        ff = imp.load_module(m, source, "../../", ('', '', imp.PY_SOURCE))
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

def main():
    return getTriangleNumDivisors(500)

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
