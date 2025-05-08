#迭代器和生成器
from itertools import islice

_list: list[int] = [1,2,3,4,5]
iterator: iter = iter(_list)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

#生成器
def batch_handle_data(list_data: list[int], batch_size: int) -> list[list[int]]:
    """
    批量处理数据
    :param list_data:
    :param data: 数据
    :param batch_size: 批量大小
    :return:
    """
    for index in range(0, len(list_data), batch_size):
        yield list_data[index:index + batch_size]
        print("******")

for data in batch_handle_data(_list, 2):
    print(data)
    print(">>>>>>>>")


#使用生成器生成
"""
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
"""
#多个生成器yield一次执行完迭代器后再执行下一个yield
def create_data() ->list[int]:
    row: list[int] = [1]
    yield row
    while True:
        row: list[int] =  [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] +[1]
        yield row


def handle_data() -> list[list[int]]:
    result: list[list[int]] = []
    for l in islice(create_data(),10):
        result.append(l)
    return result

print(handle_data())
