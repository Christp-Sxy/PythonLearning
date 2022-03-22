# @author Christp
# @version 1.0
# @ClassName 05-Salary
# @Description TODO
# @date 2022/3/21 11:46

salary = float(input("请输入有固定工资收入的党员的月工资："))
f = 0

if salary <= 3000:
    print("月工资 = {0}，缴纳党费 = {1}".format(salary, salary*0.005))
elif salary <= 5000:
    print("月工资 = {0}，缴纳党费 = {1}".format(salary, salary*0.01))
elif salary <= 10000:
    print("月工资 = {0}，缴纳党费 = {1}".format(salary, salary*0.015))
else:
    print("月工资 = {0}，缴纳党费 = {1}".format(salary, salary*0.02))