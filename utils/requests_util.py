import json

import requests


class RequestsUtil:
    session = requests.session()

    def send_request(self, method, url, data, **kwargs):
        method = str(method).lower()
        if method == 'get':
            # print(method)
            res = RequestsUtil.session.request(method=method, url=url, params=data, **kwargs)
        else:
            # print(method)
            datas = json.dumps(data)  # 序列化，不知道data是什么格式，所以统一转换成字符串格式，通过data方式传参
            res = RequestsUtil.session.request(method=method, url=url, data=data, **kwargs)
        return res

# def test_resign_email():
#     url = 'http://dev.uugamer.com/api/user/mail/register'
#     data = {
#         'mail': '123a96@gmail.com',
#         'code': 8888,
#         'password': 'qq111111',
#         'mobile_code': +86,
#         'source': 1
#     }
#     headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8', 'lang': 'zh-CN'}
#     rq = RequestsUtil().send_request(method='post', url=url, data=data, headers=headers)
#     print(rq.json())
#
#
# if __name__ == '__main__':
#     test_resign_email()
