
def isPalindrome(num):
    v=str(num)
    for i in range(len(v)):
        if v[i]!=v[-(i+1)]:
            return False
    return True

def fact(num,stop=None):
    if not stop:
        stop=num
    n=1
    while stop>0:
        n*=num
        num-=1
        stop-=1
    return n

def permute(digits=2):
    d=[1,2,3,4,5,6,7,8,9,0]
    d=[str(i) for i in d]
    perms=[]
    for i in range(pow(10,digits-1),pow(10,digits)):
        if len(str(i)) < digits:
            continue
        perms.append(i)
    return perms

def largestPalindrome(digits=2):
    perms=permute(digits)
    max=0
    for i in perms:
        for j in perms:
            if i*j<max:
                continue
            if isPalindrome(i*j):
                max=i*j
    return max

def main():
    return largestPalindrome(3)

if __name__ == '__main__':
    print main()
