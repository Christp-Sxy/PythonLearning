# @author Christp
# @version 1.0
# @ClassName 13-factorial
# @Description TODO
# @date 2022/3/7 13:46
while True:
    n = int(input("请输入非负整数n: "))
    if n < 0:
        print("请输入大于0的数")
        continue
    elif n == 0:
        print("0! = 1")
        break
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        print("for循环: {0}! = {1}".format(n, result))
        x = 1
        result = 1
        while x < n + 1:
            result *= x
            x += 1
        print("for循环: {0}! = {1}".format(n, result))
        break
