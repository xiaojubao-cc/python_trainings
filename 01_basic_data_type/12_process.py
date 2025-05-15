#进程
"""
在Windows中，由于没有fork(Linux中创建进程的机制)，在创建进程的时候会import启动该文件，
而在import文件的时候又会再次运行整个文件，如果把Process()放在 if __name__ == '__main__' 判断之外，
则Process()在被import的时候也会被运行，导致无限递归创建子进程导致报错，所以在Windows系统下，必须把Process()放在 if __name__ == '__main__' 的判断保护之下。
在子进程中不能使用input，因为输入台只显示在主进程中，故如果在子进程中使用input，会导致报错。
"""
import multiprocessing
import os
from multiprocessing import Process, Pool


def read_list(list_data: list[int]) -> None:
    print(f'子进程{os.getpid()}开始读取列表数据')
    for i in list_data:
        print(i)
    print(f'子进程{os.getpid()}读取列表数据结束')

def main():
    #使用Process
    # for _ in range(10):
    #     p = Process(target=read_list, args=([i for i in range(100000)],))
    #     p.start()
    #     p.join()

    #使用Pool
    """
    apply(func[, args[, kwds]])方法是阻塞，意味着当前的进程没有执行完的话，后续的进程需要等待该进程执行结束才能执行，实际上该方法是串行。

    apply_async(func[, args[, kwds[, callback[, error_callback]]]])方法是异步非阻塞的，意味着不用等待当前进程执行完成，即可根据系统的调度切换进程，该方法是并行。

    map(func, iterable[, chunksize])方法将iterable对象分成一些块，作为单独的任务提交给进程池。 这些块的（近似）大小可以通过将chunksize设置为正整数来指定，
    并且该方法是阻塞的。如果可迭代对象很多时，会消耗较大的内存，可以考虑使用imap或imap_unordered。

    map_async(func, iterable[, chunksize[, callback[, error_callback]]])方法是map的变种，是非阻塞的。

    imap(func, iterable[, chunksize])该方法和map一样，只不过该方法适用于对大量数据的遍历，返回的结果顺序和输入相同。

    imap_unordered(func, iterable[, chunksize])与imap()一样，只不过输出的顺序是任意的
    """
    with Pool(processes=4) as pool:
        for _ in range(10):
            #pool.apply_async(read_list, args=([i for i in range(100000)],))
            pool.map_async(read_list, ([i for i in range(100000)],),chunksize=1000)
            #pool.imap_unordered(read_list, ([i for i in range(100000)],))
            #pool.starmap_async(read_list, ([i for i in range(100000)],))
        pool.join()

    #进程同步
    with multiprocessing.Lock():
        print(f'主进程{os.getpid()}开始读取列表数据')
        for i in [i for i in range(100000)]:
            print(i)
        print(f'主进程{os.getpid()}读取列表数据结束')



if __name__ == '__main__':
    main()