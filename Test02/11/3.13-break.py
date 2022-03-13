# @author Christp
# @version 1.0
# @ClassName 3.13-break
# @Description TODO
# @date 2022/3/7 11:46

while True:
    s = input("请输入字符串(按Q或者q结束): ")
    if s.upper() == 'Q':
        break
    print("字符串的长度是: ", len(s))
