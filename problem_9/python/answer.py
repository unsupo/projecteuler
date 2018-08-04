import os
import imp
import math

f= os.path.dirname(os.path.realpath(__file__))
f+="/../../"

def func(b,d):
    return d*(2*b-d)/2/(b-d)

def pythagoreanTriplet(d=1000):
    b=0
    while True:
        # where b != d
        if b == d:
            b+=1
            continue
        # where b in func(b,d)
        a=func(b,d)
        c=math.sqrt(a**2+b**2)
        # where a and b < c
        if a >= c or b >= c:
            b+=1
            continue
        # where a^2+b^2=c^2
        if round(c)!=c:
            b+=1
            continue
        return [a,b,c]

def main():
    with open(f+"/problem_8/python/answer.py") as source:
        ff = imp.load_module("answer", source, "../", ('', '', imp.PY_SOURCE))
    return int(ff.prod(pythagoreanTriplet()))

def checkAnswer():
    with open(f+"/tester.py") as source:
        ff = imp.load_module("tester", source, "../", ('', '', imp.PY_SOURCE))
    return ff.getAnswer(9)

if __name__ == '__main__':
    n=main()
    a=checkAnswer()
    if a == str(n):
        print "Correct"
    else: print "Wrong, Correct is: "+a
    print n

"""
a+b+c=1000 => c=1000-a-b
a<b<c
a^2+b^2=c^2

a^2+b^2=(1000-a-b)^2=1000^2-1000a-1000b-1000a+a^2+ab-1000b+ab+b^2
0=1000^2-2000a-2000b+2ab=1000^2+a(2b-2000)-2000b
(2000b-1000^2)/(2b-2000)=a

1000*(b-500)/(b-1000)=a

d(2b-d)/2/(b-d)=a
"""