#dict操作
from typing import Any, Iterator

_dict: dict[str,Any] = dict()
#添加
_dict["age"] = 18
_dict["sex"] = "man"
_dict["hobby"] = ["football", "basketball", "swimming"]
#修改
_dict["age"] = 19
print(_dict)
#查询
print(_dict.get("age"))
#删除
#_dict.pop("age")
#获取所有的key
keys: Iterator[str] = _dict.keys()
print(list(keys))
#获取所有的value
values: Iterator[Any] = _dict.values()
print(list(values))
#遍历字典
for key,value in _dict.items():
    print(key,value)
#查询key是否在字典中
print("age" in _dict)

#字典推导式
"""
_dict = {key:value for value in collection if 条件}
"""
list_demo = ['Google','Runoob', 'Taobao']
_dict: dict[int,str] = {index:value for index,value in enumerate(list_demo)}
print(_dict)