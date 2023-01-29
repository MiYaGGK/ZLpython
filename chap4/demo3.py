# _*_ coding : utf-8 _*_
# @Time : 2022/11/13 22:15
# @Author : 小仙女儿张灵
# @File : demo3
# @Project : 子木
# 单分支结构  if

money=1000
# 取款金额
s=int(input('请输入取款金额'))
# 判断余额是否充足
if money>=s:    # 如果余额大于取款金额就可以进行下一步
    money1=money-s  # money1是现在的余额
    print('取款成功，余额为：',money1)
