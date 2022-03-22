# @author Christp
# @version 1.0
# @ClassName 12-FallOut
# @Description TODO
# @date 2022/3/21 14:18

height = 100
distance = 0
for i in range(10):
    distance += height
    height = height / 2
    distance += height
print("第十次反弹时，共经过 {0} 米， 第十次反弹 {1} 米".format(distance, height))