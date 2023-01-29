# _*_ coding : utf-8 _*_
# @Time : 2022/11/13 21:49
# @Author : 小仙女儿张灵
# @File : demo2
# @Project : 子木
# 测试对象的bool值

print('--------------以下对象的布尔值都为False-------------------')
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(''))
print(bool(""))
print(bool([]))    # 空列表
print(bool(list()))   # 空列表
print(bool(tuple()))  # 空元祖
print(bool(()))    # 空元祖
print(bool({}))    # 空字典
print(bool(dict())) # 空字典
print(bool(set()))  # 空集合


print('--------------其他对象的布尔值均为True-------------------------')
print(bool(18))
print(bool(True))
print(bool('helloworld'))