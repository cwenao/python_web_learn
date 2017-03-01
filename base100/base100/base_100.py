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

