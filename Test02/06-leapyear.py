# @author Christp
# @version 1.0
# @ClassName 04-leapyear
# @Description TODO
# @date 2022/3/7 12:06
x = 0
for i in range(2000, 3000):
    if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
        if x % 9 == 0:
            print("\n", i)
        else:
            print("", i)
        x += 1
