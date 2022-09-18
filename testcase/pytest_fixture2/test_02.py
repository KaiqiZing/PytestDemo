# test_02.py
import pytest

class Test(object):
    def test2(self, get_token):
        token = 'qeehfjejwjwjej11sss@'
        print("【执行test02.py-Test类-test2用例,获取get_token：%s】" % get_token)
        assert get_token == token
class Test01(object):
    def test_01(self, get_token):
        token = 'qeehfjejwjwjej11sss@22'
        print("【执行test02.py-Test类-test2用例,获取get_token：%s】" % get_token)
        assert get_token == token
if __name__ == '__main__':
    pytest.main()