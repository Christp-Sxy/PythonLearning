# @author Christp
# @version 1.0
# @ClassName while_e
# @Description TODO
# @date 2022/3/7 11:13

i = 1
e = 1
t = 1
while 1 / t >= pow(10, -6):
    t *= i
    e += 1 / t
    i += 1
print("e = ", e)