# @author Christp
# @version 1.0
# @ClassName 14-CalculateSn
# @Description TODO
# @date 2022/3/21 14:30
import random

n = random.randint(1, 10)
t1 = 1
sn = 1
for i in range(n-1):
    t1 = t1 * 10 + 1
    sn += t1
print("n = {0}, Sn = {1}".format(n, sn))