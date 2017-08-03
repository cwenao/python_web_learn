#71 编写input()和output()函数输入，输出5个学生的数据记录


student = []


def input_stu(stu, num):
    for i in range(5):
        stu.append(['', '', []])

    for i in range(num):
        stu[i][0] = input('input the num:\n')
        stu[i][1] = input('input the name:\n')

        for j in range(2):
            stu[i][2].append(int(input('input the score:\n')))


def output_stu(stu):
    for i in range(len(stu)):
        print('%-6s%-10s' % (stu[i][0], stu[i][1]))
        for j in range(len(stu[i][2])):
            print('%-8d' % stu[i][2][j])


#input_stu(student, 3)

#output_stu(student)


#72 创建一个链表

def create_link():
    pLink = []

    for i in range(20):
        pLink.append(i)

    print('this is the pLink', pLink)

create_link()


#73 题目：反向输出一个链表。


def create_reverse_link():
    pLink = []
    for i in range(20):
        pLink.append(i)
    pLink.reverse()
    print('this is the pLink to reverse print: ', pLink)

create_reverse_link()


#74. 题目：列表排序及连接。


def sorted_and_linked():

    head = [1,3,2,5,9,110,67]
    tail = [111,45,89]

    head.sort()

    print('this is sorted the head: ', head)

    #head + tail 也可以
    head.extend(tail)
    print('this is to extend the head and tail :', head)

sorted_and_linked()


#75. 放松一下，算一道简单的题目
# 简单的判断题不想写




