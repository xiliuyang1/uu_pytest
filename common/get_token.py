import requests

from utils.yaml_util import write_extract_yaml
from utils.requests_util import RequestsUtil


def set_token():
    # caseinfo = {
    #     'name': "获取token",
    #     'url': '/api/user/phone/loginPassword',
    #     'method': 'post',
    #     'headers': {
    #         'lang': 'zh-CN',
    #         'content-type': 'application/x-www-form-urlencoded;charset=UTF-8'
    #     },
    #     'datas': {
    #         'source': 1,
    #         'ime': '97dd9609edd4c7bc52f36276c9cefd2b',
    #         'password': 'qq111111',
    #         'mobile': 18069776400
    #     }
    # }
    # name = caseinfo['name']
    # url = caseinfo['url']
    # headers = caseinfo['headers']
    # method = caseinfo['method']
    # data = caseinfo['datas']

    name = "获取token"
    url = '/api/user/phone/loginPassword'
    method = 'post'
    headers = {
        'lang': 'zh-CN',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    data = {
        'source': 1,
        'ime': '97dd9609edd4c7bc52f36276c9cefd2b',
        'password': 'qq111111',
        'mobile': 18838035853
    }
    # req=requests.post(url=url,headers=headers,data=data)
    # print(req.json())
    res = RequestsUtil().send_request(testcasename=name, method=method, url=url, headers=headers, data=data)
    values = {'token': res.json()['data']['token']}
    write_extract_yaml(values)

if __name__ == '__main__':
    set_token()