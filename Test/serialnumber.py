#!/usr/env/bin python3
# -*- coding:utf-8 -*-

"""
尝试生成优惠码，并设定程序可以对其进行校验
"""

from random import randint, randrange, choice
import base64
import math


def b64_method_test():
    test1 = "atestcode".encode('ascii')
    # base64编码需要bytes类型数据
    a = base64.b64encode(test1).decode('ascii')
    b = base64.b32encode(test1)
    print('Code: %s, len: %d' % (a, len(a)))
    print(b)


def b64_method(leng):
    intlen = math.ceil(leng/4)*3
    init = randint(10**(intlen-1), 10**intlen)
    byteint = str(init).encode('ascii')
    return base64.b64encode(byteint).decode('ascii')


def b64_confirm(code, sset, leng=0):
    if (len(code) < leng) and (leng != 0):
        print('The code is too short!')
        return 0
    if code in sset:
        sset.remove(code)
        print('confirmed: %s' % code)
        return 1
    else:
        print('Not Confirmed!')
        return 0

serial_set = set()
length = 16
while len(serial_set)<20:
    serial_set.add(b64_method(length))
print('output done!')
print(serial_set)
print(len(serial_set))
b64_confirm('MTU5NzE0MTQ0MzY4', serial_set, length)