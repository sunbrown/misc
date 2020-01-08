#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/19 19:15
# @Author  : Brown
# @FileName: 根据msk筛选src.py
# @Software: PyCharm

import os
import shutil

a_path = 'E:/肖练/基因分型/src'
b_path = 'E:/肖练/traindata/msk'
save_path = 'E:/肖练/基因分型/msk'


def listing_img(in_path):
    name_list = []
    for root1, dirs1, files1 in os.walk(in_path):
        for file1 in files1:
            if os.path.splitext(file1)[1] == ".jpg" or '.JPG' or '.png':
                path0 = os.path.join(root1, file1)
                name_list.append(path0)
    return name_list


a_list = listing_img(a_path)
b_list = listing_img(b_path)

for i in a_list:
    basename = os.path.basename(i)[:-4]
    b = 0
    for j in b_list:
        if j.find(basename) != -1:
            b = j
            break
    path = i.replace(a_path, save_path, 1)
    path = path.replace('jpg', 'png', 1)
    save_dir = path.split('\\')[:-1]
    save_dir = '\\'.join(save_dir)

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    dist = save_dir + '\\' + basename + '.png'
    shutil.copyfile(b, dist)
