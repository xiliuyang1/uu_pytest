from api.user_api import mobile_login
from utils.log_util import LogUtil
from utils.yaml_util import write_extract_yaml


def set_token():
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
    return req.json()['data']['token']


def write_token_in_yaml():
    req = set_token()
    data = {'token': req}
    write_extract_yaml(data)
    # LogUtil().set_log().info("把{}写入token.yml文件中".format(data))