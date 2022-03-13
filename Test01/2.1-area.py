# @author Christp
# @version 1.0
# @ClassName area
# @Description 使用math库中的开方函数套用三角形面积公式
# @date 2022/2/27 12:39

import math
a = 3.0
b = 4.0
c = 5.0
h = (a + b + c) / 2                                        #三角形周长的一半
s = math.sqrt(h*(h-a)*(h-b)*(h-c))          #三角形面积
print(s)