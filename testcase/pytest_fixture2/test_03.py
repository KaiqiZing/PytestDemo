# test_03.py
import pytest

class Test(object):
    def test3(self, get_token):
        token = 'qeehfjejwjwjej11sss@22'
        print("【执行test03.py-Test类-test3用例,获取get_token：%s】" % get_token)
        assert get_token == token

    def test4(self, get_token):
        token = 'qeehfjejwjwjej11sss@22'
        print("【执行test03.py-Test类-test4用例,获取get_token：%s】" % get_token)
        assert get_token == token

