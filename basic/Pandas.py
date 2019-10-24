import numpy as np
import pandas as pd

# 参考:https://www.pypandas.cn/
# 对象创建
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
# 返回2013-10-17开始的6天日期
dates = pd.date_range('20191017', periods=6)
print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=('A', 'B', 'C', 'D'))
print(df)
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4))),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print(df2)
print(df.tail(3))  # 查看前三行
print(df.index)  # 查看索引
print(df.columns)  # 查看列
# Pandas于Numpy根本区别,Pandas不需要所有元素类型相同,但每一列相同
print(df.describe())  # 基本统计信息
print(df.T)  # 转置
print(df.sort_index(axis=1, ascending=False))  # 按轴逆排序
print(df.sort_values(by='B'))  # 按值排序
# 获取
print(df['A'])  # 获取一个Series
print(df[0:3])  # 切片
print(df.loc[dates[0]])  # 按标签获取
print(df.loc[:, ['A', 'B']])  # 标签和轴获取数据
print(df.loc['20191020':'20191021', ['A', 'B']])
print(df.loc[dates[0], 'A'])  # 获取单个值
print(df.at[dates[0], 'A'])  # 获取单个值
# 按位置选择
print(df.iloc[3])
print(df.iloc[3:5, 0:2])  # 行:3-5 列0-2
print(df.ilo[[1, 2, 4], [0, 2]])
print(df.iloc[1, 1])  # 具体值
print(df.iat[1, 1])  # 具体值
print(df[df.A>0])  # 列的值选择

