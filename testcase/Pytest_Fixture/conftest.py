import pytest
# session独有的运行方式，第一需要创建运行文件夹下conftest.py,
#第二步 设置session函数
#第三步 执行命令: pytest -s testcase/Pytest_Fixture
@pytest.fixture(scope="session")
def test_sesssion():
    print("我是session的fixture")



# 前置步骤全部在conftest.py文件下做管理
@pytest.fixture(scope="function")
def function_conftest():
    print("function的前置步骤，conftest配置文件")
    yield "返回数据测试yield"
    print("function的后置步骤，conftest配置文件")



@pytest.fixture(scope="class")
def class_conftest():
    print("class的前置步骤，conftest配置文件")


@pytest.fixture(scope="module")
def module_conftest():
    print("module的前置步骤，conftest配置文件")
