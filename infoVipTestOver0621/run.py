import os

import pytest

if __name__ == '__main__':
    pytest.main(['-sv','./test_case/login_test.py','--alluredir','allure-results','--clean-alluredir'])
    os.system('allure serve allure-results')

# 单接口测试
# excel里面做接口关联