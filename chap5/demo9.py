# _*_ coding : utf-8 _*_
# @Time : 2022/11/19 2:38
# @Author : 小仙女儿张灵
# @File : demo9
# @Project : 子木
# 嵌套循环
'''输出一个三行四列的矩形'''
for i in range(1,4):   # 行表，执行三次，一次是一行
    for j in range(1,5):
        print('*',end='\t')   # 不换行输出
    print()   # 换行

'''输出一个九行的直角三角形'''
for i in range(1,10):
    for j in range(1,i+1):
        print('*',end='\t')
    print()

'''打印九九乘法表'''
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()