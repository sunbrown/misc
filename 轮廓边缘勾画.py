import cv2 as cv
import numpy as np


def contours(img):
    dst = cv.GaussianBlur(img, (3, 3), 0)
    # 转换为灰度图像
    gray = cv.cvtColor(dst, cv.COLOR_RGB2GRAY)
    # 转换为二值图像
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("bi", binary)

    clone_img, contour_lines, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contour_lines):
        cv.drawContours(img, contour_lines, i, (0, 255, 255), 2)
    cv.imshow("contours", img)


src = cv.imread(r'D:\code\SoftUi\U-Net\4.jpg')
cv.imshow('src', src)
contours(src)
cv.waitKey(0)
cv.destroyAllWindows()