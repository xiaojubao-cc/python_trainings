#数据清洗
from typing import Iterator

import pandas
import pymysql
from pandas import DataFrame
from sqlalchemy import create_engine

pd:  DataFrame = pandas.read_csv("property-data.csv",na_values = ["n/a", "na", "--"])
#删除所有的缺失值
#pd = pd.dropna()
#删除指定列的缺失值
#pd.dropna(subset=["PID"],  inplace=True)
#填充
pd.fillna({"PID": "000000000.0","NUM_BEDROOMS":0.0}, inplace=True)
#for index in pd.query("NUM_BEDROOMS==0.0").index:
    #print(pd.loc[index,"PID"])
    # 使用pymysql的连接方式
database_ip:str = "10.1.35.14"
database_username:str = "root"
database_password:str = "root"
database_name:str = "bfbms"
connection_string = f'mysql+pymysql://{database_username}:{database_password}@{database_ip}/{database_name}'
engine = create_engine(connection_string)
sql_pandas:DataFrame = pandas.read_sql("select midgroupid,groupname, bossprovince, functype, businessstate,  numtotal  from mcn_midgrp_config",con=engine)
sql_pandas["cumsum"] = sql_pandas.groupby(by="bossprovince")["midgroupid"].cumsum()
