test = [(i, j, k) for i in range(1, 101) for j in range(1, 101) for k in range(1, 101) if
        pow(i, 2) + pow(j, 2) == pow(k, 2)]
print(test)


def fib():
    a = 1
    b = 1
    yield a
    yield b
    while 1:
        yield a + b
        c = a + b
        a = b
        b = c


for fn in fib():
    if fn > 1000:
        break
    print(fn)