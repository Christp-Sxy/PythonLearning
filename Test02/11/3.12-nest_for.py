# @author Christp
# @version 1.0
# @ClassName 3.12-nest_for
# @Description TODO
# @date 2022/3/7 11:21

for i in range(1, 10):
    s = " "
    for j in range(1, 10):
        s += str.format("{0} * {1} = {2} ", i, j, i * j)
    print("%s" % s)

for i in range(1, 10):
    s = " "
    for j in range(1, i+1):
        s += str.format("{0} * {1} = {2} ", i, j, i * j)
    print("%s" % s)

for i in range(1, 10):
    s = " "
    for j in range(1, 10):
        s += str.format("{0} * {1} = {2} ", j, (10 - i), j * (10-i))
    print("%s" % s)