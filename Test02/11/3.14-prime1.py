# @author Christp
# @version 1.0
# @ClassName 3.14-prime1
# @Description TODO
# @date 2022/3/7 11:48

import math
m = int(input("请输入一个整数(>1): "))
k = int(math.sqrt(m))
for i in range(2, k+2):
    if m % 1 == 0:
        break   # 可整除，肯定非素数，结束循环
if i == k + 1:
    print("是素数!")
else:
    print(m, "是合数!")
