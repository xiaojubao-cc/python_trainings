#读取excel
import pandas
from pandas import DataFrame

pd: DataFrame = pandas.read_excel("runoob_pandas_data.xlsx",skiprows=1)
#print(pd)
#将csv数据转换为xlsx
csv_data = pandas.read_csv("update_data.csv")
#筛选出年龄小于25的female
#csv_data.query("Age<25 and Sex=='female'").sort_values(by=["Age","Sex"]).to_excel("data.xlsx",index=False,sheet_name="list")

#其他方式读取
with pandas.ExcelFile("data.xlsx") as other_way:
    pd: DataFrame = other_way.parse(other_way.sheet_names[0])
    #print(pd.to_string())
    #透视表
    pd = pd.pivot_table(index="Sex",values="Fare",aggfunc="sum",margins=True,margins_name="总计:")
    print(pd.to_string())
#
# #其他方式写入数据
# with pandas.ExcelWriter("other_way_data.xlsx") as writer:
#     csv_data.query("Age<25 and Sex=='female'").sort_values(by=["Age","Sex"]).to_excel(writer,sheet_name="list",index=False)
