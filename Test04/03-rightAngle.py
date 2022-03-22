# @author Christp
# @version 1.0
# @ClassName 03-rightAngle
# @Description 输入两条直角边，打印相应的面积以及周长
# @date 2022/3/21 10:14

import math

a = float(input("请输入三角形的一条直角边长a（>0）: "))
b = float(input("请输入三角形的另一条直角边长b（>0）: "))
c = math.sqrt(a**2 + b**2)

p = a + b + c
area = a * b / 2
A = round(math.asin(b / c) * 180 / math.pi, 0)
B = round(math.asin(a / c) * 180 / math.pi, 0)

print("三角形的三条边分别长: {:1.1f}, {:1.1f}, {:1.1f}".format(a, b, c))
print("三角形的周长 ={:1.1f}，面积＝ {:1.1f}".format(p, area))
print("三角形两个锐角的度数分别为：{:1.1f} 和{:1.1f}".format(A, B))
