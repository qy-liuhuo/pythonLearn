import random

secret = random.randint(1, 100)
print("猜1-100内的数字，共六次机会")
tries = 1
while tries<=6:
    guess = int(input("请输入：" ))
    if guess == secret:
        print("猜对了")
        break
    elif guess > secret:
        print("猜大了")
    else:
        print("猜小了")
    tries += 1
if guess != secret:
    print("没机会了")

