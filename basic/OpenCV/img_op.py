import numpy as np
import cv2 as cv


def show_image(i):
    cv.imshow('image', i)
    cv.waitKey(0)
    cv.destroyAllWindows()


# 1. 获取并修改像素值
image = cv.imread("test.jpg")
px = image[100, 100]
print(px)
# [100,100]像素点的BGR值
blue = image[100, 100, 0]
green = image[100, 100, 1]
red = image[100, 100, 2]
print(blue, green, red)
image[:, 100] = [255, 255, 255]
# 通道拆分
image = cv.imread("test.jpg")
b, g, r = cv.split(image)  # 拆分
print(b, g, r)
b = image[:, :, 0]  # 拆分
image[:, :, 2] = 0  # 红色通道设置0

# 图像扩边
image = cv.copyMakeBorder(image, 10, 10, 10, 10, cv.BORDER_WRAP)
print(image)
image = cv.imread("test.jpg")

# 图像上的算数运算
x = np.uint8([250])  # 8位最大255
y = np.uint8([10])
cv.add(x, y)  # 饱和运算最大255, 250+10=260->255 优先选择
print(x + y)  # 模运算 250+10=260%256=4
# 图像混合计算公式: h(x)=(1-a)f(x)+ag(x)+Y , Y常数参数,将Y取0
image1 = cv.imread("test.jpg")
image2 = cv.imread("test_gray.jpg")
dst = cv.addWeighted(image1, 0.3, image2, 0.7, 0)
show_image(dst)
