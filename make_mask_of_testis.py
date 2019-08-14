#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Brown

import cv2
import numpy as np
import os
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import tkinter as tk
# import thread
import time
import threading
from multiprocessing import Process


# -----------------------opencv主函数------------------------------------------
def main_cv2():
    global img, img2, save_path, im_idx, list_img_names
    while im_idx < len(list_img_names):
        if done > im_idx:
            print('第{}张图片'.format(im_idx + 1))
            im_idx += 1
            continue
        else:
            print('第{}张图片'.format(im_idx + 1))
            str_img_path = list_img_names[im_idx]
            list_split_name = str_img_path.split('\\')
            image_name = list_split_name[-1]
            ck_id = int(list_split_name[-2])
            root = '\\'.join(list_split_name[0:-1])

            # 保存文件到E盘相应位置
            save_path = 'E' + root[1:len(root)]
            info = '检查号：{}, 图片目录：{}'.format(ck_id, str_img_path)
            info1 = '按R重画，按空格下一张或者跳过，按Q上一张(需要重新运行程序)，按ESC退出'
            img = cv2.imread(str_img_path)
            if img is None:
                break
            # time.sleep(0.05)
            img2 = img.copy()
            # ---------------图像预处理，设置其大小---------------------------
            # height, width = img.shape[:2]
            # size = (int(width * 0.3), int(height * 0.3))
            # img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
            # ------------text窗口相关------------------------------------------------
            # --------------PIL图片上打印汉字--------------
            with open(r'./report.csv', 'r') as f:
                for df in pd.read_csv(f, chunksize=10000):
                    # s = df.loc[df['check_id'] == ck_id, :]
                    # a = s.DES
                    a = df.DES[df.check_id == ck_id]
                    # print(a)
            j = 2 * row_ledge
            white_bg = Image.new('RGB', (1700, 200), 'white')  # 定义文字框背景
            draw = ImageDraw.Draw(white_bg)  # 图片上打印
            font = ImageFont.truetype("simhei.ttf", row_ledge, encoding="utf-8")  # 参数1：字体文件路径，参数2：字体大小
            font1 = ImageFont.truetype("simhei.ttf", 2 * row_ledge, encoding="utf-8")  # 参数1：字体文件路径，参数2：字体大小
            draw.text((0, 0), info1, (0, 0, 255), font=font1)  # 提示文字
            draw.text((0, 2 * row_ledge), info, (255, 0, 250), font=font)  # 参数：位置坐标；打印文字；文字颜色；字体
            #  -----------------------换行控制----------------------------------
            for i in a:
                if len(i) > row_length:
                    row_count = int((len(i) + row_length - 1) / row_length)  # 向上整除得需要打印的行数
                    for jj in range(row_count):
                        if len(i[jj * row_length:-1]) > row_length:
                            draw.text((0, j + (jj + 1) * row_ledge), i[jj * row_length:(jj + 1) * row_length],
                                      (255, 0, 0), font=font)
                        else:
                            draw.text((0, j + (jj + 1) * row_ledge), i[jj * row_length:len(i)], (255, 0, 0),
                                      font=font)
                    j += row_count * row_ledge
                else:
                    draw.text((0, j + row_ledge), i[0:row_length], (255, 0, 0),
                              font=font)  # 参数1：打印坐标，参数2：文本，参数3：字体颜色，参数4：字体
                    j += row_ledge
            # --------------PIL图片转cv2 图片--------------
            text_frame = cv2.cvtColor(np.array(white_bg), cv2.COLOR_RGB2BGR)
            cv2.namedWindow('text', 1)
            # cv2.resizeWindow('text', 1920-img.shape[1], 1080-325-100)
            cv2.moveWindow('text', 200, img.shape[0] + 32)
            # font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.imshow('text', text_frame)
            # -----------循环检测鼠标移动点--------------------------------
            while 1:
                # -----------src窗口相关------------------------------------
                cv2.namedWindow('src', 1)  # , cv2.WINDOW_NORMAL)
                # cv2.resizeWindow('src', 1000, 800)  # 调整窗口大小
                cv2.moveWindow('src', 200, 0)  # 调整窗口位置
                cv2.imshow('src', img2)
                cv2.setMouseCallback('src', on_mouse)

                # ------------捕捉按键，控制循环------------------------------------------------
                k = cv2.waitKey(1) & 0xFF
                # if k != 255:
                #     print(k)
                # ------------按R键，重新扣图------------------------------------------------
                if k == 114:
                    if os.path.exists(save_path + '/H' + '.png'):
                        os.remove(save_path + '/H' + '.png')
                        print('已删除第{}张'.format(im_idx + 1) + '横切')
                    else:
                        print('不存在第{}张'.format(im_idx + 1) + "横切")
                    if os.path.exists(save_path + '/V' + '.png'):
                        os.remove(save_path + '/V' + '.png')
                        print('已删除第{}张'.format(im_idx + 1) + '纵切')
                    else:
                        print('不存在第{}张'.format(im_idx + 1) + "纵切")
                    img2 = img.copy()
                # ------------空格键下一张,Q键下个文件夹，按ESC退出程序------------------------------------------------
                if k == 32:
                    # file_list.append(file)
                    im_idx += 1
                    ff.seek(0)
                    ff.truncate()
                    ff.write(str(im_idx))
                    # ff.writelines(file+"\n")
                    break
                if k == ord('q'):
                    im_idx -= 1
                    ff.seek(0)
                    ff.truncate()
                    ff.write(str(im_idx))
                    print('回滚上一张图片')
                    break
                if k == 27:
                    break
            # if k == 27 or k == ord('q'):
            #     break
            if k == 27:
                print('程序终止')
                ff.close()
                cv2.destroyAllWindows()
                break


def on_mouse(event, x, y, flags, param=0):
    global img, img2, point1, count, pointsMax, mode
    global lsPointsChoose, tpPointsChoose  # 存入选择的点
    global pointsCount  # 对鼠标按下的点计数
    global mouse_flag
    mouse_flag = True

    # ------------按住左键或者右键开始勾画------------
    if event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON \
            or event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_RBUTTON \
            or event == cv2.EVENT_LBUTTONDOWN \
            or event == cv2.EVENT_RBUTTONDOWN \
            or event == cv2.EVENT_LBUTTONDBLCLK \
            or event == cv2.EVENT_RBUTTONDBLCLK:  # 鼠标移动

        if event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_RBUTTON:
            mouse_flag = False
        pointsCount = pointsCount + 1
        point1 = (x, y)
        # print(x, y)
        # ------------画圆圈------------
        # cv2.circle(img2, point1, 1, (0, 255, 0), 1)

        # ------------将选取的点保存到list列表里------------
        lsPointsChoose.append((x, y))
        tpPointsChoose.append((x, y))
        # ------------将鼠标选的点用直线连起来------------------------------------
        # print(len(tpPointsChoose))
        for ii in range(len(tpPointsChoose) - 1):
            if mouse_flag:
                cv2.line(img2, tpPointsChoose[ii], tpPointsChoose[ii + 1], (0, 0, 255), 3)  # 最后一个参数为线宽
            else:
                cv2.line(img2, tpPointsChoose[ii], tpPointsChoose[ii + 1], (255, 0, 0), 3)  # 最后一个参数为线宽
        cv2.imshow('src', img2)
    # --------------左键抬起，画mask--------------------------------------------------------
    elif event == cv2.EVENT_LBUTTONUP:
        mode = True
        roi_by_mouse()
        mouse_flag = 1
        lsPointsChoose = []
        tpPointsChoose = []
        print('横切')
    # --------------右键抬起，画mask--------------------------------------------------------
    elif event == cv2.EVENT_RBUTTONUP:
        mode = False
        roi_by_mouse()
        mouse_flag = 1
        lsPointsChoose = []
        tpPointsChoose = []
        print('纵切')
    else:
        pass
        # print('Do nothing!')


def listing_img(in_path):
    name_list = []
    for root1, dirs1, files1 in os.walk(in_path):
        for file1 in files1:
            if os.path.splitext(file1)[1] == ".jpg":
                path1 = os.path.join(root1, file1)
                name_list.append(path1)
    return name_list


def roi_by_mouse():
    global img, img2, ROI, mask2, mode, save_path_h, save_path_v
    mask = np.zeros(img.shape, np.uint8)
    pts = np.array([lsPointsChoose], np.int32)  # pts是多边形的顶点列表（顶点集）
    pts = pts.reshape((-1, 1, 2))
    # ------------这里 reshape 的第一个参数为-1, 表明这一维的长度是根据后面的维度的计算出来的。------------
    # ------------OpenCV中需要先将多边形的顶点坐标变成顶点数×1×2维的矩阵，再来绘制------------

    # --------------画多边形---------------------
    mask = cv2.polylines(mask, [pts], True, (255, 255, 255))
    # -------------填充多边形---------------------
    mask2 = cv2.fillPoly(mask, [pts], (255, 255, 255))

    # ------------mask窗口设置------------
    cv2.namedWindow('mask', 0)
    w = int(0.5*img.shape[0])
    cv2.resizeWindow('mask', w, w)  # 调整窗口大小
    cv2.moveWindow('mask', img.shape[1]+200, 0)  # 调整窗口位置
    cv2.imshow('mask', mask2)
    # ------------ROI窗口设置和图片保存------------
    ROI = cv2.bitwise_and(mask2, img)
    cv2.namedWindow('ROI', 0)
    cv2.resizeWindow('ROI', w, w)  # 调整窗口大小
    cv2.moveWindow('ROI', img.shape[1]+200, int(0.5*img.shape[0]))  # 调整窗口位置
    # cv2.imwrite('ROI.bmp', ROI)
    cv2.imshow('ROI', ROI)

    # ------------根据mode保存mask------------
    if mode:
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        cv2.imwrite(save_path + '/H' + '.png', mask2)
    else:
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        cv2.imwrite(save_path + '/V' + '.png', mask2)

# -----------------------定点ROI绘制，程序中未使用-------------------
# def fixed_ROI():
#     mask = np.zeros(img.shape, np.uint8)
#     pts = np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4]], np.int32)  # 顶点集
#     pts = pts.reshape((-1, 1, 2))
#     mask = cv2.polylines(mask, [pts], True, (255, 255, 255))
#     mask2 = cv2.fillPoly(mask, [pts], (255, 255, 255))
#     cv2.imshow('mask', mask2)
#     # cv2.imwrite('mask.bmp', mask2)
#     # cv2.drawContours(mask,points,-1,(255,255,255),-1)
#     ROI = cv2.bitwise_and(mask2, img)
#     cv2.imshow('ROI', ROI)
#     # cv2.imwrite('ROI.bmp', ROI)

# def draw_circle(event, x, y, flags, param):
#     if event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON \
#             or event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_RBUTTON \
#             or event == cv2.EVENT_LBUTTONDOWN \
#             or event == cv2.EVENT_RBUTTONDOWN \
#             or event == cv2.EVENT_LBUTTONDBLCLK \
#             or event == cv2.EVENT_RBUTTONDBLCLK:  # 鼠标移动
#         cv2.circle(img, (x, y), 10, (255, 250, 230), 1)


def main_tk():
    # 第1步，实例化object，建立窗口window
    window = tk.Tk()

    # 第2步，给窗口的可视化起名字
    window.title('My Window')

    # 第3步，设定窗口的大小(长 * 宽)
    window.geometry('500x300')  # 这里的乘是小x

    # 第4步，在图形界面上设定标签
    l = tk.Label(window, text='你好！this is Tkinter', bg='green', font=('Arial', 12), width=30, height=2)
    # 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

    # 第5步，放置标签
    l.pack()  # Label内容content区域放置位置，自动调节尺寸
    # 放置lable的方法有：1）l.pack(); 2)l.place();

    # 第6步，主窗口循环显示
    window.mainloop()


if __name__ == '__main__':
    # # 创建图像与窗口并将窗口与回调函数绑定
    # img = np.zeros((500, 500, 3), np.uint8)
    # cv2.namedWindow('image')
    # cv2.setMouseCallback('image', draw_circle)


    #  --------变量初始化------------------
    read_path = r'D:\greyimage'
    csv_path = r'report.csv'
    row_ledge = 16  # 定义行间距和字体大小
    row_length = 115  # 定义行长度
    #  ------进度读取--------
    done_dir = r'done.txt'
    mode = True
    img = img2 = lsPointsChoose = tpPointsChoose = list_img_names = []
    pointsCount = count = k = im_idx = done = 0
    pointsMax = 3000000
    save_path_h = save_path_v = ''
    if os.path.exists(done_dir):  # 读取进度文件
        ff = open(done_dir, 'r+')
        ff.seek(0)
        done = ff.read()
        if done:
            done = int(done)
        else:
            done = 0
    else:  # 进度文件不存在创建一个
        ff = open(done_dir, 'w+')
    # -------遍历所有的目录和文件，包括子文件夹------------
    list_img_names = listing_img(read_path)
    main_cv2()
    # print('thread %s is running...' % threading.current_thread().name)
    # t1 = threading.Thread(target=main_tk(), name='tk_thread')
    # t2 = threading.Thread(target=main_cv2(), name='cv2_thread')
    # t1.start()
    # t2.start()
    # print('thread %s ended.' % threading.current_thread().name)
    #
    # print('Parent process %s.' % os.getpid())
    # p1 = Process(target=main_tk())
    # p1.start()
    # p2 = Process(target=main_cv2())
    # print('Child process will start.')
    # p2.start()
    # # p.join()
    # print('Child process end.')