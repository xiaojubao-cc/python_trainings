#装饰器类似一个内函数，以外函数为参数，返回一个内函数，最外层一定是一个函数
import functools
#方法装饰器
def func_decorator(func):
    def wrapper(*args,**kwargs):
        print(f"{func.__name__}开始执行>>>>>>")
        result:  str = func(*args,**kwargs)
        print(f"{func.__name__}执行结束>>>>>>")
        return result
    return wrapper

@func_decorator
def greet(name) -> str:
    print(f"hello {name}")
    return  name

print(greet("alice"))

#类装饰器相当于内部类是被装饰器的子类，通过重写父类的方法
def class_decorator(cls):
    class Wrapper(cls):
            def __init__(self,*args,**kwargs):
                super().__init__(*args,**kwargs)
            def greet(self,*args,**kwargs):
                print("类装饰器前置通知")
                super().greet(*args,**kwargs)
                print("类装饰器后置通知")

            def say(self,*args,**kwargs):
                print("类装饰器前置通知")
                super().say(*args,**kwargs)
                print("类装饰器后置通知")

            def close_relatives(self,*args,**kwargs) ->  list[str]:
                print("类装饰器前置通知")
                result: list[str] = super().close_relatives(*args,**kwargs)
                print("类装饰器后置通知")
                return result
    # 保留元数据
    functools.update_wrapper(Wrapper, cls, updated=())
    return Wrapper


@class_decorator
class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"hello {self.name}")

    def say(self, message):
        print(f"{self.name} say: {message}")

    def close_relatives(self,relatives:list[str]) ->  list[str]:
        return [relative for relative in relatives if relative != self.name]
person = Person("alice")
person.greet()
person.say("hello")
print(person.close_relatives(["bob","alice","tom"]))

#类内置的装饰器@staticmethod @classmethod @property在类中展开