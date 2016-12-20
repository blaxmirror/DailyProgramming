#!/usr/env/bin python3
# -*- coding:utf-8 -*-

"""
在头像的右上角加上一个红色的数字
"""


from PIL import Image, ImageDraw, ImageFont
import random


def image_addredint(image):
    img = Image.open(image)
    width, height = img.size
    print('原始图片大小为： %s * %s' % (width, height))
    # 设置字体对象
    font = ImageFont.truetype('Arial.ttf', width//10)
    draw = ImageDraw.Draw(img)
    draw.text((width*0.8, height*0.1), str(random.randint(4, 12)), font=font, fill=(255, 0, 70))
    img.save('output.jpg', 'jpeg')


if __name__ == '__main__':
    image_addredint('test.jpg')
    print('ALL DONE!\n')