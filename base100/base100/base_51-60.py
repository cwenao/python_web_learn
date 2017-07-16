#!/usr/bin/python
# --*-- coding: UTF-8 --*--


#51 学习使用按位与 &
# 0&0=0; 0&1=0; 1&0=0; 1&1=1

a = 56
b = a & 3

print('this is the goods & a & 3: %d' % b)
b &= 3
print('this is the goods & b & 3: %d' % b)

#52 学习使用按位或 |
# 0|0=0; 0|1=1; 1|0=1; 1|1=1

c = a | 3

print('this is the goods | a | 3: %d' % c)

#53 学习使用按位异或 ^
# 0^0=0; 0^1=1; 1^0=1; 1^1=0

d = a ^ 3

print('this is the goods ^ ~~~ a ^ 3: %d' % d)

# 54 取一个整数a从右端开始的4〜7位

a = 1234567890 >> 4

print('this is a : %d ' % a)

b = ~(~0 << 4)

print('this is b : %d ' % b)
print('this is the goods ~ and & : %d ' % (a & b))

# 55 学习使用按位取反~

a = 123

print('this is the ~a: %d' % (~a))

#56 画图，学用circle画圆形


from tkinter import *


def draw_with_tkinter():
    canvas = Canvas(width=400,heigh=400,bg='red')
    canvas.pack(expand=YES, fill=BOTH)
    k = 1
    j = 1
    for i in range(0,26):
        canvas.create_oval(210-k,150-k,210+k,150+k, width=1)
        k += j
        j += 0.3
    mainloop()

#draw_with_tkinter()

#57 画图，学用line画直线

def draw_line():
    canvas = Canvas(width=400, heigh=400,bg='yellow')
    canvas.pack(expand=YES, fill=BOTH)
    x0 = 250
    y0 = 250
    y1 = 275

    for i in range(19):
        canvas.create_line(x0,y0,x0,y1,width=1,fill='red')
        x0 = x0 - 5
        y0 = y0 - 5
        y1 = y1 + 5
    mainloop()

#draw_line()

#58 画图，学用rectangle画方形。　

def draw_rectangle():
    root = Tk()
    root.title('CWENAO')
    canvas = Canvas(root,width=400,heigh=400,bg='yellow')
    canvas.pack()
    x0 = 250
    y0 = 250
    x1 = 275
    y1 = 275

    for i in range(19):
        canvas.create_rectangle(x0,y0,x1,y1)
        x0 = x0 - 5
        y0 = y0 - 5
        x1 = x1 + 5
        y1 = y1 + 5
    mainloop()

#draw_rectangle()

#60 计算字符串长度。

a = 'abcdefghedsfdsdf'
print('the string length is : %d' % (len(a)))
