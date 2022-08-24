a=set([1,2,3,4,5])
b=set([2,4,6,8,10])

print(a | b)
print(a & b)
print(a - b)
print(a ^ b)

a.add(6)
a.pop()

print(a.isdisjoint(b))