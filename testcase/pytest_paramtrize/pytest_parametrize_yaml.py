import pytest
from utils.read_yaml import get_data
get_datas = get_data.read_yaml_data()

# 单参数
@pytest.mark.parametrize("name", get_datas['heros_name'])
def test_parametrize_02(name):
    print(name)
# 多参数
@pytest.mark.parametrize("name,word", get_datas['heros_name_word'])
def test_parametrize_02(name, word):
    print(f'{name}的台词是{word}')