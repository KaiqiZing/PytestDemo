import configparser
import os
import yaml
data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config", "data.yaml")
# ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config", "settings.ini")

class FileRead:
    def __init__(self):
        self.data_path = data_path
        # self.ini_path = ini_path

    def read_yaml_data(self):
        f = open(self.data_path, encoding='utf8')
        data = yaml.safe_load(f)
        print(data["mobile_belong_dict"])
        return data


get_data = FileRead()
get_data.read_yaml_data()
