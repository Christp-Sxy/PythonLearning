# @author Christp
# @version 1.0
# @ClassName 3.4-mark
# @Description TODO
# @date 2022/3/7 10:47

mark = int(input("请输入分数: "))
if mark >= 90:
    grade = "优"
elif mark >= 80:
    grade = "良"
elif mark >= 70:
    grade = "良"
elif mark >= 60:
    grade = "良"
else:
    grade = "不及格"
print(str.format("成绩为: {0}", grade))
