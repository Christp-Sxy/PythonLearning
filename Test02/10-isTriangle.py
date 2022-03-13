# @author Christp
# @version 1.0
# @ClassName 10-isTriangle
# @Description TODO
# @date 2022/3/7 12:49

import math

a = float(input("请输入三角形的边长a: "))
b = float(input("请输入三角形的边长b: "))
c = float(input("请输入三角形的边长c: "))
if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        h = (a + b + c) / 2  # 三角形周长的一半
        area = math.sqrt(h * (h - a) * (h - b) * (h - c))  # 三角形面积
        print("三角形的三条边分别长: {:f}, {:f}, {:f}".format(a, b, c))
        print("三角形的周长为: ", a + b + c)
        print(str.format("三角形的面积 = {0}", area))
    else:
        print("无法构成三角形!")
else:
    print("无法构成三角形!")
