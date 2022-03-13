# @author Christp
# @version 1.0
# @ClassName 07-sum5
# @Description TODO
# @date 2022/3/7 12:38

sum_all = 0
mark = 0
for i in range(1, 101):
    if i % 2 != 0:
        mark += 1
        if mark % 2 == 0:
            sum_all += (i * (-1))
        else:
            sum_all += i
print(sum_all)
