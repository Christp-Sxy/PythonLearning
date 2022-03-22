# @author Christp
# @version 1.0
# @ClassName 09-Calculation1
# @Description TODO
# @date 2022/3/21 13:16

x = float(input("请输入x: "))
result = 1
for i in range(500):
    a = x**(i+1)
    for j in range(i + 1):
        a = a / (j+1)
    result = result + a
    if a < 0.000001:
        break
print("Pow(e, x) = {0}".format(result))