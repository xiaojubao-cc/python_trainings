#读取csv数据
import pandas
from pandas import DataFrame

data:DataFrame = pandas.read_csv("data.csv",sep=",",usecols=["PassengerId","Name","Sex","Age","Embarked","Fare"])
data["Age"] = data["Age"].fillna("0.00")
#data.to_csv("update_data.csv",index=False)
print(data.set_index("PassengerId").sort_values(by=["Fare","Embarked"]).to_string())