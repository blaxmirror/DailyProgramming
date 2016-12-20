#!/usr/env/bin python3
# -*- coding:utf-8 -*-

"""
调用PIL进行简单的图像处理
"""

from PIL import Image, ImageFilter, ImageDraw, ImageFont

import random


def init_open(image):
    # 打开jpg文件，并获取图像尺寸
    img = Image.open(image)
    wid, hgt = img.size
    print('Original image size: %s * %s' % (wid, hgt))
    return img, wid, hgt


def test_thumbnail(image):
    # 调用开启函数，获取对象及图像尺寸
    img, wid, hgt = init_open(image)
    img.thumbnail((wid // 2, hgt // 2))
    print('Resize image to: %s * %s' % (wid // 2, hgt // 2))
    # 保存为jpeg
    img.save('thumbnail.jpg', 'jpeg')


def test_imageblur(image):
    img, wid, hgt = init_open(image)
    img2 = img.filter(ImageFilter.BLUR)
    img2.save('blur.jpg', 'jpeg')


def rndchar():
    return chr(random.randint(65, 90))


def rndcolor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rndcolor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def captcha():
    width = 60*4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Font对象
    font = ImageFont.truetype('Arial.ttf', 36)
    # 创建Draw对象
    draw = ImageDraw.Draw(image)
    # 填充每个像素：
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndcolor())
    # 输出文字：
    for t in range(4):
        draw.text((60 * t + 10, 10), rndchar(), font=font, fill=rndcolor2())
    # 模糊：
    image = image.filter(ImageFilter.BLUR)
    image.save('code.jpg', 'jpeg')


def dot_image(image):
    img, wid, hgt = init_open(image)
    font = ImageFont.truetype('Arial.ttf', int(wid*0.1))
    draw = ImageDraw.Draw(img)
    draw.text((wid*0.8, hgt*0.1), '10', font=font, fill=(255, 0, 70))
    img.save('edit.jpg', 'jpeg')



if __name__ == '__main__':
    test_thumbnail('test.jpg')
    test_imageblur('test.jpg')
    captcha()
    dot_image('test.jpg')
    print('ALL DONE\n')