# _*_ coding : utf-8 _*_
# @Time : 2022/11/19 1:06
# @Author : 小仙女儿张灵
# @File : demo4
# @Project : 子木
# for in 循环
for item in 'Python':     # 第一次取出来的是P，将P赋值给item，将item·的值输出
    print(item)

#range（）产生一个整数序列，这也是一个可迭代对象
for i in range(10):
    print(i)

# 如果在循环体中不需要使用到自定义变量，可将自定义变量写为“_”
for _ in range(3):  #range()函数可以用做for循环的次数
    print('无关风月，我题序等你回')

'''用for循环计算1到100的偶数和'''
sum=0  #用于存储偶数和
for item in range(1,101):
    if item%2==0:
        sum+=item
print('1到100之间的偶数和',sum)

