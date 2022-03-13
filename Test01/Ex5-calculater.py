# @author Christp
# @version 1.0
# @ClassName calculater
# @Description 使用math库中的开方函数套用方程求解公式
# @date 2022/2/27 12:38

import math
a = 1; b = -10; c = 16                              # 进行赋值
x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)  # 计算第一个解
x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)  # 计算第二个解
print('方程x*x - 10x + 16 = 0的解为: x1 = {0}, x2 = {1}'.format(x1, x2))
