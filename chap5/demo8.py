# _*_ coding : utf-8 _*_
# @Time : 2022/11/19 2:22
# @Author : 小仙女儿张灵
# @File : demo8
# @Project : 子木
# else 语句
# for irem in range(3):
#     pwd=input('请输入密码')
#     if pwd=='1516':
#         print('密码正确')
#         break
#     else:
#         print('密码错误')
# else:
#     print('对不起，三次密码均输入错误')

'''while'''
a=0
while a<3:
    pwd=input('请输入密码')
    if pwd=='3344':
        print('密码正确')
        break
    else:
        print('密码不正确')
    '''改变变量'''
    a+=1
else:
    print('三次密码均输入错误')
