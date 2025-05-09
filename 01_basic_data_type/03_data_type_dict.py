#dict操作
from collections import Counter, UserDict
from typing import Any, Iterator, ChainMap

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
#chainmap连接多个dict
dict01  = {"name": "Runoob"}
dict02 = {"age": 18}
chainmap:  ChainMap = ChainMap(dict01,dict02)
print(dict(chainmap))
#userdcit包装类
class MyDict(UserDict):
    def __setitem__(self, k:str, v:Any):
        print(f"修改或者插入键为:{k}数据为:{v}")
        super().__setitem__(k, v)

mydict: MyDict[str,Any] = MyDict()
mydict["name"] = "Runoob"
print(mydict)
