
try:
    a=int(input())
    b=int(input())
    print(a/b)
except ValueError :
    print("输入类型错误")
except ZeroDivisionError:
    print("除数为零")