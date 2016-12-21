#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from random import randint
import base64
import math


# 计算用于生成指定长度兑换码需要的int位数
def intlen(length):
    return math.ceil(length/4)*3


def generate_code(length):
    grndint = randint(10**(intlen(length)-1), 10**intlen(length))
    byteint = str(grndint).encode('ascii')
    # 返回str
    return base64.b64encode(byteint).decode('ascii')


def generator(num, length=16):
    # 设定一个set，用于保存生成的兑换码，避免重复
    outputset = set()
    while len(outputset) < num:
        outputset.add(generate_code(length))
    print("Ready to output:")
    with open('codes.txt', 'w', encoding='utf-8') as f:
        for i in outputset:
            f.write('%s\n' % i)
            print('%s has been output!' % i)
        print(">>>Coupon-codes have all been generated!<<<")

# 测试生成20个字符长度为16的兑换码
if __name__ == '__main__':
    generator(20, 16)
