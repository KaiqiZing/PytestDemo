import pytest
# pytest中的params and IDs的用法
@pytest.fixture(params=["data1","data2"], ids=["case1", "case2"])
def params_fixtures(request):
    return request.param


def test_params(params_fixtures):
    print(params_fixtures)
