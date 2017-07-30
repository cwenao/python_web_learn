#61.题目：打印出杨辉三角形（要求打印出10行如下图）。　　
#利用生成器解决

def triangle():
    x = [1]
    while True:
        yield x
        #zip: 添加0组成元组
        x = [sum(i) for i in zip([0]+x, x+[0])]

num = 0
for x in triangle():
    print(x)
    num += 1
    if num == 10:
        break

#62.题目：查找字符串。

str1 = 'abcdedf'
str2 = 'ded'

print('The find index is %d ' % str1.find(str2))

#63.题目：画椭圆。　

from tkinter import *

def draw_oval():
    x = 360
    y = 160
    top = y-30
    bottom = y-30

    canvas = Canvas(width=400, height=600, bg='white')

    for i in range(20):
        canvas.create_oval(250-top, 250-bottom, 250+top, 250+bottom)
        top -= 5
        bottom += 5
    canvas.pack()
    mainloop()

#draw_oval()

#64. 利用ellipse 和 rectangle 画图。


def draw_rectangle():
    canvas = Canvas(width=400, height=600, bg='white')

    for i in range(num):
        canvas.create_rectangle(20 - 2 * i, 20-2 * i, 10 * (i+2), 10 * (i+2))

    canvas.pack()
    mainloop()

#draw_rectangle()

#65. 一个最优美的图案。
#抄的demo


import math


class PTS:
    def __init__(self):
        self.x = 0
        self.y = 0
points = []


def line_to_demo():

    screenx = 400
    screeny = 400
    canvas = Canvas(width = screenx,height = screeny,bg = 'white')

    AspectRatio = 0.85
    MAXPTS = 15
    h = screeny
    w = screenx
    xcenter = w / 2
    ycenter = h / 2
    radius = (h - 30) / (AspectRatio * 2) - 20
    step = 360 / MAXPTS
    angle = 0.0
    for i in range(MAXPTS):
        rads = angle * math.pi / 180.0
        p = PTS()
        p.x = xcenter + int(math.cos(rads) * radius)
        p.y = ycenter - int(math.sin(rads) * radius * AspectRatio)
        angle += step
        points.append(p)
    canvas.create_oval(xcenter - radius,ycenter - radius,
                       xcenter + radius,ycenter + radius)
    for i in range(MAXPTS):
        for j in range(i,MAXPTS):
            canvas.create_line(points[i].x,points[i].y,points[j].x,points[j].y)

    canvas.pack()
    mainloop()

#line_to_demo()


#66. 题目：输入3个数a,b,c，按大小顺序输出。

def swap(x1, x2):
    return x2, x1

m1 = 50
m2 = 100

print('The value is x1 %d, x2 %d' % swap(m1, m2))


#67. 题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。

def swap_max_first(array):
    maxNum = 0
    for i in range(len(array)-1):
        if array[maxNum] < array[i]:
            maxNum = i
    array[0], array[maxNum] = array[maxNum], array[i]

maxArray = [1,3,5,6,9,11,8,7]
swap_max_first(maxArray)

# for x in maxArray:
#     print(x)

#68. 题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
# 循环数组


def rotation_array_by_reversal(array, start, end):
    while start < end:
        tmp = array[start]
        array[start] = array[end]
        array[end] = tmp
        start += 1
        end -= 1


def rotation_array(array, index):

    lenx = len(array)
    rotation_array_by_reversal(array, 0, index-1)
    rotation_array_by_reversal(array, index, lenx-1)
    rotation_array_by_reversal(array, 0, lenx-1)

rotation_array(maxArray, 2)

# for rex in maxArray:
#     print(rex)


#69. 题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。


def rotation_remove(array):
    i = 1
    while len(array) > 1:
        if i % 3 ==0:
            array.pop(0)
        else:
            array.insert(len(array), array.pop(0))
        i += 1

dataArray = [i+1 for i in range(34)]
rotation_remove(dataArray)

print(dataArray)


#70. 题目：写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度。


def str_len(strx):
    print('The str len is %d' % len(strx))

str_len('aaddffee')