#  [参考](https://www.runoob.com/w3cnote/matplotlib-tutorial.html)
#  Matplotlib教程
#  IPython是Python增强版(命名输入输出系统命令纠错能力)
#  pylab 是Matplotlib 面向对象的绘图库

#  正弦函数 余弦函数
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 256)
c, s = np.cos(x), np.sin(x)
plt.plot(x, c)
plt.plot(x, s)
plt.show()

#  散点图
plt.figure(2)
x = np.random.normal(0, 1, 1024)
y = np.random.normal(0, 1, 1024)
plt.scatter(x, y)
plt.show()
