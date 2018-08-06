import os
import imp
f= os.path.dirname(os.path.realpath(__file__))
f+="/../../"

def getMethod(p,m):
    with open(f+p+"/"+m+".py") as source:
        ff = imp.load_module(m, source, "../", ('', '', imp.PY_SOURCE))
    return ff

def main():
    return sum(getMethod("/problem_3/python","answer").primesfrom2to(int(2e6)))

def checkAnswer():
    return getMethod("/","tester").getAnswer(10)

if __name__ == '__main__':
    n=main()
    a=checkAnswer()
    if a == str(n):
        print "Correct"
    else: print "Wrong, Correct is: "+a
    print n
