# _*_ coding : utf-8 _*_
# @Time : 2022/11/12 20:41
# @Author : 小仙女儿张灵
# @File : demo5
# @Project : 子木
# 比较运算符
# 比较运算符布尔类型，只有True或False
# False
a,b=10,20
print('a>b吗?',a>b)
# True
print('a<b吗·?',a<b)
# True
print('a<=b吗?',a<=b)
# False
print('a>=b吗?',a>=b)
# False
print('a==b吗?',a==b)
# True
print('a!=b吗?',a!=b)


'''一个=表示赋值运算符，==表示比较运算符
   一个变量由三部分组成，标识，类型，值
   ==表示的是value，值，而不是标识
   比较对象的标识用  is
   '''

a=10
b=10
# True  说明a与b的value，值，相等
print(a==b)
# True  说明a与b的id，标识，相等
print(a is b)
# False   is not 是指值不相同
print(a is not b)

# 以下代码没学过，后期会讲到
list1=[11,22,33,44]
list2=[11,22,33,44]
# value   True
print(list1==list2)
# id   False
print(list1 is list2)
print(list1,id(list1))
print(list2,id(list2))
print(list1 is not list2)
