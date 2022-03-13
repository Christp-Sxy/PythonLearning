# @author Christp
# @version 1.0
# @ClassName getAge
# @Description 使用input方法读取控制台中输入的内容并通过print进行打印
# @date 2022/2/27 12:39

import datetime

sName = str(input("请输入您的姓名: "))             # 读取姓名
birth = int(input("请输入您的出生年份: "))          # 读取出生年月
age = datetime.date.today().year - birth        # 调用datetime中的方法获取时间
print("您好! {0}。您{1}岁了。".format(sName, age))
