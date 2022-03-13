# @author Christp
# @version 1.0
# @ClassName 3.14-prime2
# @Description TODO
# @date 2022/3/7 11:52

import math

m = int(input("请输入一个整数(>1): "))
k = int(math.sqrt(m))
flag = True
i = 2
while i <= k and flag:
    if m % i == 0:
        flag = False  # 可整除，肯定非素数，结束循环
    else:
        i += 1
if flag:
    print(m, "是素数!")
else:
    print(m, "是合数!")
