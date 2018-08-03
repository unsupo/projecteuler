
def sum(v):
    s=0
    for i in v:
        s+=i
    return s

def multiples(max=10,l=[3,5]):
    m=[]
    for i in range(1,max):
        for j in l:
            if i%j==0:
                m.append(i)
    return sum(list(set(m)))

def main():
    return multiples(max=1000)

if __name__ == '__main__':
    print main()