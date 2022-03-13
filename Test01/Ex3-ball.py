# @author Christp
# @version 1.0
# @ClassName ball
# @Description 使用math库中的PI常量带入球的公式求值
# @date 2022/2/27 12:39

import math                                 # 调用库
r = float(input("请输入圆的半径r："))          # 读取用户输入半径
area = 4 * math.pi * (r**2)                 # 计算表面积
volume = (4 * math.pi * (r**3)) / 3         # 计算体积
print(str.format("球的表面积为: {0: 2.2f}, 体积为: {1: 2.2f}", area, volume))