"""
operator内置模块
数学运算
add, mul, sub, truediv
比较运算
eq, gt, lt, ne
逻辑运算
and_, or_, not_
序列操作
concat, contains, countOf
元素操作
itemgetter, setitem, delitem
对象操作
attrgetter, methodcaller
"""
import itertools
import operator
from itertools import islice, dropwhile, zip_longest
from typing import Iterator

#无限迭代器
#1.生成无限序列
counter = itertools.count(start=0, step=1)
for data in islice(counter, 0, 10, 2):
    print(data)
#2.生成无限循环
list01:list[str] = ['W','A','N','G']
cycler = itertools.cycle(list01)
for data in islice(cycler, 0, 10):
    print(data)
#3.重复对象输出
list02:list[str] = ['W','A','N','G']
repeater = itertools.repeat(list02,10)
for data in repeater:
    print(data)

#终止迭代器
#1.累积计算
list02:list[int] = [1,3,5,7,9]
accumulator = itertools.accumulate(list02,operator.add)
print(list(accumulator))
#2.连接多个迭代器['W', 'A', 'N', 'G', 1, 2, 3, 4, 5]
list03:list[str] = ['W','A','N','G']
list04:list[int] = [1,2,3,4,5]
chainer = itertools.chain(list03,list04)
print(list(chainer))
#3.展开嵌套['w', 'a', 'n', 'g', 'j', 'i', 'a', 'n', 'c', 'h', 'a', 'o']
list05:list[str] = ['wang','jian','chao']
from_iterable = itertools.chain.from_iterable(list05)
print(list(from_iterable))
#4.按选择器过滤['W', 'N']
list06:list[str] = ['W','A','N','G']
compress = itertools.compress(list06,[True,False,True])
print(list(compress))
#5.条件为假时开始输出['N', 'G']
list07:list[str] = ['W','A','N','G']
drop_while = itertools.dropwhile(lambda x:x!='N',list07)
print(list(drop_while))
#6.过滤不符合条件的元素[6, 7, 8, 9]
list08:list[int] = [1,2,3,4,5,6,7,8,9]
filters = itertools.filterfalse(lambda x:x in list04,list08)
print(list(filters))
#7.分组
#分组
data = [('A', 90), ('B', 85), ('A', 88), ('C', 92)]
#先排序后分组
sorted_data: list[tuple[str,int]] = sorted(data, key=lambda x: x[0])
#分组
group_by: Iterator[tuple[str, Iterator[tuple[str, int]]]] = itertools.groupby(sorted_data, key=lambda x: x[0])
for key,group in group_by:
    print(key,list(group))
#8.展开映射[1, 81]
list09:list[tuple[int,int]] = [(1,2),(3,4)]
startMap = itertools.starmap(pow, list09)
print(list(startMap))
#9.条件为假时取值第一个元素就不满足则终止遍历[2]
list10:list[int] = [2,3,4,5]
takeWhile = itertools.takewhile(lambda x:x%2==0,list10)
print(list(takeWhile))
#10.克隆迭代器[1,2,3,4,5]
'''itertools.tee 是处理 流式数据多次访问 的核心工具，在需要 并行消费同一数据源 的场景中不可替代，但需注意内存管理和迭代器生命周期控制'''
list11:list[int] = [1,2,3,4,5]
list12,list13 = itertools.tee(list11)
print(list11)
#11.不等长压缩[(1, 'a'), (2, 'b'), (3, 'c'), (4, '-'), (5, '-')]
list14:list[int] = [1,2,3,4,5]
list15:list[str] = ['a','b','c']
zip_longest = itertools.zip_longest(list14,list15,fillvalue='-')
print(list(zip_longest))
#组合生成器
#1.笛卡尔积
'''
[(1, 'a', 'D'), (1, 'a', 'E'), (1, 'a', 'F'), (1, 'a', 'G'), (1, 'a', 'H'), (1, 'b', 'D'), (1, 'b', 'E'), (1, 'b', 'F'), (1, 'b', 'G'), (1, 'b', 'H'), (1, 'c', 'D'), (1, 'c', 'E'), (1, 'c', 'F'), (1, 'c', 'G'), (1, 'c', 'H'), (2, 'a', 'D'), (2, 'a', 'E'), (2, 'a', 'F'), (2, 'a', 'G'), (2, 'a', 'H'), (2, 'b', 'D'), (2, 'b', 'E'), (2, 'b', 'F'), (2, 'b', 'G'), (2, 'b', 'H'), (2, 'c', 'D'), (2, 'c', 'E'), (2, 'c', 'F'), (2, 'c', 'G'), (2, 'c', 'H'), (3, 'a', 'D'), (3, 'a', 'E'), (3, 'a', 'F'), (3, 'a', 'G'), (3, 'a', 'H'), (3, 'b', 'D'), (3, 'b', 'E'), (3, 'b', 'F'), (3, 'b', 'G'), (3, 'b', 'H'), (3, 'c', 'D'), (3, 'c', 'E'), (3, 'c', 'F'), (3, 'c', 'G'), (3, 'c', 'H'), (4, 'a', 'D'), (4, 'a', 'E'), (4, 'a', 'F'), (4, 'a', 'G'), (4, 'a', 'H'), (4, 'b', 'D'), (4, 'b', 'E'), (4, 'b', 'F'), (4, 'b', 'G'), (4, 'b', 'H'), (4, 'c', 'D'), (4, 'c', 'E'), (4, 'c', 'F'), (4, 'c', 'G'), (4, 'c', 'H'), (5, 'a', 'D'), (5, 'a', 'E'), (5, 'a', 'F'), (5, 'a', 'G'), (5, 'a', 'H'), (5, 'b', 'D'), (5, 'b', 'E'), (5, 'b', 'F'), (5, 'b', 'G'), (5, 'b', 'H'), (5, 'c', 'D'), (5, 'c', 'E'), (5, 'c', 'F'), (5, 'c', 'G'), (5, 'c', 'H')]
'''
list16:list[int] = [1,2,3,4,5]
list17:list[str] = ['a','b','c']
list18:list[str] = ['D','E','F','G','H']
product = itertools.product(list16,list17,list18)
print(list(product))
#2.排列有序
'''
[('D', 'E', 'F'), ('D', 'E', 'G'), ('D', 'E', 'H'), ('D', 'F', 'E'), ('D', 'F', 'G'), ('D', 'F', 'H'), ('D', 'G', 'E'), ('D', 'G', 'F'), ('D', 'G', 'H'), ('D', 'H', 'E'), ('D', 'H', 'F'), ('D', 'H', 'G'), ('E', 'D', 'F'), ('E', 'D', 'G'), ('E', 'D', 'H'), ('E', 'F', 'D'), ('E', 'F', 'G'), ('E', 'F', 'H'), ('E', 'G', 'D'), ('E', 'G', 'F'), ('E', 'G', 'H'), ('E', 'H', 'D'), ('E', 'H', 'F'), ('E', 'H', 'G'), ('F', 'D', 'E'), ('F', 'D', 'G'), ('F', 'D', 'H'), ('F', 'E', 'D'), ('F', 'E', 'G'), ('F', 'E', 'H'), ('F', 'G', 'D'), ('F', 'G', 'E'), ('F', 'G', 'H'), ('F', 'H', 'D'), ('F', 'H', 'E'), ('F', 'H', 'G'), ('G', 'D', 'E'), ('G', 'D', 'F'), ('G', 'D', 'H'), ('G', 'E', 'D'), ('G', 'E', 'F'), ('G', 'E', 'H'), ('G', 'F', 'D'), ('G', 'F', 'E'), ('G', 'F', 'H'), ('G', 'H', 'D'), ('G', 'H', 'E'), ('G', 'H', 'F'), ('H', 'D', 'E'), ('H', 'D', 'F'), ('H', 'D', 'G'), ('H', 'E', 'D'), ('H', 'E', 'F'), ('H', 'E', 'G'), ('H', 'F', 'D'), ('H', 'F', 'E'), ('H', 'F', 'G'), ('H', 'G', 'D'), ('H', 'G', 'E'), ('H', 'G', 'F')]
'''
permutations = itertools.permutations(list18,r=3)
print(list(permutations))
#3.组合无序
'''
[('D', 'E', 'F'), ('D', 'E', 'G'), ('D', 'E', 'H'), ('D', 'F', 'G'), ('D', 'F', 'H'), ('D', 'G', 'H'), ('E', 'F', 'G'), ('E', 'F', 'H'), ('E', 'G', 'H'), ('F', 'G', 'H')]
'''
combinations = itertools.combinations(list18,r=3)
print(list(combinations))
#4.带重复的组合
'''
[('D', 'D', 'D'), ('D', 'D', 'E'), ('D', 'D', 'F'), ('D', 'D', 'G'), ('D', 'D', 'H'), ('D', 'E', 'E'), ('D', 'E', 'F'), ('D', 'E', 'G'), ('D', 'E', 'H'), ('D', 'F', 'F'), ('D', 'F', 'G'), ('D', 'F', 'H'), ('D', 'G', 'G'), ('D', 'G', 'H'), ('D', 'H', 'H'), ('E', 'E', 'E'), ('E', 'E', 'F'), ('E', 'E', 'G'), ('E', 'E', 'H'), ('E', 'F', 'F'), ('E', 'F', 'G'), ('E', 'F', 'H'), ('E', 'G', 'G'), ('E', 'G', 'H'), ('E', 'H', 'H'), ('F', 'F', 'F'), ('F', 'F', 'G'), ('F', 'F', 'H'), ('F', 'G', 'G'), ('F', 'G', 'H'), ('F', 'H', 'H'), ('G', 'G', 'G'), ('G', 'G', 'H'), ('G', 'H', 'H'), ('H', 'H', 'H')]
'''
combinations_with_replacement = itertools.combinations_with_replacement(list18,r=3)
print(list(combinations_with_replacement))
#5.分批次[(1, 2, 3), (4, 5)]
list19:list[int] = [1,2,3,4,5]
batched = itertools.batched(list19,n=3)
print(list(batched))
#6.生成连续的元素对[(1, 2), (2, 3), (3, 4), (4, 5)]
list20:list[int] = [1,2,3,4,5]
pairwise = itertools.pairwise(list20)
print(list(pairwise))