import requests
import pytest

# return 返回值的形式
@pytest.fixture()
def get_mobile():
    mobile = "13456755448"
    return mobile

def test_mobile(get_mobile):
    mobile = get_mobile
    print("测试手机归属地get请求")
    r = requests.get('https://api.binstd.com/shouji/query',
                     params={"shouji": mobile, "appkey": "0c818521d38759e1"})
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



if __name__ == '__main__':
    pytest.main()
