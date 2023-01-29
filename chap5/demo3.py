# _*_ coding : utf-8 _*_
# @Time : 2022/11/19 0:22
# @Author : 小仙女儿张灵
# @File : demo3
# @Project : 子木
# 计算1到100之间的偶数和
sum=0   # sum用于存储偶数和
'''初始化变量'''
a=1
'''条件判断'''
while a<=100:
    '''条件执行体（求和）'''
    # 条件判断是否是偶数
    if not bool(a%2):                      # if a%2==0:
        sum+=a
    '''改变变量'''
    a+=1
print('1到100之间的偶数和',sum)

