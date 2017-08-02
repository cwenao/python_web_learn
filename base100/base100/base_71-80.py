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