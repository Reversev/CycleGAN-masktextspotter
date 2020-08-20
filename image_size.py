#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author = 'IReverser'

"""
    This is a script to resize images.
"""
import os.path
import sys

from PIL import Image
import glob
import time

import shutil

aspect = [1024, 300]  # 比例分配


def convertjpg(jpgfile, outdir):
    img = Image.open(jpgfile)
    width = int(aspect[0])
    height = int(aspect[1])
    new_img = img.resize((width, height), Image.BILINEAR)
    new_img.save(os.path.join(outdir, os.path.basename(jpgfile).split('.')[0]+str('_resize.jpg')))
    # new_img.save(os.path.join(outdir, os.path.basename(jpgfile)))


def png2jpg(source_path, resize_path, types):
    files = []
    image_list = os.listdir(source_path)
    # print(image_list)
    files = [os.path.join(source_path, _) for _ in image_list]
    for index, jpg in enumerate(files):
        if index > 1000:
            break
        try:
            sys.stdout.write('\r>>Converting image %d/100000 ' % (index))
            sys.stdout.flush()
            im = Image.open(jpg)
            png = os.path.splitext(jpg)[0] + "." + types
            im.save(png)
            shutil.move(png, resize_path)
        except IOError as e:
            print('could not read:', jpg)
            print('error:', e)
            print('skip it\n')
    sys.stdout.write('Convert Over!\n')
    sys.stdout.flush()


source_path = "/media/ty/PKBACK# 001/datasets/test_result/test_20200113_8000_1024/"
resize_path = "/media/ty/PKBACK# 001/datasets/test_result/test_20200113_8000_1024/"
start_time = time.time()
png2jpg(source_path, resize_path, 'jpg')
source_path = source_path + str("*.jpg")

for jpgfile in glob.glob(source_path):  # 图片路径
    if not os.path.exists(resize_path):
        print('Source_path is not exit. Creating ......')
        os.mkdir(resize_path)
        print('reading........')
    # dirname, filename = os.path.split(jpgfile)
    # print(str('resize_')+filename.split('.')[0]+str('.jpg'))
    convertjpg(jpgfile, resize_path)  # 保存路径
print('Processing Finish!')
end_time = time.time()
print('The total cost time:', str(end_time-start_time)+str('sec'))
