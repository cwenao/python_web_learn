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
