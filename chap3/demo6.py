# _*_ coding : utf-8 _*_
# @Time : 2022/11/12 21:10
# @Author : 小仙女儿张灵
# @File : demo6
# @Project : 子木
# 布尔运算

# and  并且
a,b=1,2
# True   True and True ----->True
print(a==1 and b==2)
# False  True and False ---->False
print(a==1 and b<2)
# False  False and True ----->True
print(a!=1 and b==2)
# False  False and False ---->False
print(a<1 and b>2)

# or  或者
# True  True or True ----->True
print(a==1 or b==2)
# True  True or False ----->True
print(a==1 or b>2)
# True  False or True ----->True
print(a!=1 or b==2)
# False  False or False -----False
print(a>1 or b<2)

# not  非  对布尔类型的操作数取反
f1=True
f2=False
print(not f1)
print(not f2)

# in 与 not in
s='helloworld'
# True
print('e' in s)
# False
print('f' in s)
# True
print('k' not in s)
# False
print('o' not in s)
