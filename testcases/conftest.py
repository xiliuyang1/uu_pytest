import pytest

from common.get_token import set_token
from utils.yaml_util import clear_extract_yaml


@pytest.fixture(scope="session",autouse=True)
def setup():
    print("--------测试开始--------")
    set_token()
    yield
    clear_extract_yaml()
    print("--------测试结束--------")

