# @author Christp
# @version 1.0
# @ClassName 3.7-if_3desc
# @Description TODO
# @date 2022/3/7 10:55

a = int(input("请输入第1个整数: "))
b = int(input("请输入第2个整数: "))
c = int(input("请输入第3个整数: "))
if a < b:
    t = a
    a = b
    b = t
if a < c:
    t = a
    a = c
    c = t
if b < c:
    t = b
    b = c
    c = t
print(str.format("降序值: {0}, {1}, {2}", a, b, c))
