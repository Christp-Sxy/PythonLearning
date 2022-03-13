# @author Christp
# @version 1.0
# @ClassName 3.1-area
# @Description TODO
# @date 2022/3/7 10:38

import math

a = float("请输入三角形的边长a: ")
b = float("请输入三角形的边长b: ")
c = float("请输入三角形的边长c: ")
h = (a + b + c) / 2  # 三角形周长的一半
area = math.sqrt(h * (h - a) * (h - b) * (h - c))  # 三角形面积
print(str.format("三角形三边分别为: a = {0}, b = {1}, c = {2}"), a, b, c)
print(str.format("三角形的面积 = {0}", area))
