# @author Christp
# @version 1.0
# @ClassName string
# @Description TODO
# @date 2022/3/21 10:06

print("1".center(20))                     # 1行20个字符，居中对齐
print(format("121", "^20"))         # 1行20个字符，居中对齐
print(format("12321", "^20"))     # 1行20个字符，居中对齐
print("1".rjust(20,"*"))                 # 1行20个字符，右对齐，加*号
print(format("121", "*>20"))       # 1行20个字符，右对齐，加*号
print(format("12321", "*>20"))   # 1行20个字符，右对齐，加*号
