import logging
from logging.handlers import RotatingFileHandler

# 详细日志格式配置
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s.%(msecs)03d | '  # 精确到毫秒的时间戳
           '%(process)d:%(threadName)s | '  # 进程与线程信息
           '%(name)-12s | '  # logger名称（固定12字符宽度）
           '%(levelname)-8s | '  # 日志级别（固定8字符宽度）
           '%(filename)s:%(lineno)d | '  # 文件名与行号
           '%(funcName)s() | '  # 函数名称
           '%(message)s',  # 日志内容
    datefmt='%Y-%m-%d %H:%M:%S',  # 时间格式
    handlers=[
        logging.StreamHandler(),
        RotatingFileHandler(
            'app.log',
            maxBytes=1024*1024,
            backupCount=5
        )
    ]
)

logging.info('hello world')