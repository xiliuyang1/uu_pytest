import pytest

from utils.yaml_util import read_yaml


@pytest.fixture(scope="function")
def get_token():
    token = read_yaml('/test_data/common/token.yml')['token']
    return token
