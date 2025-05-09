#文件操作
import os.path
from itertools import islice


def read_file():
    with open("D:\\python projects\\python_tranings\\01_basic_data_type\\nba.txt", "r+", encoding="utf-8",buffering=-1) as file:
        #读取一行数据
        for line in file.readlines():
            #yield必须在函数内使用
            yield line.strip()

def write_file(content:str):
    with open("D:\\python projects\\python_tranings\\01_basic_data_type\\nba.txt", "a+", encoding="utf-8",buffering=-1) as file:
        file.writelines(content)

write_file("\nStephen Curry|Golden State|12.0|PG|22.0|6-2|190.0|Louisville|1824360.0")

for content in islice(read_file(),0,None):
    print(content)