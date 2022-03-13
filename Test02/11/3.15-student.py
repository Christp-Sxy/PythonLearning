# @author Christp
# @version 1.0
# @ClassName 3.15-student
# @Description TODO
# @date 2022/3/7 14:57

num = 0;
scores = 0;  # 初始化学生人数和成绩和
while True:
    s = input('请输入学生成绩（按Q或q结束）：')
    if s.upper() == 'Q':
        break
    if float(s) < 0:  # 成绩必须>=0
        continue
    num += 1  # 统计学生人数
    scores += float(s)  # 计算成绩之和
