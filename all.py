import os
import time
import pytest

if __name__ == '__main__':
    pytest.main()
    time.sleep(1)
    os.system('allure generate reports/temps -o reports/allues --clean')
# 加上--clean标识每执行一次都会把原来的文件清除
