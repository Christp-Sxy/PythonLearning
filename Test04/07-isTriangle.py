# @author Christp
# @version 1.0
# @ClassName 06-isTriangle
# @Description TODO
# @date 2022/3/21 12:27

a = float(input("请输入三角形的边长a: "))
b = float(input("请输入三角形的边长b: "))
c = float(input("请输入三角形的边长c: "))
if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2:
            print("该三角形是直角三角形！")
        elif a == b == c:
            print("该三角形是等边三角形")
        elif a == b or c == a or b == c:
            print("该三角形是等腰三角形")
        else:
            print("该三角形不是特殊三角形")
    else:
        print("无法构成三角形")
else:
    print("无法构成三角形")