# @author Christp
# @version 1.0
# @ClassName 12-Peaches
# @Description TODO
# @date 2022/3/21 14:06

p = 1
print("第 8 天桃子数为: 1")
for i in range(7):
    p = 2 * (p + 1)
    print("第 {0} 天桃子数为: {1}".format((7 - i), p))
