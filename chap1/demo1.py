# _*_ coding : utf-8 _*_
# @Time : 2022/10/21 17:41
# @Author : 小仙女儿张灵
# @File : demo1
# @Project : 子木
# 输出函数print


# 可以输出数字（输出到显示器上）
print(520)
print(98.5)

# 可以输出字符串（输出到显示器上）
print('helloworld')


# 含有运算符的表达式(输出到显示器上)
# 3和1叫作操作数，+叫作运算符，含有操作数和运算符的称作表达式
# print()函数会输出表达式的结果
print(3+1)


# 将数据输出到文件中
# 注意点  1.所指定的盘符必须存在  2.使用file=  的形式
# a+的意思是如果文件不存在就创建，存在就在文件内容的后面追加
fp=open('E:/text.txt','a+')
print('helloworld',file=fp)
fp.close()


# 不进行换行输出（输出内容在一行当中）
print('hello','world','python')