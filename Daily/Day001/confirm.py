#!/usr/env/bin python3
# -*- coding:utf-8 -*-


# 读取兑换码库并返回一个set
def load(filename):
    codeset = set()
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            codeset.add(line.strip())
    return codeset


# 使用追加方法，将已经确认后的兑换码追加写入文件
def write(code, filename):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write('%s\n' % code)
        return 1


# 确认完成后，将删除已用兑换码的set，覆写原兑换码库
def lastwrite(newset, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for i in newset:
            f.write('%s\n' % i)
        return 1


def iscode(code, length=16):
    if len(code) < length:
        print('Invalid Coupon!')
        return 0
    bank = load('codes.txt')
    if code in bank:
        bank.remove(code)
        write(code, 'confirmed.txt')
        lastwrite(bank, 'codes.txt')
        print("Coupon confirmed!")
        return 1
    else:
        print('Invalid Coupon!')
        return 0


if __name__ == '__main__':
    iscode('NjA1ODQ4NTU3Njkw')
    iscode('MzU3MTQxNzE1OTAy')
