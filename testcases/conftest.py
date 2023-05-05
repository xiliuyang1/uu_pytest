import pytest

from common.get_token import get_token
from utils.yaml_util import read_yaml, clear_extract_yaml


@pytest.fixture(scope="function")
def login_token():
    token = get_token()
    yield token
    # clear_extract_yaml()

