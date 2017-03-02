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

# 2. 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？

#思路： 奖金是根据利润走，且为区间为准；则按提成--利润对应关系



superprofit = [1000000,600000,400000,200000,100000,0]

royaltyRate = [0.01,0.015,0.03,0.05,0.075,0.1]



def calculateProfit(num,sumnum,profitList,rateList):
    if num < 0:
        return 0
    for i,v in enumerate(profitList):
        if (num - v) >0:
            sumnum  = sumnum + (num - v)*rateList[i]
            yield (num - v)*rateList[i]
            num = v


#profit = int(input())

profit = 120000
print(list(calculateProfit(profit,0,superprofit,royaltyRate)))


