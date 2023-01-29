# _*_ coding : utf-8 _*_
# @Time : 2022/11/19 2:05
# @Author : 小仙女儿张灵
# @File : demo7
# @Project : 子木
# 流程控制语句continue
'''要求输出1到50之间所有5的倍数，5,10,15,20......
   5的倍数的共同点：和5的余数为0的数都是5的倍数
   什么样的数不是5的倍数：和5的余数不为0的数都不是5的倍数
   要求使用continue实现'''
for item in range(1,51):
    if item%5==0:
        print(item)

'''使用continue'''
for item in range(1,51):
    if item%5!=0:
        continue
    print(item)
