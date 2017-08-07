# 91.题目：时间函数举例1。
import time


print(time.ctime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.asctime(time.gmtime(time.time())))
print(time.time())


# 92 题目：时间函数举例2。

start = time.time()

for i in range(10000):
    i += 1

end = time.time()

print(start-end)


# 93.题目：时间函数举例2。

start = time.clock()

for i in range(10000):
    i += 1

end = time.clock()

print(start-end)

# 94. 题目：时间函数举例4,一个猜数游戏，判断一个人反应快慢。


# 95. 题目：字符串日期转换为易读的日期格式。

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))


# 96. 题目：计算字符串中子串出现的次数。

source = 'abc,bcd,abcd,aabbccddbcd'

print(source.count('bcd'))

# 97. 题目：从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。

from sys import stdout


def output_in_disk():
    fileName = input('pls input the file name: \n')
    fp = open(fileName, 'w')

    ch = input('pls input the context: \n')

    while ch != '#':
        fp.write(ch)
        stdout.write(ch)
        ch = input('pls go on : \n')

    fp.close()

#output_in_disk()


# 98. 题目：从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。


def output_in_disk_with_caseup(fileName):
    #fileName  = input('pls input the file name: \n')

    fp = open(fileName, 'w')
    ch = input('pls input the context: \n')

    while ch != '#':
        fp.write(ch.upper())

        ch = input('pls go on: \n')
        ch = ch.upper()

    fp.close()

# output_in_disk_with_caseup('test_gogo')


# 99. 题目：有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。


def merge_file_and_sorted():
    output_in_disk_with_caseup('gog')

    fp = open('gog')
    x = fp.read()

    print(x)
    l = list(x)
    l.sort()
    print(l)

# merge_file_and_sorted()


# 100. 题目：列表转换为字典。

x = ['a', 'b']
y = [1, 2]

print(dict(zip(x, y)))
