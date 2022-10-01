import pytest
"""
单次循环获取数据
多次循环获取数据

# 单次循环
@pytest.mark.parametrize("a",["b"])
def test_parametrize(a):
    print(a)
# 多次循环˚
@pytest.mark.parametrize("a,b",[("c","d"),("e","f")])
def test_parametrize(a,b):
    print(a,b)
"""
#数组的形式，元组也可以使用
# 一个参数，多个值 ，多值部分是可迭代的就行不管是数组还是元组
# @pytest.mark.parametrize("game, word", [['魔兽世界', '为了部落数组'], ['英雄联盟', '德玛西亚哈哈'], ['地平线', 'welcome backsir']])
# def test_parametrize_02(game, word):
#     print(f'{game}的主题是数组参数--{word}')

@pytest.mark.parametrize("game, word", [('魔兽世界', '为了部落元组'), ('英雄联盟', '德玛西亚哈哈'), ('地平线', 'welcome backsir')])
def test_parametrize_02(game, word):
    print(f'{game}的主题是元组参数--{word}')


#game--魔兽世界
#word--为了部落
# 参数值为字典形式的操作：
# @pytest.mark.parametrize("mygame", [{"game":'魔兽世界', "word":'为了部落字典'}, {"game":'英雄联盟', "word":'德玛西亚哈哈'}, {"game":'地平线', "word":'welcome backsir'}])
# def test_parametrize_02(mygame):
#     print(mygame["game"])
#     print(mygame["word"])