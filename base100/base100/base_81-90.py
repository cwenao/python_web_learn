#81. 题目：809*??=800*??+9*??+1 其中??代表的两位数,8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，及809*??后的结果。
#


#82 题目：八进制转换为十进制


def convert8to10(n):
    lenN = len(str(n))
    sumN = 0

    for i in range(lenN):
        sumN += 8 ** i * int(str(n)[lenN-1-i])

    print('this is the 8 to 10 : %d' % sumN)

convert8to10(122)


#83. 题目：求0—7所能组成的奇数个数。


def odd_num(n):
    if n == 0:
        return 1
    elif n == 1:
        return 7
    else:
        return odd_num(n-1) * 8


def count_odd_num():
    l = []

    for i in range(1,9):
        l.append(odd_num(i-1) * 4)

    print(sum(l))

count_odd_num()


#84 题目：连接字符串。


def join_str(split, array):
    print('this is to join the str: ', split.join(array))

x = ['a', 'b', 'dd', 'good', 'lucky', 'day']

join_str(',', x)


#85 题目：输入一个正整数，然后判断最少几个 9 除于该数的结果为整数。


def numerator(n):
    x = 9

    while(True):
        if x % n == 0:
            print('this is the numerator: %d' % x)
            break

        x = x * 10 + 9


numerator(13)


#87. 题目：回答结果（结构体变量传递）。


class GoodDay:
    m = 0
    n = 0


def struct_do(goodDay):
    goodDay.m = 20
    goodDay.n = 50


x = GoodDay()
x.m = 100
x.n = 20

print('this is the x.m %d and x.n %d' % (x.m, x.n))

struct_do(x)

print('this is the x.m %d and x.n %d' % (x.m, x.n))


# 88. 题目：读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。


def print_start(n):
    print(n * '*')

print_start(22)


# 89. 题目：某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，
# 加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。


def encode_num(n):
    x = str(n)
    n = ''
    for i in range(len(x)):
        n += str((int(x[i]) + 5) % 10)
    return int(n[::-1])

print(encode_num(1234))


# 90 题目：列表使用实例。


def do_list():
    testList = ['10086', '小姐姐', '你好', '工号', [1, 2, 3, 4, 5]]

    print('this is the len to list : %d ' % len(testList))

    print('this is the order read the element for list : ', testList[1:])

    testList.append('大家好')

    print('add the element to list: ', testList)

    print('pop the last element : ', testList.pop(-1))

    x = testList.pop(-1)

    print('pop the last element : ', x)

do_list()