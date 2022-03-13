# @author Christp
# @version 1.0
# @ClassName getBonus
# @Description 使用getValue函数实现对本金的计算，其中三个变量来自input读取用户输入的本金，年利率和年数
# @date 2022/2/27 12:41

def getValue(b, r, n):                  # 创建getValue函数
    return b * ((1 + r/100)**n)         # 计算公式获取值
principle = float(input("请输入本金: "))  # 获取本金
yearRate = float(input("请输入年利率: ")) # 获取年利率
years = int(input("请输入年数: "))        # 获取年数
print(str.format("本金利率和为: {0: 2.2f}", getValue(principle, yearRate, years)))