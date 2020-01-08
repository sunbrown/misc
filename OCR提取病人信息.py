#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 13:20
# @Author  : Brown
# @FileName: OCR提取病人信息.py
# @Software: PyCharm

from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '17813914'
API_KEY = 'RAgpB20mkGwBKB46UTs287gH'
SECRET_KEY = 'wQclv68wrl30GGAPiSRLeQfSKv7NZ0h0'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# image = get_file_content(r'C:\Users\sunbrown\Pictures\20191120081657.jpg')
image = get_file_content(r'e:\阑尾截屏\2009\0000297699.PNG')

""" 调用通用文字识别, 图片参数为本地图片 """
# client.basicGeneral(image)

""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "false"
options["detect_language"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别, 图片参数为本地图片 """
a = client.basicGeneral(image, options)
print(a)
