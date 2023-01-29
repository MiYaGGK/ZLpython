# _*_ coding : utf-8 _*_
# @Time : 2022/11/11 15:35
# @Author : 小仙女儿张灵
# @File : demo9
# @Project : 子木
# float（）函数转换

print('--------float()函数,将其他类型转成float类型-------------')

s1='128.987'
s2='76'
ff=True
s3='hello'
i=98
print(type(s1),type(s2),type(ff),type(s3),type(i))

# str转float
print(float(s1),type(float(s1)))

#
print(float(s2),type(float(s2)))

print(float(ff),type(float(ff)))

# 字符串中的数据如果是非数字串，则不允许转换
# print(float(s3),type(float(s3)))

print(float(i),type(float(i)))


