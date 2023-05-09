import pytest

from utils.requests_util import RequestsUtil
from utils.yaml_util import read_yaml, read_extract_yaml, write_extract_yaml, read_variable_yaml


def mobile_login(caseinfo):
    url = caseinfo['url']
    headers = caseinfo['headers']
    method = caseinfo['method']
    json = caseinfo['datas']
    req = RequestsUtil().send_request(method=method, url=url, headers=headers, data=json)
    return req


def quit_login(caseinfo):
    method = caseinfo['method']
    headers = read_variable_yaml(caseinfo['headers'])
    url = caseinfo['url']
    print(headers)
    req = RequestsUtil().send_request(method=method, url=url, headers=headers)
    return req


def get_token():
    caseinfo = {
        'url': '/api/user/phone/loginPassword',
        'method': 'post',
        'headers': {
            'lang': 'zh-CN',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8'
        },
        'datas': {
            'source': 1,
            'ime': '97dd9609edd4c7bc52f36276c9cefd2b',
            'password': 'qq111111',
            'mobile': 18069776400
        }
    }
    req = mobile_login(caseinfo)
    data = {'token': req.json()['data']['token']}
    write_extract_yaml(data, file_name="/common/token.yml")
    token = read_yaml('/common/token.yml')['token']
    return token


def common_recharge(caseinfo):
    url = caseinfo['url']
    method = caseinfo['method']
    headers = read_variable_yaml(caseinfo['headers'])
    datas = caseinfo['datas']
    req = RequestsUtil().send_request(url=url, method=method, headers=headers, data=datas)
    return req


def activity_recharge(caseinfo, channel='4'):
    url = caseinfo['url']
    method = caseinfo['method']
    headers = read_variable_yaml(caseinfo['headers'])
    datas = caseinfo['datas']
    req = RequestsUtil().send_request(url=url, method=method, headers=headers, data=datas)
    return req


def set_recharge_order_success(order_id):
    url = '/api/activity/activity/get-activity-by-code'
    datas = {
        'order_id': order_id,
        'out_trade_no': 111
    }
    req = RequestsUtil().send_request(url=url, method='post', headers='', data=datas)
    return req


def sign_task(caseinfo):
    # print(caseinfo)
    method = caseinfo['method']
    url = caseinfo['url']
    headers = read_variable_yaml(caseinfo['headers'])
    # print(headers)
    req = RequestsUtil().send_request(url=url, method=method, headers=headers)
    return req


if __name__ == '__main__':
    pytest.main(['-vs'])
