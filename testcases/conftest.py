import pytest

from common.get_token import write_token_in_yaml
from utils.yaml_util import clear_extract_yaml


@pytest.fixture(scope="session",autouse=True)
def setup():
    print("--------测试开始--------")
    write_token_in_yaml()
    yield
    clear_extract_yaml()
    print("--------测试结束--------")

