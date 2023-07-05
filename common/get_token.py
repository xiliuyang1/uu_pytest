import requests

from utils.yaml_util import write_extract_yaml
from utils.requests_util import RequestsUtil


def set_token():
    name = "获取token"
    url = '/api/user/mail/login'
    method = 'post'
    headers = {
        'lang': 'zh-CN',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    data = {
        'source': 1,
        'ime': '97dd9609edd4c7bc52f36276c9cefd2b',
        'code': 8888,
        'mail': 'pytestceshi@gmail.com'

    }
    res = RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, data=data)
    values = {'token': res.json()['data']['token']}
    write_extract_yaml(values, "/common/token.yml")


if __name__ == '__main__':
    set_token()
