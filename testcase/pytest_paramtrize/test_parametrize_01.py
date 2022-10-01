import pytest
"""
单次循环获取数据
多次循环获取数据

# 单次循环
@pytest.mark.parametrize("a",["b"])
def test_parametrize(a):
    print(a)
# 多次循环
@pytest.mark.parametrize("a,b",[("c","d"),("e","f")])
def test_parametrize(a,b):
    print(a,b)
"""

@pytest.mark.parametrize("name", ["test1"])
def test_parametrize_01(name):
    assert  name == "test1"

@pytest.mark.parametrize("name", ["test1", 'test2', 'test3'])
def test_parametrize_01(name):
    print(name)

# 一个参数，多个值 ，测试用例会把每个值赋给参数，进行测试用例的执行有的几个值就会执行几次；
@pytest.mark.parametrize("name1", ["test1", "test2","test3"])
def test_parametrize_02(name1):
    assert name1 == "test1"