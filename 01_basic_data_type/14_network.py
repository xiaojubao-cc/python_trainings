#网络请求
import requests
from requests import Response
with requests.get("https://www.hupu.com") as _response:
    print(f"响应时间:{_response.elapsed}")
    print(f"状态码信息:{_response.status_code}")
    print(f"文本信息:{_response.text}")
    print(f"响应头信息:{_response.headers}")
    print(f"响应类容信息:{_response.content}")