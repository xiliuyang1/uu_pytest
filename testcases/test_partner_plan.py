from common.get_token import get_token
from utils.requests_util import RequestsUtil


class TestPartnerPlan:
    """
    明星合伙人计划
    /activity/partner-plan
    """

    def test_get_task_reward(self):
        url = "dev.uugamer.com/api/user/task/receive"
        params = {
            'task_id': 1110778204030906368,
            'history_id': 1112879980784099328}  # history_id  每次领取任务都会生成一个history_id
        token = get_token()
        headers = {'token': token}
        RequestsUtil.send_request()

