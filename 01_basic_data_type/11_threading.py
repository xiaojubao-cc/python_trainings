#多线程操作
import os
import threading

from concurrent.futures import ThreadPoolExecutor
from fontTools.misc.iterTools import batched


def read_list(list_data: list[int]):
    for item in list_data:
        print(f"线程{threading.current_thread().name} is reading consumer:{item}")

list01: list[int] = [1,2,3,4,5,6,7,8,9,10]

thread01: threading.Thread = threading.Thread(target=read_list, args=(list01,),name="Customize01")
thread02: threading.Thread = threading.Thread(target=read_list, args=(list01,),name="Customize02")
print(f">>>>>{thread01.ident}")
thread01.start()
print(f">>>>>{thread01.ident}")
thread02.start()
thread01.join()
thread02.join()
print("main thread")


#创建一个线程池
with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(read_list, list(batched(list01, 1)))

#线程同步
with threading.Lock():
    print(f'线程{os.getpid()}开始读取列表数据')
    for i in [i for i in range(100000)]:
        print(i)
    print(f'线程{os.getpid()}读取列表数据结束')

#threadlocal线程本地存储