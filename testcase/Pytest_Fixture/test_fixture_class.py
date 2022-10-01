import requests
import pytest
"""
Autouse--usage
If True, the fixture func is activated for all tests that can see it.
If False (the default), an explicit reference is needed to activate
the fixture.
"""
# scope 默认方法是function
@pytest.fixture(scope="class", autouse=False)  # auto=True=, 每个类都执行一次，auto=False需要单独调用激活函数
def func_method():
    print("这是class的前置方法")


class TestFixture_First:
    def test_mobile(self, func_method):  # auto=False
        print("测试手机归属地get请求")
        r = requests.get('https://api.binstd.com/shouji/query',
                         params={"shouji": "13456755448", "appkey": "0c818521d38759e1"})
        print(r.status_code)
        assert r.status_code == 200
        result = r.json()
        assert result['status'] == 0
        assert result['msg'] == "ok"
        assert result['result']["shouji"] == "13456755448"
        assert result['result']["province"] == "浙江"
        assert result['result']["city"] == "杭州"
        assert result['result']["company"] == "中国移动"
        assert result['result']["cardtype"] is None
        assert result['result']["areacode"] == "0571"

class TestFixture_Second:

    def test_mobile_post(self):
        print("测试手机归属地post请求")
        params = {
            "shouji": "13456755448",
            "appkey": "0c818521d38759e1"
        }
        r = requests.post('https://api.binstd.com/shouji/query', params=params)
        assert r.status_code == 200
        result = r.json()
        assert result['status'] == 0
        assert result['msg'] == "ok"
        assert result['result']["shouji"] == "13456755448"
        assert result['result']["province"] == "浙江"
        assert result['result']["city"] == "杭州"
        assert result['result']["company"] == "中国移动"
        assert result['result']["cardtype"] is None
        assert result['result']["areacode"] == "0571"


if __name__ == '__main__':
    pytest.main()
