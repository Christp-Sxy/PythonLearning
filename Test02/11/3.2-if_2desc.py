# @author Christp
# @version 1.0
# @ClassName 3.2-if_2desc
# @Description TODO
# @date 2022/3/7 10:42

a = int(input("请输入第1个整数: "))
b = int(input("请输入第2个整数: "))
print(str.format("输入值: {0}, {1}", a, b))
if a < b:  # a和b交换
    t = a
    a = b
    b = t
print(str.format("降序值: {0}, {1}", a, b))
