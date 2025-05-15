#list操作
from collections import deque, OrderedDict, Counter, UserList
from itertools import islice, batched, chain, groupby, product, permutations, combinations
from typing import Iterator, Any, get_origin, get_args

_list: list[int] = list()
#末尾添加指定数据
_list.extend([1])
_list.append([2,3,4])
_list.insert(2,5)
print(_list)
#删除指定索引下的数据
del _list[2]
print(_list)
#修改指定索引下的数据
_list[1] = 6
print(_list)
#返回指定数据的索引
print(_list.index(6))
#遍历
for index,value in enumerate(_list):
    print(index,value)

for value in _list:
    print(value)

for index in range(len(_list)):
    print(index,_list[index])

#排序
_list.sort(reverse=True)
print(_list)
#删除
print(_list.pop())
_list.remove(6)
print()

#合并多个list为元组
_list01: list[int] = [1,2,3]
_list02: list[str] = ["Tom","Jerry"]
zipped: Iterator[tuple[int,str]] = zip(_list01,_list02)
print(list(zipped))

#列表推导式
"""
_list = [表达式 for i in range(5) if 条件]
"""
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']

_names = [name.upper() for name in names if len(name) > 3]
print(_names)

#切片
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
sliced: slice = slice(1,3)
print(names[sliced])

for name in islice(names,2):
    print(name)

#分批次
for name in batched(names,3):
    print(list(name))

#合并多个数据源
list_chain: Iterator[Any] = chain(_list01,_list02)
for index,value in enumerate(list_chain):
    print(index,value)

#分组
data = [('A', 90), ('B', 85), ('A', 88), ('C', 92)]
#先排序后分组
sorted_data: list[tuple[str,int]] = sorted(data, key=lambda x: x[0])
#分组
group_by: Iterator[tuple[str, Iterator[tuple[str, int]]]] = groupby(sorted_data, key=lambda x: x[0])
for key,group in group_by:
    print(key,list(group))

#多个list的笛卡尔积行列式
list03: list[int] = [1,2,3]
list04: list[int] = [4,5,6]
list05: list[int] = [7,8,9]

_product: Iterator[int] = product(list03,list04,list05)
print(list(_product))

#列表中的排列
list06: list[int] = [1,2,3,4]
_permutations: Iterator[int] = permutations(list06,3)
print(list(_permutations))

#列表中的组合
list07: list[int] = [1,2,3,4]
combinations: Iterator[int] = combinations(list07,3)
print(list(combinations))

#collection中的一些方法
#list的查询和修改很快，但是dequeue的插入和删除很快
list08:list[int] = [1,2,3,4,5]
_deque: deque[int] = deque(list08)
_deque.append(6)
_deque.appendleft(0)
print(_deque)
#计数
list09:list[str] = ['a','b','c','a','c']
counter: Counter[str] = Counter(list09)
print(counter)
#包装类
class Mylist(UserList):
    def append(self, item:Any):
        print(f"加入列表元素：{item}")
        super().append(item)
        print(f"加入元素:{item}成功")

mylist: Mylist[Any] = Mylist()
mylist.append(1)
print(mylist)
print(mylist.__contains__(1))