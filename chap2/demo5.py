# _*_ coding : utf-8 _*_
# @Time : 2022/11/11 11:56
# @Author : 小仙女儿张灵
# @File : demo5
# @Project : 子木
# 浮点类型
a=3.14159
print(a,type(a))

n1=1.1
n2=2.2
n3=2.1
print(n1+n3)

from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))