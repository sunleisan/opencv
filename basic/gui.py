import cv2 as cv
import numpy as np


def get_image():
    print("保存灰度图像")
    # 输入灰度图片
    img = cv.imread('./test.jpg', 0)
    # 显示图片
    cv.imshow('test', img)
    cv.imwrite('test_gray.jpg', img)
    # 退出图片
    cv.waitKey(0)
    cv.destroyAllWindows()
    print("灰度图片图像退出")


def get_video():
    print("视频读取显示保存")
    # 获取摄像头,参数0标记摄像头索引号,0为内置摄像头
    # 也可以从文件中获取 cv.VideoCapture('./test.avi')
    cap = cv.VideoCapture(0)
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
    # 按帧捕捉
    while True:
        ret, frame = cap.read()
        # gray = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)
        # 前置摄像头,1左右调换,-1上下调换
        frame = cv.flip(frame, 1)
        cv.imshow('frame', frame)
        out.write(frame)
        # 延迟设置
        c = cv.waitKey(10)
        if c == ord('q'):
            break
    # 关闭
    cap.release()
    out.release()
    cv.destroyAllWindows()
    print("视频操作退出")


def draw():
    img = np.zeros((512, 512, 3), np.uint8)
    # 图片,起点,终点,颜色RGB值,粗细值
    cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
    # 图片,左上角,右下角,颜色值,粗细值
    cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
    # 图片,圆点,半径,颜色值,粗细值(-1填充图形)
    cv.circle(img, (447, 63), 63, (0, 0, 255), -1)
    # 图片,中心点,长短轴长度，旋转角度,颜色值,粗细值
    cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, (255, 0, 0), -1)
    pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
    pts = pts.reshape(-1, 1, 2)
    # 图片,线条列表,首位闭合,颜色值
    cv.polylines(img, [pts], True, (0, 255, 255))
    font = cv.FONT_HERSHEY_SIMPLEX
    # 图片,文字,位置,字体,大小,颜色,粗细,线条类型
    cv.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv.LINE_AA)
    cv.imshow('img', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def draw_circle(event, x, y, flag, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(image, (x, y), 30, (255, 0, 0), 2)
        cv.imshow('image', image)
        print(flag)
        print(param)
    else:
        print(event)


def draw_while_double_click():
    print("查询系统所有事件")
    events = [i for i in dir(cv) if 'EVENT' in i]
    print(events)
    # 设置监听器, 设置一次即可
    cv.namedWindow('image')
    cv.setMouseCallback('image', draw_circle)
    cv.imshow('image', image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    print("鼠标事件结束")


# global data
image = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')
drawing = False
mode = True  # 画矩形
sx, sy = -1, -1  # 起点坐标


# mouse callback function
def draw_something(event, x, y, flag, param):
    color=(cv.getTrackbarPos('B','image'),cv.getTrackbarPos('G','image'),cv.getTrackbarPos('R','image'))
    global drawing, mode, sx, sy
    # 捕捉不同事件
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        sx, sy = x, y
        print(flag)
        print(param)
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                # don't do anything
                pass
            else:
                cv.circle(image, (x, y), 5, color, -1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv.rectangle(image, (sx, sy), (x, y), color, 1)
        else:
            cv.circle(image, (x, y), 5, color, -1)


def draw_while_mouse_move():
    cv.createTrackbar('R', 'image', 0, 255, do_nothing)
    cv.createTrackbar('G', 'image', 0, 255, do_nothing)
    cv.createTrackbar('B', 'image', 0, 255, do_nothing)
    global mode
    cv.namedWindow('image')
    cv.setMouseCallback('image', draw_something)
    while 1:
        cv.imshow('image', image)
        c = cv.waitKey(1)
        if c == ord('m'):
            mode = not mode
        elif c == ord('q'):
            break
    cv.destroyAllWindows()


def do_nothing():
    pass


def track_bar():
    # create trackBar: bar标记名,显示的图片名,最小值,最大值,变化的回调函数
    cv.createTrackbar('R', 'image', 0, 255, do_nothing)
    cv.createTrackbar('G', 'image', 0, 255, do_nothing)
    cv.createTrackbar('B', 'image', 0, 255, do_nothing)
    cv.createTrackbar('switch', 'image', 0, 1, do_nothing)
    while 1:
        cv.imshow('image', image)
        r = cv.getTrackbarPos('R', 'image')
        g = cv.getTrackbarPos('G', 'image')
        b = cv.getTrackbarPos('B', 'image')
        s = cv.getTrackbarPos('switch', 'image')
        if s == 0:
            image[:] = 0
        else:
            image[:] = [b, g, r]
        if cv.waitKey(10) == ord('q'):
            break
    cv.destroyAllWindows()


draw_while_mouse_move()
