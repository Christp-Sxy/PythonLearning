# @author Christp
# @version 1.0
# @ClassName 3.9-for_sum_1_100
# @Description TODO
# @date 2022/3/7 11:03

sum_odd = 0
sum_even = 0
for i in range(1, 101):
    if i % 2 != 0:  # 奇数
        sum_odd += i    # 奇数和
    else:   # 偶数
        sum_even += i   # 偶数和
print("1 ~ 100中所有的奇数和为: ", sum_odd)
print("1 ~ 100中所有的偶数和为: ", sum_even)