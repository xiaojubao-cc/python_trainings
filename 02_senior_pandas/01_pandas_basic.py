#pandas基础
import pandas
from pandas import DataFrame

basic_dict = data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
data: DataFrame = pandas.DataFrame(basic_dict)
#排序
print(data.sort_values(by="Age", ascending=False))
#打印指定的列
print(data[["Name","Age"]])
#按照索引选择行
print(data.loc[1:2])
print(data.iloc[1:2])
#分组
print(data.groupby("City")["Age"].mean())
#返回详细的行列信息
print(data.info())
#返回行列数
print(data.shape)
#返回所有的列名
print(data.columns)
#返回行索引
print(data.index)
#按照指定列排序
data.sort_values(by="Name",ascending=False)
#按照标签返回值
#返回的数据是11行
print(data.loc[0:10])
#返回的数据是10行
print(data.iloc[0:10])
#连接两个dataFrame
left = pandas.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
right = pandas.DataFrame({'ID': [1, 2, 4], 'Age': [24, 27, 22]})
result = left.merge(right,on="ID",how="inner")
print(result)
#往已有的列或者行添加数据
df1: DataFrame = pandas.DataFrame({'A': [1, 2, 3]})
df2: DataFrame = pandas.DataFrame({'A': [4, 5, 6]})
#合并行数据
result = pandas.concat([df1, df2], axis=0,ignore_index=True)
df3: DataFrame = pandas.DataFrame({'B':["tom","jerry","bob"]})
result = pandas.concat([result, df3], axis=1,ignore_index=True)
print(result)
#透视表
data = {'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04'],
        'Category': ['A', 'B', 'A', 'B'],
        'Sales': [100, 150, 200, 250]}
df = pandas.DataFrame(data)
print(pandas.pivot_table(df,values='Sales',index='Date',columns='Category',aggfunc='sum',fill_value=0,margins=True,margins_name='Total'))
#交叉表是一种特殊的透视表
data = {'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
        'Region': ['North', 'South', 'North', 'South', 'West', 'East']}
df = pandas.DataFrame(data)
print(pandas.crosstab(df['Category'],df['Region']))


# 创建数据
data = {
    'date': ['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-02'],
    'product': ['A', 'A', 'B', 'B'],
    'sales': [100, 150, 200, 250]
}
df = pandas.DataFrame(data)

# 转换为多重索引
df = df.set_index(['date', 'product'])
print(df)
# 访问特定数据
print(df.loc[('2023-01-01', 'A')])
#优化建议
"""
尽量使用int类型，减少float类型，字符类型使用category:astype('category')
使用向量或者apply和applymap替代循环
使用分块处理大数据集
使用numba
# 示例函数
@numba.jit
def calculate_square(x):
    return x ** 2

# 使用 numba 加速计算
df = pd.DataFrame({'A': [1, 2, 3, 4]})
df['B'] = df['A'].apply(calculate_square)
print(df)
避免链式赋值
# 链式赋值：可能引发警告并影响性能
df['A'][df['A'] > 2] = 0

# 正确赋值方法：
df.loc[df['A'] > 2, 'A'] = 0

"""