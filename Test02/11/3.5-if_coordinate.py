# @author Christp
# @version 1.0
# @ClassName 3.5-if_coordinate
# @Description TODO
# @date 2022/3/7 10:50

x = int(input("请输入x的坐标: "))
y = int(input("请输入y的坐标: "))
if x == 0 and y == 0:
    print("位于原点")
elif x == 0:
    print("位于y轴")
elif y == 0:
    print("位于x轴")
elif x > 0 and y > 0:
    print("位于第一象限")
elif x < 0 and y > 0:
    print("位于第二象限")
elif x < 0 and y < 0:
    print("位于第三象限")
else:
    print("位于第四象限")