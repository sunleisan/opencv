import cv2 as cv

print("image show")
# cv.namedWindow("test image", cv.WINDOW_AUTOSIZE)
img = cv.imread("./test.jpg")  # 读入图片
cv.imshow("imgShow(窗口的名字)", img)  # 显示图片
# 参数:毫秒时间 函数: 等待毫秒时间的键盘输入，有输入返回按键ASCII
# 没有输入返回-1,继续，参数为0无限等待输入
cv.waitKey(0)
cv.destroyAllWindows()  # 关闭全部窗口cv.destroyWindow(arg),关闭指定窗口
print("image show end")
