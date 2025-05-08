#字符串的相关操作
_str: str = "hello world"
#首字母大写
print(f"首字母大写:{_str.capitalize()}")
#返回指定长度的字符串并以指定字符填充
print(f"指定字符填充:{_str.center(20,'*')}")
#返回指定字符在个数
print(f"指定字符出现次数:{_str.count("l")}")
#查询指定字符第一次出现的索引位置
print(f"指定字符出现的首次索引位置:{_str.find("l")}")
#判断字符是否包含字母和数字
_str: str = "hello123"
print(f"指定字符是否只包含数字和字母:{_str.isalnum()}")
#判断字符串是否只包含字母和汉字
_str: str = "hello你好"
print(f"指定字符是否只包含字母和汉字:{_str.isalpha()}")
#判断字符串是否只包含数字
_str: str = "123"
print(f"指定字符是否只包含数字:{_str.isdigit()}")
#以指定分隔符分割字符串
_str: str = "hello|world"
print(f"指定字符分割字符串:{_str.split('|')}")
#以指定字符拼接字符串
_str: str = "hello world"
print(f"指定字符串拼接:{"-".join(_str.split())}")
#去掉字符中的左右的空格
_str: str = " hello world "
print(f"去掉字符串中的空格:{_str.strip()}")
#字符串左右填充
_str: str = "1111"
print(f"给指定字符串左填充:{_str.ljust(10,'0')}")
print(f"给指定字符串右填充:{_str.rjust(10,'0')}")
print(f"给指定字符串左填充0:{_str.zfill(10)}")