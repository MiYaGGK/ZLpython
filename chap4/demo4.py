# _*_ coding : utf-8 _*_
# @Time : 2022/11/13 22:51
# @Author : 小仙女儿张灵
# @File : demo4
# @Project : 子木
# 双分支结构  if...else...  二选一执行
'''从键盘录入一个整数，编写程序让计算机判断是奇数还是偶数'''

num=int(input('请输入一个整数'))

# 条件判断
if num%2==0:
    print(num,'是偶数')
else:
    print(num,'是奇数')
