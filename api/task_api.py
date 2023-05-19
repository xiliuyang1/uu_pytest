from utils.requests_util import RequestsUtil
from utils.yaml_util import read_variable_yaml


def sign_task(caseinfo):
    # 签到任务
    method = caseinfo['method']
    url = caseinfo['url']
    headers = read_variable_yaml(caseinfo['headers'])
    req = RequestsUtil().send_request(url=url, method=method, headers=headers)
    return req


def accept_task(caseinfo):
    # 领取任务
    method = caseinfo['method']
    url = caseinfo['url']
    headers = read_variable_yaml(caseinfo['headers'])
    datas = caseinfo['data']
    print(datas)
    req = RequestsUtil().send_request(url=url, method=method, headers=headers, data=datas)
    return req


def get_task_list(caseinfo):
    # 获取任务列表
    method = caseinfo['method']
    url = caseinfo['url']
    headers = read_variable_yaml(caseinfo['headers'])
    req = RequestsUtil().send_request(url=url, method=method, headers=headers)
    return req


def receive_task_reword():
    # 领取任务奖励
    pass


def get_task_receive_record():
    # 获取任务奖励领取记录
    pass
