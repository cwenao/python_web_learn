# 练习题来自于菜鸟教程
# http://www.runoob.com/python/python-exercise-example1.html

#################################################################################

# 1. 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 思路：使用yield将函数作为生成器

d = [1,2,3,4]

def assemblyNum(num,targetD,length):
    temp = num

    for i in range(len(targetD)):
        num = temp*10+targetD[i]
        if length==3:
            yield num
        elif length<3:
            for x in assemblyNum(num,targetD[:i]+targetD[i+1:],length+1):
                yield x


targetD = list(assemblyNum(0,d,1))

print(targetD)


#################################################################################

# 2. 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？

#思路： 奖金是根据利润走，且为区间为准；则按提成--利润对应关系



superprofit = [1000000,600000,400000,200000,100000,0]

royaltyRate = [0.01,0.015,0.03,0.05,0.075,0.1]



def calculateProfit(num,sumnum,profitList,rateList):
    if num < 0:
        return 0
    for i,v in enumerate(profitList):
        if (num - v) >0:
            sumnum  = sumnum + (num - v)*rateList[i]
            yield (num - v)*rateList[i]
            num = v


#profit = int(input())

profit = 120000
print(list(calculateProfit(profit,0,superprofit,royaltyRate)))


# 3. 一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？
# 思路：假设为x 则 x+i与x+268都可以开平方
# 安装NumPy科学计算库：pip install NumPy

import numpy
def getSqrt(endNum):

    for x in range(endNum):
        d1 = int(numpy.sqrt(x+100))
        d2 = int(numpy.sqrt(x+268))

        if((numpy.square(d1) == (x+100)) and (numpy.square(d2) == (x+268))):
            yield x

print(list(getSqrt(10000)))


# 4. 输入某年某月某日，判断这一天是这一年的第几天？
# 思路: 内置datetime进行日期格式转换与输出
# 如果手写则需要判断闰月

from datetime import datetime

#inputtime = input()

def getTheDaythForInput(inputtime):

    dateStr = datetime.strptime(inputtime, '%Y-%m-%d')

    date = datetime.date(dateStr)

    print(date.strftime('%j'))

# getTheDaythForInput(inputtime)

# 5. 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
# 思路：利用list的sort

#lstr = input()
lstr = '1,3,5,2'
l = lstr.split(",")
l.sort()

print(l)

# 6. 题目：斐波那契数列

def fib(max):

    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n= n+1
    return 'done'

f = fib(8)

for n in f:
    print(n)

# 7题目：将一个列表的数据复制到另一个列表中。

a= [1,2,3,4,5,6]
b=a[:]

print(b)

# 8.题目：输出 9*9 乘法口诀表。
def multiTable():
    for x in range(1,10):
        for y in range(1,x+1):
            print("%d*%d=%2d" % (x,y,x*y),end=" ")
        print(" ")

multiTable()

# 9. 暂停一秒输出

import time
def sleep_sec():
    for n in range(0,10):
        print(n)
        time.sleep(1)

sleep_sec()