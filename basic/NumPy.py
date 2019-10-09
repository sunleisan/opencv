import numpy as np

# numpy中数组的属性
# arange(start,end,num) 从start开始num个数小于end为止返回数组
# arange(3,7)=[3,4,5,6] arange(2)=[0,1,2] arange(3,7,2)=[3,4]
# array.reshape(3,5)=> 3*5的数组
# 可以调用科学模式窗口查看变量属性
a = np.arange(15).reshape(3, 5)
# 创建数组
b = np.array([1, 2, 3], np.int32)
# 全0的3*4数组
c = np.zeros((3, 4))
# 全1的3*4数组
d = np.ones((3, 4))
# 有序3*4数组
e = np.arange(12).reshape(3, 4)
f = np.linspace(0, 2, 9)
# 数组组成矩阵操作
A = np.array([[1, 2], [3, 4]])
B = np.array([[0, 1], [0, 1]])
# 对应元素运算
C = A * B
D = A + B
# 矩阵乘法
E = A.dot(B)

# 操作数组的一元方法
array = np.random.random((2, 3))
s = array.sum()
mi = array.min()
ma = array.max()
# 操作数组行列
array.sum(axis=0)  # 列求和
array.sum(axis=1)  # 行求和

# 通用数学算术方法
A = np.arange(3)
np.exp(A)
np.sqrt(A)
A = np.array([[1, 2], [3, 4]])
B = np.array([[0, 1], [0, 1]])
np.add(A, B)

# 数组索引切片迭代
A = np.arange(10) ** 3
# 第四个元素
print(A[3])
# a[2],a[3],a[4]
print(A[2:5])
# 从下标1开始,小于下标6为止,步长为2,不填默认最初值
print(A[1:6:2])
# 逆向切片
print(A[-1:-4:-1])
# 二维数组
A = np.arange(15).reshape(3, 5)
print(A[2, 3])  # 返回一个元素
print(A[:, 1])  # 返回一个数组
print(A[-1])  # 返回最后一行数组
# 迭代操作
# 每行迭代
for row in A:
    print(row)
# 每个元素迭代
for element in A.flat:
    print(element)

# shape操作
a = np.ones((3, 4), dtype=int)
print(a.ravel())  # 返回一元数组
print(a.reshape(2, -1))  # 返回两行,resize()直接改变原矩阵
print(a.T)  # 转置

# 数组堆叠切片
a = np.floor(10 * np.random.random((2, 2)))
b = np.floor(10 * np.random.random((2, 2)))
np.vstack((a, b))  # 横向堆叠行数不变
np.hstack((a, b))  # 纵向堆叠列数不变
# 数组分割
a = np.arange(12).reshape(3, 4)
np.split(a, 3)  # 横向分成三个数组[0,1,2,3],[4,5,6,7],[8,9,10,11]
np.hsplit(a, 4)  # 纵向分割
np.vsplit(a, 3)  # 横向分割
# 复制与视图
a = np.arange(12)
b = a  # python复制方式,a,b指向同一地址
c = a.view()  # 仅复制值
d = a.copy()  # 完整拷贝

# numpy 中常见运算
a = np.array([-0.23, 4.6, 9.34])
np.around(a=a, decimals=1, out=None)  # 四舍五入
np.floor(a)  # 返回不大于输入参数的最大整数,参数数组或单个元素
np.ceil(a)  # 返回大于输入参数的最小整数
np.where(a > 0, a, 0)  # a>0选择a否则选择0
