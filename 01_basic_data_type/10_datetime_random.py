#时间相关操作
#获取当前时间
import random
from datetime import datetime, timedelta

_now = datetime.now()
print(f"当前时间:{_now}")
#格式化当前时间
_format_time = datetime.strftime(_now, "%Y-%m-%d %H:%M:%S")
print(f"格式化当前时间:{_format_time}")
#字符串转datetime
_datetime = datetime.strptime("2023-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
print(type(_datetime))
#时间计算但不支持年和月
_timedelta  = timedelta(days=1, hours=1, minutes=1, seconds=1)
print(datetime.strftime(_now + _timedelta, "%Y-%m-%d %H:%M:%S"))

#随机数操作
#[0,1)生成随机数
print(f"当前生成随机数:{random.random()}")
#指定范围内生成随机数[0,10)
print(f"指定范围内生成随机数:{random.randrange(0, 10,2)}")
#指定范围内生成随机数[0,10]
print(f"指定范围内生成随机数:{random.randint(0, 10)}")
#指定序列中返回一个随机数
_list:list[int] = [1, 2, 3, 4, 5]
print(f"指定序列中返回一个随机数:{random.choice(_list)}")
#随机打乱序列
random.shuffle(_list)
print(f"随机打乱后的序列:{_list}")
_list0: list[str] = ["boa","cat","dog"]
print(f"随机返回一个元素:{random.choice(_list0)}")