import json

import requests


class RequestsUtil:
    session = requests.session()

    def send_request(self, method, url, data, **kwargs):
        method = str(method).lower()
        if method == 'get':
            # print(method)
            res = RequestsUtil.session.request(method=method, url=url, params=data, **kwargs)
            return res
        elif method == 'post':
            # print(method)
            datas = json.dumps(data)  # 序列化，不知道data是什么格式，所以统一转换成字符串格式，通过data方式传参
            res = RequestsUtil.session.request(method=method, url=url, data=data, **kwargs)
            return res
