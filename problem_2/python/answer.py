
def fib(max=100,s=1):
    nums=[]
    ss=1
    while ss < max:
        nums.append(ss)
        t=ss
        ss+=s
        s=t
    return nums

def evenFibs(max=100,s=1):
    nums=[]
    ss=1
    while ss < max:
        if ss%2==0:
            nums.append(ss)
        t=ss
        ss+=s
        s=t
    return nums

def main():
    return sum(evenFibs(4e6))

if __name__ == '__main__':
    print main()
