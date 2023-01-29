# _*_ coding : utf-8 _*_
# @Time : 2022/11/30 19:52
# @Author : 小仙女儿张灵
# @File : demo10
# @Project : 子木
# 二重循环中的break与continue
'''流程控制语句break与continue在二重循环中的使用'''
for i in range(5):        #代表外层循环要执行五次
    for j in range(1,10):
        if j%2==0:
            # break
            continue
        print(j,end='\t')
    print()
    