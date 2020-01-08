#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8 16:32
# @Author  : Brown
# @FileName: 截取图片.py
# @Software: PyCharm
import os
from PIL import Image

read_path = 'E:/肖练'
save_path = 'E:/肖练(去敏感信息)'
c = 0
for root, dirs, files in os.walk(read_path):
    for file in files:
        if file[-1] == 'g' or file[-1] == 'G':
            img = Image.open(os.path.join(root, file))
            try:
                img.paste('black', (0, 0, img.width, int(0.16*img.height)))
                save_dir = os.path.join(save_path, root[6:])
                print(os.path.join(root, file))
                if not os.path.exists(save_dir):
                    os.makedirs(save_dir)
                img.save(os.path.join(save_dir, file))
            except OSError:
                img.save(os.path.join(save_path, file))
        else:
            c += 1
            print(c)
