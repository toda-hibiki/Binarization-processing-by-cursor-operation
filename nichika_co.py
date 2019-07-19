# coding: UTF-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

# 画像をグレースケールとして読み込む
src = cv2.imread('050.png', 0)
dst = src.copy()

# トラックバーを動かしたときに呼ばれる関数
def threshold(x):
    global dst
    ret, dst = cv2.threshold(src, x, 255, cv2.THRESH_BINARY)


# ウィンドウを作成する
cv2.namedWindow('Image')
cv2.createTrackbar('Threshold', 'Image', 0, 255, threshold)

while(True):
    cv2.imshow('Image', dst)

    # ESC キーを押したら終了する
    key = cv2.waitKey(1)
    if key == 27:
        break

    # get current threshold.
    thresh = cv2.getTrackbarPos('Threshold', 'Image')

cv2.destroyAllWindows()
