# @author Christp
# @version 1.0
# @ClassName 04-CompareNumber
# @Description TODO
# @date 2022/3/21 11:05

import random

a = random.randint(0, 100)
b = random.randint(0, 100)
c = random.randint(0, 100)
x = 0

print("原始值: {0}, {1} , {2}".format(a, b, c))

if a > b:
    if b > c:
        print("(方法一)升序值: {0}>{1}>{2}".format(a, b, c))
    else:
        x = b
        b = c
        c = x
        if a > b:
            print("(方法一)升序值: {0}>{1}>{2}".format(a, b, c))
        else:
            x = a
            a = b
            b = x
            print("(方法一)升序值: {0}>{1}>{2}".format(a, b, c))

else:
    x = a
    a = b
    b = x
    if b > c:
        print("(方法一)升序值: {0}>{1}>{2}".format(a, b, c))
    else:
        x = b
        b = c
        c = x
        if a > b:
            print("(方法一)升序值: {0}>{1}>{2}".format(a, b, c))
        else:
            x = a
            a = b
            b = x
            print("(方法一)升序值: {0}>{1}>{2}".format(a, b, c))

maxNum = max(a, b, c)
minNum = min(a, b, c)
t = a + b + c - maxNum - minNum
print("(方法二)升序值: {0}>{1}>{2}".format(maxNum, t, minNum))

