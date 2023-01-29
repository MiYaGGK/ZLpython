# _*_ coding : utf-8 _*_
# @Time : 2022/11/19 1:30
# @Author : 小仙女儿张灵
# @File : demo5
# @Project : 子木
# for in 练习题_100到999之间的水仙花数
for item in range(100,1000):
    ge=item%10
    shi=item//10%10
    bai=item//100
    # print(bai,shi,ge)
    # 判断
    if ge**3+shi**3+bai**3==item:
      print(item)
