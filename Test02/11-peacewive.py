# @author Christp
# @version 1.0
# @ClassName 11-peacewive
# @Description TODO
# @date 2022/3/7 13:02
import math

x = float(input("请输入x的值: "))
if x >= 0:
    y = (((x ** 2) - (3 * x)) / (x + 1)) + (2 * math.pi) + math.sin(x)
    print("方法一: x = {0}, y = {1}".format(x, y))
elif x < 0:
    y = math.log(((-5) * x), math.e) + (6 * math.sqrt((abs(x) + (math.e ** 4)))) - ((x + 1) ** 3)
    print("方法一: x = {0}, y = {1}".format(x, y))

if x >= 0:
    y = (((x ** 2) - (3 * x)) / (x + 1)) + (2 * math.pi) + math.sin(x)
    print("方法二: x = {0}, y = {1}".format(x, y))
else:
    y = math.log(((-5) * x), math.e) + (6 * math.sqrt((abs(x) + (math.e ** 4)))) - ((x + 1) ** 3)
    print("方法二: x = {0}, y = {1}".format(x, y))

y = (((x ** 2) - (3 * x)) / (x + 1)) + (2 * math.pi) + math.sin(x) if x >= 0 else \
    math.log(((-5) * x), math.e) + (6 * math.sqrt((abs(x) + (math.e ** 4)))) - ((x + 1) ** 3)
print("方法三: x = {0}, y = {1}".format(x, y))
