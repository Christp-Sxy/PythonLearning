# @author Christp
# @version 1.0
# @ClassName 12-equation
# @Description TODO
# @date 2022/3/7 13:16
import math

a = float(input("请输入第一个系数a: "))
b = float(input("请输入第二个系数b: "))
c = float(input("请输入第三个系数c: "))
if a == 0 and b == 0:
    print("该方程无解")
elif a == 0 and b != 0:
    print("该方程只有一个实根: x = {0}".format(-(c / b)))
else:
    if ((b ** 2) - (4 * a * c)) > 0:
        x1 = (-(b/(2 * a))) + (math.sqrt(b * b - 4 * a * c) / (2 * a))  # 计算第一个解
        x2 = (-(b/(2 * a))) - (math.sqrt(b * b - 4 * a * c) / (2 * a))  # 计算第二个解
        print('方程{0}*x*x + {1}*x + {2} = 0的解为: x1 = {3}, x2 = {4}'.format(a, b, c, x1, x2))
    elif ((b ** 2) - (4 * a * c)) == 0:
        print("方程{0}*x*x + {1}*x + {2} = 0有两个相等的实根: x1 = x2 = {3}".format(a, b, c, -(b/(2 * a))))
    else:
        p = -(b/(2 * a))
        q = math.sqrt(4 * a * c - b * b) / (2 * a)
        print("方程{0}*x*x + {1}*x + {2} = 0有两个共轭复根: x1 = {3}+{4}i, x2 = {3}-{4}i".format(a, b, c, p, q))

