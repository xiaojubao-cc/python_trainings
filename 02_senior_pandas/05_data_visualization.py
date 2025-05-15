#数据可视化
import matplotlib.pyplot
import pandas
from pandas import DataFrame

data:DataFrame = pandas.read_csv("data.csv",usecols=["PassengerId","Survived","Name","Sex","Age","Embarked","Fare","Ticket"],index_col="PassengerId")
#针对数据进行处理
data.dropna(subset=["Age"],inplace=True)
#转化age的类型
data["Age"].astype(int)
#绘制折线图
data.plot(kind="pie",y="Age",labels=data["Sex"],autopct='%1.1f%%', title='Age Proportions', figsize=(8, 5))
matplotlib.pyplot.show()