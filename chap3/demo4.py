# _*_ coding : utf-8 _*_
# @Time : 2022/11/12 20:15
# @Author : 小仙女儿张灵
# @File : demo4
# @Project : 子木
# 赋值运算符
# 运算顺序：从右到左
i=3+4
print(i)

# 链式赋值
a=b=c=20
print(a,id(a))
print(b,id(b))
print(c,id(c))

# 参数赋值
a=20
# 相当于a+=a+50
a+=50
print(a)
# a=a-30
a-=30
print(a)
# a=a*5
a*=5
print(a)
# a=a/3
a/=3
print(a)
# a=a//6
a//=6
print(a)
# a=a%3
a%=3
print(a)

# 系列解包赋值
a,b,c=20,30,40
print(a,b,c)
# a,b=20,30,40  报错，左右变量个数和值的个数不对应

# 交换两个变量的值
a,b=10,20
print('交换之前',a,b)
a,b=b,a
print('交换之后',a,b)

