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

draw_oval()