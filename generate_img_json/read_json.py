#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author = 'IReverser'
import os
import sys
import json
import io
import random
import re
import cv2
import numpy as np
from random import choice
import math


def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.jpg':
                L.append(os.path.join(root, file))
        return L


def write_read_json(points, chars, epoch):
    source_path = 'H:/opencv_image/test_test1/'  # picture path
    destination_path = 'H:/opencv_image/test2/'  # save json path

    article_info = {}
    data_json = json.loads(json.dumps(article_info, indent=4))
    print(data_json)
    data_json['version'] = '3.16.7'
    data_json['flags'] = {}

    shape_json = []

    # 设置新的json文件属性
    for i in range(0, 9, 1):

        # point = [[65, 40], [165, 40], [165, 130], [65, 130], [869, 40], [969, 40], [969, 130], [869, 130], [45, 20], [979, 20], [979, 280], [45, 280], [115, 195], [180, 195], [115, 265], [180, 265], [185, 195], [250, 195], [185, 265], [250, 265], [255, 195], [320, 195], [255, 265], [320, 265], [325, 195], [390, 195], [325, 265], [390, 265], [395, 195], [460, 195], [395, 265], [460, 265], [465, 195], [530, 195], [465, 265], [530, 265]]

        print(points[0])

        data_json_rec = "polygon"
        # print(point)

        char = chars[i]
        shape_json_item = {"label": char,
                           "line_color": 'null',
                           "fill_color": 'null',
                           "points": [points[i * 4],
                                      points[i * 4 + 1],
                                      points[i * 4 + 2],
                                      points[i * 4 + 3]],
                           "shape_type": data_json_rec,
                           "flags": {}}
        shape_json.append(shape_json_item)
    data_json['shapes'] = shape_json

    data_json["lineColor"] = [
        0,
        255,
        0,
        128
    ]
    data_json["fillColor"] = [
        255,
        0,
        0,
        128
    ]
    data_json['imagePath'] = str(epoch) + '_' + str(chars[2]) + '.jpg'
    data_json['imageData'] = None

    img_W = 1024
    img_H = 300
    data_json['imageWidth'] = img_W
    data_json['imageHeight'] = img_H

    data_info = json.dumps(data_json, ensure_ascii=False, indent=2)
    print(data_info)
    data_new_json_name = str(epoch) + '_' + str(chars[2]) + '.json'
    fp = open(destination_path + data_new_json_name, "w+")
    fp.write(data_info)
    fp.close()
