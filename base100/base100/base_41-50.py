#41. 模仿静态变量的用法。


class TestStatic:
    staticVar = 10

    def up_static(self):
        self.staticVar += 1
        print('this is to imitate the static var : ', self.staticVar)

print(TestStatic.staticVar)
x = TestStatic()

for i in range(3):
    x.up_static()

#42. 学习使用auto定义变量的用法。
# auto 出自C: 函数中的局部变量，如不专门声明static，一般都是动态地分配存储空间
# python : 变量搜索路径是：本地变量->全局变量

num = 2
def autofunc():
    num = 1
    print('internal block num = %d' % num)

for i in range(3):
    print('The num = %d' % num)
    num += 1
    autofunc()

#44 Python 两个矩阵相加

X = [[0, 3, 4], [1, 3, 5], [2, 4, 6]]
Y = [[1, 3, 3], [0, 2, 4], [1, 3, 9]]
Z = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def matrix_plus():
    for i in range(len(X)):
        for j in range(len(Y)):
            Z[i][j] = X[i][j] + Y[i][j]

matrix_plus()
for x in Z:
    print('this is the matrix plus: ', x)


#45 统计 1 到 100 之和

def sum_count():
    n = 1
    m =100
    tmp = (m+n) * (m-n +1)/2
    print("this is the sum 1-100: %d" % (tmp))

sum_count()

print("To use the sum function, the sum is %d" %(sum(range(1,101))))


#46 求输入数字的平方，如果平方运算后小于 50 则退出

import math

def power_count(x):
    print('this is the x: %d' % x)
    x = math.pow(x,2)
    print('this is the pow: %d' % x)

power_count(5)