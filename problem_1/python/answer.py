
def sum(v):
    s=0
    for i in v:
        s+=i
    return s

def multiples(max=10,mults=[3,5]):
    s=0
    for i in range(1,max):
        isMult=False
        for mu in mults:
            if i % mu == 0:
                isMult=True
        if isMult:
            s+=i
    return s

def main():
    return multiples(max=1000)

if __name__ == '__main__':
    print main()