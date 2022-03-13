# @author Christp
# @version 1.0
# @ClassName 3.10-while_sum
# @Description TODO
# @date 2022/3/7 11:10

i = 1
sum_all = 0
sum_odd = 0
sum_even = 0
while i <= 100:
    sum_all += i
    if i % 2 != 0:  # 奇数
        sum_odd += i    # 奇数和
    else:   # 偶数
        sum_even += i   # 偶数和
    i += 1
print("和 = %d, 奇数和 = %d, 偶数和 = %d" % (sum_all, sum_odd, sum_even))