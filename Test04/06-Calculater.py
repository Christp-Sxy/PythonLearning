# @author Christp
# @version 1.0
# @ClassName 06-Calculater
# @Description TODO
# @date 2022/3/21 11:55
def calculater(x, y, a):
    if a == '+':
        print("{0} + {1} = {2}".format(x, y, (x + y)))
    elif a == '-':
        print("{0} - {1} = {2}".format(x, y, (x - y)))
    elif a == '*':
        print("{0} * {1} = {2}".format(x, y, (x * y)))
    elif a == '/':
        if y == 0:
            print("分母=0，零除异常")
            x = float(input("请输入操作数x: "))
            y = float(input("请输入操作数y: "))
            a = input("请输入操作符: ")
            calculater(x, y, a)
        else:
            print("{0} / {1} = {2}".format(x, y, (x / y)))
    else:
        print("对不起，您输入有误，请重试\n")
        x = float(input("请输入操作数x: "))
        y = float(input("请输入操作数y: "))
        a = input("请输入操作符: ")
        calculater(x, y, a)


x = float(input("请输入操作数x: "))
y = float(input("请输入操作数y: "))
a = input("请输入操作符: ")
calculater(x, y, a)

