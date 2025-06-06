#面向对象
"""
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__truediv__: 除运算
__mod__: 求余运算
__pow__: 乘方
"""
import json
import pickle
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, unique
from typing import Any


class Fruit(object):
    address: str
    #实例属性，在__init__方法执行前会调用__new__方法实例化
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.__specification = None


    def __del__(self):
        print(f"实例对象被释放了>>>>>")

    def __str__(self):
        return "水果名称:{self.name},价格是:{self.price}"

    def __repr__(self):
        return "Fruit(name:{self.name},price:{self.price})"

    @staticmethod
    def introduce():
        print("我是一个水果")

    @classmethod
    def set_address(cls, address:str):
        cls.address = address

    @property
    def specification(self):
        return self.__specification

    @specification.setter
    def specification(self,  value:str):
        if value not in ["small","big"]:
            raise ValueError("请输入正确的规格")
        self.__specification = value
#使用@property需要注意该变量需要私有化
apple = Fruit("苹果", 10)
print(apple)
Fruit.introduce()
Fruit.set_address("杭州")
print(Fruit.address)
apple.specification = "big"
print(apple.specification)



#类属性，多个实例共享,
#单例模式
class Singleton(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)

#使用json映射
@dataclass
class Subject:
    name:str
    score:int

#设置slots=True节约内存和提高访问速度
@dataclass(frozen=True,  order=True,slots=True)
class Student(object):
    id:str
    name:str
    cls:str
    age:int
    subjects:list[Subject]

student_str = """[
{
    "id": "001",
    "name": "张三",
    "cls": "1班",
    "age": 18,
    "subjects": [
        {
            "name": "数学",
            "score":123
        },
        {
            "name": "语文",
            "score":125
        }
    ]
},
{
    "id": "002",
    "name": "李四",
    "cls": "2班",
    "age": 18,
    "subjects": [
        {
            "name": "数学",
            "score":124
        },
        {
            "name": "语文",
            "score":125
        }
    ]
}
]"""

# json_str = json.loads(student_str)
# students: list[Student] = [Student(**s) for s in json_str]
json_str = json.loads(student_str)
students: list[Student] = [
    Student(
        #类中的对象属性单独结构
        subjects=[Subject(**subj) for subj in s["subjects"]],
        #非类属性直接结构
        **{k:v for k,v in s.items() if k != 'subjects'}
    )
    for s in json_str
]
#将对象映射成str
print(json.dumps(students,default=lambda o: o.__dict__,  indent=4))

#继承
class Animal(object):
    def __init__(self, name:str):
        self.name = name

    def eat(self):
        print("父类的方法")
        print(f"{self.name}在吃东西")


class Person(Animal):
    def __init__(self, name:str, age:int):
        super().__init__(name)
        self.age = age

    def eat(self):
        print(f"{self.name}在吃东西")
        super().eat()

p:Animal = Person("ww",  18)
super(Person,p).eat()

#抽象类实现一个模板方法
class PayMent(ABC):
    @abstractmethod
    def verify_identity(self) -> bool:
        pass
    @abstractmethod
    def pay(self, amount:float):
        pass


class AbstractPayMent(PayMent):

    def __init__(self,way:str):
        self.way = way
    def verify_identity(self) -> bool:
        print(f"验证支付方式{self.way}信息成功")
        return  True

    def pay(self, amount:float):
        raise NotImplementedError("子类必须实现此方法")


class WeixinPay(AbstractPayMent):
    def __init__(self, way:str):
        super().__init__(way)

    def pay(self, amount:float):
        print(f"使用微信支付{amount}元成功")

abstract_pay: AbstractPayMent = WeixinPay("微信")
if abstract_pay.verify_identity():
    abstract_pay.pay(100)

#自定义异常并支持序列化
class CustomException(Exception):
    def __init__(self, message:str, code:int) -> None:
        self.code = code
        self.message = message

    def __str__(self):
        return f"{self.code}>>>>>{self.message}"

    def __repr__(self) -> str:
        return f"{self.code}>>>>>{self.message}"

    #控制对象序列化和反序列化
    def __reduce__(self) -> tuple[Any,tuple[str,Any]]:
        #这里返回需要序列化的字段
        return self.__class__, (self.message, self.code)


cu:Exception = CustomException(message="自定义异常", code=1000)
#序列化
pickled:bytes = pickle.dumps(cu)
unpickled:CustomException =pickle.loads(pickled)
print(repr(unpickled))

#枚举
@unique
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

r = Color.RED
print(r.name,r.value)



