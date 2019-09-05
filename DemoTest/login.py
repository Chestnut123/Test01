#!/usr/bin/evn Python3
# -*- encoding:utf-8 -*-
def hello(name):
    strHello='hello, ' + name
    return strHello;
print(hello("python"));

if __name__=="__main__":
    print("hello word！");

names = ['nini','uiui','ioi']
for name in names:
    print(name);

sum = 0;
for x in [1,2,3,4,5]:
    sum = sum + x;
    print(sum);

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
