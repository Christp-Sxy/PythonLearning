# @author Christp
# @version 1.0
# @ClassName getReturnValue
# @Description input读取用户输入的本金，年利率和年数，用amount记录计算值
# @date 2022/2/27 12:41

principle = float(input("请输入本金: "))     # 获取本金
yearRate = float(input("请输入年利率: "))     # 获取年利率
years = int(input("请输入年数: "))           # 获取年数
amount = principle * ((1 + yearRate/100)**years)    # 计算公式获取值
print(str.format("本金利率和为: {0: 2.2f}", amount))