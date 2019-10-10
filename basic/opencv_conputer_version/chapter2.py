import numpy as np
import cv2 as cv

# 图像-> 一个3*3的数组表示, 每个像素点由8位数值表示
img = np.zeros((3, 3), dtype=np.uint8)
print(img)
# 每一个像素点由[B,G,R]三个数值组成的数组表示
img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
print(img)
# 转换图片格式，imread()会删除Alpha通道信息
image = cv.imread('logo.png', cv.IMREAD_GRAYSCALE)
# bmp格式位图要求通道有8位, png要求通道8位或16位
cv.imwrite('logo_gray.png', image)

# 块操作
img = cv.imread('logo.png')
