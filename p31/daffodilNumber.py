def judge(n):
    temp=n
    m=len(str(n))
    sum=0
    for c in range(m):
        sum+=pow(n%10,m)
        n//=10
    if sum==temp:
        return True
    else:
        return False

def printDaffodiNumber(max):
    for i in range(100,max+1):
        if judge(i):
            print(i)

if __name__ == '__main__':
    print(judge(153))

    printDaffodiNumber(1000)