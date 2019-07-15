# -*- coding: utf-8 -*-
import cv2
import numpy as np
import time
import os
from PIL import Image, ImageDraw, ImageFont
import csv
import pandas as pd
import pickle



# -----------------------主函数------------------------------------------
def on_mouse(event, x, y, flags, param=0, pathImg=0):
    global img, img2, point1, count, pointsMax, mode
    global lsPointsChoose, tpPointsChoose  # 存入选择的点
    global pointsCount  # 对鼠标按下的点计数
    global img2, ROI_bymouse_flag

    # ------------按住左键或者右键开始勾画------------
    if event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON \
            or event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_RBUTTON \
            or event == cv2.EVENT_LBUTTONDOWN \
            or event == cv2.EVENT_RBUTTONDOWN \
            or event == cv2.EVENT_LBUTTONDBLCLK \
            or event == cv2.EVENT_RBUTTONDBLCLK:  # 鼠标移动

        pointsCount = pointsCount + 1
        # ------------感觉这里没有用？2018年8月25日20:06:42------------
        # ------------为了保存绘制的区域，画的点稍晚清零------------
        # if (pointsCount == pointsMax + 1):
        #     pointsCount = 0
        #     tpPointsChoose = []
        # print('pointsCount:', pointsCount)
        point1 = (x, y)
        # print(x, y)
        # ------------画圆圈------------
        cv2.circle(img2, point1, 1, (0, 255, 0), 1)

        # ------------将选取的点保存到list列表里------------
        lsPointsChoose.append([x, y])  # 用于转化为darry 提取多边形ROI
        tpPointsChoose.append((x, y))  # 用于画点
        # ------------将鼠标选的点用直线连起来------------------------------------
        # print(len(tpPointsChoose))
        for i in range(len(tpPointsChoose) - 1):
            # print('i', i)
            cv2.line(img2, tpPointsChoose[i], tpPointsChoose[i + 1], (0, 0, 255), 3) # 最后一个参数为线宽
        cv2.imshow('src', img2)
    # --------------左键抬起，画mask--------------------------------------------------------
    elif event == cv2.EVENT_LBUTTONUP:
        mode = True
        ROI_byMouse()
        ROI_bymouse_flag = 1
        lsPointsChoose = []
        tpPointsChoose = []
        print('横切')
    # --------------右键抬起，画mask--------------------------------------------------------
    elif event == cv2.EVENT_RBUTTONUP:
        mode = False
        ROI_byMouse()
        ROI_bymouse_flag = 1
        lsPointsChoose = []
        tpPointsChoose = []
        print('纵切')
    else:
        pass
        # print('Do nothing!')

def ROI_byMouse():
    global src, ROI, ROI_flag, mask2, mode
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
        cv2.imwrite(save_path + '/H_' + file[0:-4] + '.png', mask2)
    else:
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        cv2.imwrite(save_path + '/V_' + file[0:-4] + '.png', mask2)

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


if __name__ == '__main__':
    read_path = r'D:\greyimage'
    csv_path = r'report.csv'
    log_dir = r'log.txt'
    ff = open(log_dir, 'a+')
    file_list = []
    if os.path.exists(log_dir):
        ff = open(log_dir, 'r+')
        for line in ff:
            line = line.strip('\n')
            file_list.append(line)

    # save_path = 'E' + read_path[1:len(read_path)]
    mode = True
    lsPointsChoose = []
    tpPointsChoose = []
    pointsCount, count, k = 0, 0, 0
    pointsMax = 3000000
    # -------遍历所有的目录和文件，包括子文件夹------------
    for root, dirs, files in os.walk(read_path):
        for file in files:
            if file in file_list:
                continue
            else:
                ck_id = int(root.split('\\')[-1])
                img_path = os.path.join(root, file)
                save_path = 'E' + root[1:len(root)]
                img = cv2.imread(img_path)
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
                        s = df.loc[df['check_id'] == ck_id, :]
                        a = s.DES
                        # print(a)
                white_bg = Image.new('RGB', (1500, 200), 'white')
                draw = ImageDraw.Draw(white_bg)  # 图片上打印
                font = ImageFont.truetype("simhei.ttf", 15, encoding="utf-8")  # 参数1：字体文件路径，参数2：字体大小
                j = 0
                for i in a:
                    if len(i) > 100:
                        draw.text((0, j), i[0:100], (255, 0, 0), font=font)
                        draw.text((30, j+20), i[100:-1], (255, 0, 0), font=font)
                        j += 40
                    else:
                        draw.text((0, j), i[0:100], (255, 0, 0), font=font)  # 参数1：打印坐标，参数2：文本，参数3：字体颜色，参数4：字体
                        j += 20
                # --------------PIL图片转cv2 图片--------------
                texted_bg = cv2.cvtColor(np.array(white_bg), cv2.COLOR_RGB2BGR)
                cv2.namedWindow('text', 1)
                # cv2.resizeWindow('text', 1920-img.shape[1], 1080-325-100)
                cv2.moveWindow('text', 200, img.shape[0] + 32)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.imshow('text', texted_bg)
                # -----------循环检测鼠标移动点--------------------------------
                while (1):
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
                        img2 = img.copy()
                        print('重新扣图')
                    # ------------空格键下一张,Q键下个文件夹，按ESC退出程序------------------------------------------------
                    if k == 32:
                        file_list.append(file)
                        ff.writelines(file+"\n")
                        break
                    if k == ord('q') or k == 27:
                        break
            if k == ord('q') or k == 27:
                print('下个文件夹')
                break
        if k == 27:
            print('程序终止')

            ff.close()
            break
