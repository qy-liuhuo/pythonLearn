def strUnion(a,b):
    sa=set(a)
    sb=set(b)

    return sa|sb

if __name__ == '__main__':
    print(strUnion("abc","cde"))
