#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author = 'IReverser'
"""
    this is open cv implement for product more figures for mu_ju project.
"""
import numpy as np
import cv2
import random
from read_json import write_read_json


def generator_opencv_img(epoch):
    # source_path = 'H:\\opencv_image\\test2\\'
    # IMAGE_NUM = 1
    point = []
    # for epoch in range(IMAGE_NUM):

    # create a white use numpy,size is:1024*300
    img = np.ones((300, 1024, 3), np.uint8)
    # fill the image with white
    img.fill(255)

    chars = []

    # start x y end x y color 半径
    # cv2.circle(img, (100, 85), 45, (0, 0, 0), -1)  # circle = -1 change as a point
    cv2.circle(img, (90, 85), 45, (0, 0, 0), -1)
    point.append([45, 40])
    point.append([135, 40])
    point.append([135, 130])
    point.append([45, 130])
    chars.append('o')

    # cv2.circle(img, (945, 85), 45, (0, 0, 0), -1)
    cv2.circle(img, (935, 85), 45, (0, 0, 0), -1)
    point.append([890, 40])
    point.append([980, 40])
    point.append([980, 130])
    point.append([890, 130])
    chars.append('o')

    # cv2.ellipse(img, (256, 256), (100, 50), 45, 0, 290, (0, 0, 255), -1)    # 画椭圆
    font = cv2.FONT_HERSHEY_SIMPLEX
    # cv2.putText(img, 'Hello', (10, 500), font, 4, (255, 2, 255), 2)

    # cv2.line(img, (10, 50), (511, 511), (255, 0, 0), 5)
    cv2.rectangle(img, (35, 20), (989, 280), (0, 0, 0), 15)  # 矩形——设置左上顶点和右下顶点，颜色，线条宽度
    point.append([35, 20])
    point.append([1009, 20])
    point.append([989, 280])
    point.append([35, 280])

    for num in range(6):
        char_num = random.randint(0, 9)
        # cv2.putText(img, str(char_num), (160 + num * 120, 230), font, 6, (0, 0, 0), 35)
        cv2.putText(img, str(char_num), (150 + num * 120, 230), font, 6, (0, 0, 0), 35)
        chars.append(str(char_num))
        point.append([150 + 120 * num, 75])
        point.append([268 + 120 * num, 75])
        point.append([268 + 120 * num, 265])
        point.append([150 + 120 * num, 265])
    print(point)

    print(chars)
    big_char = chars[1:]
    big_char.append('o')
    print(big_char)
    char_ = ''.join(big_char)
    print(char_)

    chars_ = ['o', 'o', str(char_), chars[2], chars[3], chars[4], chars[5], chars[6], chars[7]]
    print(chars_)

    img_name = str(epoch) + '_' + str(char_) + '.jpg '
    cv2.imwrite(source_path + img_name, img)

    return point, chars_, img_name


source_path = 'H:\\opencv_image\\test_test1\\'  # path for saving generted data
draw_path = 'H:\\opencv_image\\draw_test\\'   # draw contour for label in this path.
IMAGE_NUM = 9000  # generated picture count
for epoch in range(IMAGE_NUM):
    points, chars, img_name = generator_opencv_img(epoch)
    print(points)
    image = cv2.imread(source_path + img_name)
    for i in range(9):
        cv2.rectangle(image, (points[i * 4][0], points[i * 4][1]), (points[i * 4 + 2][0], points[i * 4 + 2][1]), (0, 0, 255))
        print((points[i * 4][0], points[i * 4][1]), (points[i * 4 + 2][0], points[i * 4 + 2][1]))
        cv2.imwrite(draw_path + img_name, image)
    write_read_json(points, chars, epoch)


