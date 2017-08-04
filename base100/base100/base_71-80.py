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

#create_link()


#73 题目：反向输出一个链表。


def create_reverse_link():
    pLink = []
    for i in range(20):
        pLink.append(i)
    pLink.reverse()
    print('this is the pLink to reverse print: ', pLink)

#create_reverse_link()


#74. 题目：列表排序及连接。


def sorted_and_linked():

    head = [1,3,2,5,9,110,67]
    tail = [111,45,89]

    head.sort()

    print('this is sorted the head: ', head)

    #head + tail 也可以
    head.extend(tail)
    print('this is to extend the head and tail :', head)

#sorted_and_linked()


#75. 放松一下，算一道简单的题目
# 简单的判断题不想写



#76. 题目：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n


def sum_num(n):

    x = 0

    if n % 2 == 0:
        x = 2
    else:
        x = 1

    sum_x = 0

    for i in range(x, n+1, 2):
        sum_x += 1/i

    print('this is the sum_x: %f ' % sum_x)

sum_num(6)


#77. 题目：循环输出列表


def rotation_list():
    ary = [1, 2, 4, 5, 3]

    for value in enumerate(ary):
        print('this is the key: %d , value: %d' %(value[0], value[1]))

rotation_list()


#78 题目：找到年龄最大的人，并输出。请找出程序中有什么问题。


def find_max_age():
    persons = {"a": 18, "b": 20, "c": 34}
    max_person = ""

    for x in persons.keys():
        if max_person == '':
            max_person = x

        if persons[x] > persons[max_person]:
            max_person = x

    print("this is the max person %s and age is %d " % (max_person, persons[max_person]) )

find_max_age()


#79 题目：字符串排序。


def sort_str(str1, str2):
    if str1 < str2:
        return str1, str2
    else:
        return str2, str1

print(sort_str('b', 'a'))


#80 题目：海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，
# 这只猴子把多的一个扔入海中，拿走了一份。
# 第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，
# 第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？


def distribution_things(n, x):

    if x == 0:
        return n
    n = n * 5 + 1
    x = x-1

    return distribution_things(n, x)

print(distribution_things(1, 5))






