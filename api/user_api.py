import pytest

from utils.requests_util import RequestsUtil
from utils.yaml_util import read_variable_yaml



def common_recharge(caseinfo):
    # 生成普通充值订单
    url = caseinfo['url']
    method = caseinfo['method']
    headers = read_variable_yaml(caseinfo['headers'])
    datas = caseinfo['datas']
    req = RequestsUtil().send_request(url=url, method=method, headers=headers, data=datas)
    return req


def activity_recharge(caseinfo, channel='4'):
    # 生成活动充值订单
    url = caseinfo['url']
    method = caseinfo['method']
    headers = read_variable_yaml(caseinfo['headers'])
    datas = caseinfo['datas']
    req = RequestsUtil().send_request(url=url, method=method, headers=headers, data=datas)
    return req


def set_recharge_order_success(order_id):
    # 活动页支付订单，手动设置为成功
    url = '/api/activity/activity/get-activity-by-code'
    datas = {
        'order_id': order_id,
        'out_trade_no': 111
    }
    req = RequestsUtil().send_request(url=url, method='post', headers='', data=datas)
    return req


if __name__ == '__main__':
    pytest.main(['-vs'])
