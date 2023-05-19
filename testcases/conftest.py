import pytest

from common.get_token import set_token
from utils.yaml_util import clear_extract_yaml, read_yaml


@pytest.fixture(scope="session",autouse=True)
def setup():
    clear_list = read_yaml('/common/cache_file_list.yml')
    print(clear_list)
    for item in clear_list:
        clear_extract_yaml(item)
    set_token()
    print("--------测试开始--------")

    yield
    print("--------测试结束--------")

