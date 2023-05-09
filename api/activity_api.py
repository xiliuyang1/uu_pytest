import pytest

from utils.requests_util import RequestsUtil


# 获取活动的基本信息
from utils.yaml_util import read_variable_yaml


def get_activity_base_datas(caseinfo, activity_code):
    url = caseinfo['url']
    method = caseinfo['method']
    headers = read_variable_yaml(caseinfo['headers'])
    params = {"code": activity_code}
    req = RequestsUtil().send_request(url=url, method=method, headers=headers, data=params)
    return req

# 获取活动盲盒详情数据
def get_lucky_cases_datas(caseinfo, cases_code):
    url = caseinfo['url']
    method = caseinfo['method']
    headers = read_variable_yaml(caseinfo['headers'])
    params = {"code": cases_code}
    req = RequestsUtil().send_request(url=url, method=method, headers=headers, data=params)
    return req