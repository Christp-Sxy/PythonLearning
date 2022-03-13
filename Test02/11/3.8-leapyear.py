# @author Christp
# @version 1.0
# @ClassName 3.8-leapyear
# @Description TODO
# @date 2022/3/7 10:59

y = int(input("请输入想查询的年份: "))
if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
    print("是闰年")
else:
    print("不是闰年")
