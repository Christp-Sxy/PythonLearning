# @author Christp
# @version 1.0
# @ClassName 07-ChickenAndRabbit
# @Description TODO
# @date 2022/3/21 12:39

def method1(h, f):
    if f % 2 != 0:
        f = int(input("请输入总脚数(必须是偶数): "))
    r = (f / 2) - h  # 兔子的数量计算方程
    c = h - r  # 鸡的数量计算方程
    if r < 0 or c < 0:
        print("方程一: 无解，请重新测试")
        h = int(input("请输入总头数: "))
        f = int(input("请输入总脚数(必须是偶数): "))
        method1(h, f)
    else:
        print("方法一: 鸡: {0} 只, 兔: {1} 只".format(r, c))
        method2(h, f)

def method2(h, f):
    flag = 0
    for i in range(h):
        c = i
        r = h - c
        if 2 * c + 4 * r == f:
            print("方法二: 鸡: {0} 只, 兔: {1} 只".format(r, c))
            flag = 1
            break
    if flag == 0:
        print("方程二: 无解，请重新测试")

h = int(input("请输入总头数: "))
f = int(input("请输入总脚数(必须是偶数): "))
method1(h, f)




