
def sumSrDiff(n=10):
    sum=0
    sumSr=0
    for i in range(1,n+1):
        sum+=i
        sumSr+=i**2
    return sum**2-sumSr

def main():
    return sumSrDiff(100)

def checkAnswer():
    import os
    import imp
    f= os.path.dirname(os.path.realpath(__file__))
    f+="/../../"
    with open(f+"/tester.py") as source:
        ff = imp.load_module("tester", source, "../../", ('', '', imp.PY_SOURCE))
    return ff.getAnswer(6)

if __name__ == '__main__':
    n=str(main())
    a=checkAnswer()
    if a == n:
        print "Correct"
    else: print "Wrong, Correct is: "+a
    print n
