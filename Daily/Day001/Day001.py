#!/usr/env/bin python3
# -*- coding:utf-8 -*-

"""
生成优惠券兑换码的主程序，包含两个子程序：生成器generator和确认器confirm
题目：作为 Apple Store App 独立开发者，你要搞限时促销
为你的应用生成激活码（或者优惠券），使用 Python 生成 200 个激活码（或者优惠券）
"""


from Daily.Day001 import generator, confirm
import os

# 设定兑换码长度以及数量，长度推荐为4的倍数（由于base64编码的原因）
NUM = 200
LENGTH = 16


# 设定初始化函数
def initcode():
    # 如果兑换码库文件存在，则删除
    if os.path.exists('codes.txt'):
        os.remove('codes.txt')
    if os.path.exists('confirmed.txt'):
        os.remove('confirmed.txt')
    print('>>>Coupon Bank initialized!<<<')
    return 1

if __name__ == '__main__':
    # 欢迎信息
    print('>>>Welcome to use the Coupon Generator by Alex Ryan!<<<')
    # 循环，直到用户输入'e'跳出循环
    while True:
        print('------------------------------------------')
        print('Type: i to initialize the Coupon bank;\nType: g to generate the Coupon code;')
        print('Type: c to confirm the Coupon code;\nType: e to exit')
        # 获取用户输入
        strg = input('Command:')
        if strg == 'i':
            initcode()
        elif strg == 'g':
            print('>>>The original length of the code is: %s, the amount of the codes is: %s<<<' % (LENGTH, NUM))
        # 调用生成器函数
            generator.generator(NUM, LENGTH)
        elif strg == 'c':
            print('>>>Confirm Coupon code!<<<')
            code = input('Enter the coupon code: ')
            # 调用确认器函数
            confirm.iscode(code, LENGTH)
        elif strg == 'e':
            break
        else:
            print('invalid')



