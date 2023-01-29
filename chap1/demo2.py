# _*_ coding : utf-8 _*_
# @Time : 2022/11/2 21:47
# @Author : 小仙女儿张灵
# @File : demo2
# @Project : 子木

# \ + 转义功能的首字母  ,-->newline的首字母表示换行
print('hello\nworld')

# tab是四个空格为一格
print('hello\tworld')
print('helloooo\tworld')

# world将Hello进行了覆盖
print('hello\rworld')

# \b是一个退格，将o退没了
print('hello\bworld')

# 反斜杠
print('http\\\\www.baidu.com')
print('老师说：\'大家好\'')

# 原字符：不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r或R
print(r'hello\nworld')
# 注意事项：原始字符串的最后一个字符不能是反斜杠，双反斜杠可以
print(r'hello\nworld\')
print(r'hello\nworld\\')
