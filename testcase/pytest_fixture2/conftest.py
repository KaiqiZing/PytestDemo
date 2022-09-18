# conftest.py
import requests
import pytest
@pytest.fixture(scope='function')
def get_token(request):
    token = 'qeehfjejwjwjej11sss@22'
    print('conftest中开始输出token:%s' % token)
    yield token
    print('conftest中结束输出token:%s' % token)
