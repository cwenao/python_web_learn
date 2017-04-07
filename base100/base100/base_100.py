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
    for n in range(0,2):
        print(n)
        time.sleep(1)

# sleep_sec()

# 10. 暂停一秒输出，并格式化当前时间


def sleep_and_format():
    for n in range(0,10):
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        time.sleep(1)


# sleep_and_format()

# 11. 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
# 题目实际是斐波那契数列： 1,1,2,3,5,8

def fib_seq(month):
    n,a,b = 0,0,1
    while n < month:
        yield b
        a,b = b,a+b
        n=n+1

    return 'done'

# f = fib_seq(10)
#
# for n in f:
#     print(n)

# 12. 判断101-200之间有多少个素数，并输出所有素数。
# 素数的判别方法,改成从2开始输出素数

#判断是否是素数
def not_divisible(n):
    return lambda x: x%n>0

#每次生成下一个数
def oddIter():
    n=1
    while True:
        n=n+2
        yield n

def primes():
    yield 2
    odd = oddIter()
    while True:
        n = next(odd)
        yield n
        odd = filter(not_divisible(n),odd)

# for i in primes():
#     if i<100:
#         print(i)
#     else:
#         break


# 13 题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，
# 其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

def nextNum():
    n = 99
    while True:
        n = n+1
        if (n>1000):
            return 'done'
        yield n

def isnarcissitic():
    return lambda x : (pow(int(str(x)[0]),3)+pow(int(str(x)[1]),3)+pow(int(str(x)[2]),3)) == x

def narcissitics():
    nextN = nextNum()
    while True:
        nar = filter(isnarcissitic(),nextN)
        yield next(nar)


# for i in narcissitics():
#    print(i)

# 14. 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5

def reduceNum(n):
    for x in range(2,n+1):
        while n % x == 0:
            yield x
            n = n/x
        x=x+1

r = reduceNum(99)

for x in r:
    print(x)

# 15. 题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

scores = [90,60,0]
g = ['A','B','C']

def compareTo(students):
    for x in students:
        for k,v in enumerate(scores):
            if x >= v:
                yield g[k]
                break

stu = [50,30,80,100]

f = compareTo(stu)

for x in f:
    print(x)


# 16. 题目：输出指定格式的日期

print(datetime.today().strftime('%d/%m/%Y'))

# 星期
print(datetime.now().strftime('%a'))
print(datetime.now().strftime('%A'))

# 星期中的第几天
print(datetime.now().strftime('%w'))

# 月份
print(datetime.now().strftime('%b'))
print(datetime.now().strftime('%B'))

# 本地时间日期
print(datetime.now().strftime('%c'))

# 显示第几天
print(datetime.now().strftime('%d'))

# 小时 24 /12
print(datetime.now().strftime('%H'))
print(datetime.now().strftime('%I'))

# 一年中的第几天
print(datetime.now().strftime('%j'))

# 第几周： 星期天为第一天/星期一为第一天

print(datetime.now().strftime('%U'))
print(datetime.now().strftime('%W'))

#  格式化输入的字符串
print(datetime.strptime('2017-9-22 03:02:12','%Y-%m-%d %H:%M:%S'))

# 17. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数

counts=[0,0,0,0]

def countWords(words):
    if words == None:
        return 0
    for x in words:
        if x.isalpha():
            counts[0] = counts[0]+1
        elif x.isspace():
            counts[1] = counts[1]+1
        elif x.isdigit():
            counts[2] = counts[2]+1
        else:
            counts[3] = counts[3]+1
    return counts
# inputwords = input()
#
# f = countWords(inputwords)
#
# for s in f:
#     print(s)

#18 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。

def multipleNum(primitive,num,count):
    while count>0:
        yield num
        num = (num*10+primitive)
        count = count-1


f = multipleNum(2,2,3)

sumx = 0
for x in f:
    print('this is x %d ' % (x))
    sumx = sumx+x
    print('this is sumx %d ' % (sumx))



#19 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

def factorNum(num):

    for x in range(2,num+1):
        nn = 0
        for i in range(1,x):
            if x % i ==0:
                nn= nn+i
        if nn == x:
            yield nn



f = factorNum(1000)

for m in f:
    print(m)


#20 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

down =[]
kick_back = []

def calculate_distance(frequency,initHeight):
    n=0
    while n< frequency:
        down.append(initHeight)
        initHeight = initHeight/2
        kick_back.append(initHeight)
        n = n+1

calculate_distance(10,100)

print('total distance: %s ' % format(sum(down)))
print('total kick_back: %s ' % format(kick_back[-1]))

# 21 猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。


def sumFirstDay(days):
    n = 1
    while days>0:
        yield n
        n = (n+1)*2
        days = days-1

f= sumFirstDay(10)

for x in f:
    print('this is the day %d' % x)


# 22.两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
# 已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

for i in range(ord('x'),ord('z') + 1):
    for j in range(ord('x'),ord('z') + 1):
        if i != j:
            for k in range(ord('x'),ord('z') + 1):
                if (i != k) and (j != k):
                    if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
                        print('order is a -- %s\t b -- %s\tc--%s' % (chr(i),chr(j),chr(k)))


# 23 打印出如下图案（菱形）:
#*
#***
#*****
#*******
#*****
#***
#*
#思路 stdout

from sys import stdout

def printImage(num):
    printNum = int(num / 2)
    for i in range(printNum +1):
        for j in range(printNum + 1 -i):
            stdout.write(' ')

        for k in range(2*i+1):
            stdout.write('*')
        print()

    for i in range(printNum):
        for j in range(i + 2):
            stdout.write(' ')
        for k in range(printNum + 2 -2*i):
            stdout.write('*')
        print()

printImage(7)

#24 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

l =[]
def elementSum(endNum,initE,initD):
    for i in range(1,endNum+1):
        yield initE / initD
        initE,initD = initE+initD,initE


l = elementSum(20,1.0,2.0)
s=0.0
for x in l:
    s = s+x
    print(s)


#25 求1+2!+3!+...+20!的和
#map的用法

l= range(1,21)

def sumFactor(num):

    r = 1

    for x in range(1,num+1):
        r *= x
    return r

print('this is the sumfor factor %s' % sum(map(sumFactor,l)))


#26 利用递归方法求5!利用递归方法求5!

def factNum(num):

    sumN  =0
    if num == 0:
        sum =1
    else:
        sum = num * factNum(num-1)

    return sumN

factNum(5)


# 27 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

def outprint(inputstr,lengh):
    if lengh == 0:
        return
    print(inputstr[lengh-1])
    outprint(inputstr, lengh-1)

# s =  input('please input the string: ')
#
# l= len(s)
#
# outprint(s,l)

# 28：有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。
# 问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。
# 问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？

def ageNum(n):
    if n == 1:
        age = 10
    else:
        age = ageNum(n-1) +2

    return age

print(ageNum(5))


#29 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

def resolve(n):
    nl = len(str(n))
    dec = pow(10,nl-1)
    print('this is the num: ',nl)
    while nl > 0:
        yield int(n / dec)
        n = n % dec
        dec = int(dec/10)
        nl = nl - 1


for x in resolve(12345678):
    print(x)

# 30 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

def plalindrome(num):
    m = str(num)
    for x in range(int(len(m)/2)):
        if m[x] != m[-x-1]:
            return False
    return m


xx = plalindrome(123211)

print('this is the plaidrome: ',xx)


# 31 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
# 这个题目改为if elif else 的应用

def ifelif(doSomething):
    if doSomething == 'a':
        print('this is a -------------->')
    elif doSomething == 'b':
        print('this is b --------------->')
    else:
        print('this is nothing ----------------->')

ifelif('b')


# 32 按相反的顺序输出列表的值。

def opposite(num):
    for x in num[::-1]:
        print('this is the x : ',x)

a = ['a','b','c']

opposite(a)

# 33 题目：按逗号分隔列表。

L = ['a','b','c']

s1 = ','.join(str(x) for x in  L)

print(s1)