
from timeit import default_timer as timer
import os
import imp
f= os.path.dirname(os.path.realpath(__file__))
f+="/../../"

def getMethod(p,m):
    with open(f+p+"/"+m+".py") as source:
        ff = imp.load_module(m, source, "../../", ('', '', imp.PY_SOURCE))
    return ff

def collatzFunc(n):
    if n % 2 == 0:
        return n/2
    return 3 * n + 1

memoize={}
def getCollatzSeqCnt(start):
    if start in memoize:
        return memoize[start]
    i=1
    n=start
    nums={}
    while n > 1:
        if n in memoize:
            i += memoize[n]
            break
        n=collatzFunc(n)
        nums[n]=i
        i+=1
    memoize[start]=i
    for k,v in nums.iteritems():
        memoize[k]=i-v
    return i

def getLongestCollatz(max=1e6):
    maxValue=0
    chainNumber=2
    for i in range(3,int(max),2):
        v=getCollatzSeqCnt(i)
        if v > maxValue:
            maxValue=v
            chainNumber=i
    return chainNumber

def main():
    return getLongestCollatz()

def checkAnswer():
    return getMethod("/","tester").getAnswer(14)

if __name__ == '__main__':
    start = timer()
    n=str(main())
    end = timer()
    a=checkAnswer()
    if a == str(n):
        print "Correct"
        print "	Total Time:	"+str(end - start)
    else: print "Wrong, Correct is: "+a
    print n
