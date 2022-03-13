# @author Christp
# @version 1.0
# @ClassName 03-sum3
# @Description TODO
# @date 2022/3/7 12:03

sum_all = 0
for i in range(1, 101):
    if i % 2 != 0:
        sum_all += i
print(sum_all)
