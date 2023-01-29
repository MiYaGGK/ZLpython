# _*_ coding : utf-8 _*_
# @Time : 2022/11/19 1:45
# @Author : 小仙女儿张灵
# @File : demo6
# @Project : 子木
# 流程控制语句break
'''从键盘录入密码，最多录入3次，如果正确就结束循环'''
'''for in循环'''
# for item in range(3):
#     pwd=input('请输入密码：')
#     if pwd=='2526':
#         print('密码正确')
#         break
#     else:
#         print('密码不正确')

'''while循环'''
a=0
'''条件执行体（循环体）'''
while a<3:
    pwd=input('请输入密码')
    if pwd=='2526':
        print('密码正确')
        break
    else:
        print('密码不正确')
'''改变变量'''
a+=1

