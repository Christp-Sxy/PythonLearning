# @author Christp
# @version 1.0
# @ClassName 14-gongyueshu
# @Description TODO
# @date 2022/3/7 14:15
import random


def compare(a, b):
    if b > a:
        t = a
        a = b
        b = t
    arr = [a, b]
    return arr


def result(a, b):
    if a % b == 0:
        return b
    else:
        arr = compare(b, a % b)
        return result(arr[0], arr[1])


m = random.randint(0, 100)
n = random.randint(0, 100)
print("整数1为: {0}, 整数2为: {1}".format(m, n))
arr1 = compare(m, n)
answer = result(arr1[0], arr1[1])
print("最大公约数为: {0}, 最小公倍数为: {1}".format(answer, ((m * n) / answer)))