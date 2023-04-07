import logging

import allure
import pytest
import requests

from utils.requests_util import RequestsUtil
from utils.yaml_util import read_yaml, write_extract_yaml


def get_token():
    url = "http://dev.uugamer.com/api/user/phone/loginPassword"
    headers = {'content-type': 'application/x-www-form-urlencoded;charset=UTF-8', 'lang': 'zh-CN'}
    data = {
        'mobile': 18838035853,
        'password': 'qq111111',
        'source': 1,
        'ime': 'b195747cbb274a4f8d77aa9ba8a43077',
        'channel': 1}
    req = requests.request(method='post', url=url, headers=headers, data=data)
    print(req.json())
    token = req.json()['data']['token']
    print(token)
    return token


if __name__ == '__main__':
    get_token()
