import pytest
"""
单次循环获取数据
多次循环获取数据
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

[('魔兽世界', '为了部落'), ('英雄联盟', '德玛西亚哈哈'), ('地平线', 'welcome backsir')]