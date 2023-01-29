# _*_ coding : utf-8 _*_
# @Time : 2022/11/11 14:39
# @Author : 小仙女儿张灵
# @File : demo8
# @Project : 子木
# 数据类型转换

name='张三'
age=20

# name与age数据类型不相同
print(type(name),type(age))

# 当str类型与int类型进行连接时报错，解决方案是类型转换
# print('我叫'+name+'今年'+age+'岁')

# 将int类型通过str()函数转成str类型
print('我叫'+name+'今年'+str(age)+'岁')

print('------------str()将其他类型转成str类型')
a=10
b=198.8
c=False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))

print('-----------int()将其他类型转为int类型-------')
s1='128'
f1=98.7
s2='78.77'
ff=True
s3='hello'
print(type(s1),type(f1),type(s2),type(ff),type(s3))


# 将str转成int类型，前提是字符串为数字串(只能为数字串且是整数)
print(int(s1),type(int(s1)))

# 将str转成int类型报错，是因为字符串中有小数串
# print(int(s2),type(int(s2)))

# 将str转成int类型报错，是因为字符串中有文字串
# print(int(s3),type(int(s3)))

# 将float转成int类型，但只截取整数部分，舍掉小数部分
print(int(f1),type(int(f1)))

# 将bool转成int类型
print(int(ff),type(int(ff)))