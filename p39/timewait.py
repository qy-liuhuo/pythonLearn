import time

timeStart=time.time()

num=1

for i in range(1,101):
    num=num*i

timeEnd=time.time()

print(timeEnd-timeStart)