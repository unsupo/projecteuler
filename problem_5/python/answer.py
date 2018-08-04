

def smallestMultiple(min=1,max=10):
    if min == 1:
        min=2
    nums=range(min,max+1)
    i=max
    while True:
        allDivisible=True
        for j in nums:
            if i%j!=0:
                allDivisible=False
                break
        if allDivisible:
            return i
        i+=max
    return None


def smallestMult(min=1,max=10):
    #https://www.mathblog.dk/project-euler-problem-5/
    import os
    import math
    import imp

    f= os.path.dirname(os.path.realpath(__file__))
    f+="/../../problem_3/python"
    with open(f+"/answer.py") as source:
        ff = imp.load_module("answer", source, "./", ('', '', imp.PY_SOURCE))
    p = ff.primesfrom2to(max)
    r=1
    for i in range(len(p)):
        a=int(math.floor(math.log(max)/math.log(p[i])))
        r*=int(math.pow(p[i],a))
    return r

def main():
    return smallestMult(max=20)

if __name__ == '__main__':
    # print main()
    from timeit import default_timer as timer
    start = timer()
    a=smallestMult(max=20)
    end = timer()
    print str(end-start)+"\n\t"+str(a)
    start = timer()
    a=smallestMultiple(max=20)
    end = timer()
    print str(end-start)+"\n\t"+str(a)
