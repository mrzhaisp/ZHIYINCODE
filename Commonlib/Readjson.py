#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json


class OpertionJson:
    '''拿到文件路径'''

    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path = '../Data/Data.json'
        else:
            self.file_path = file_path
        self.data = self.read_json()

    def read_json(self):
        """拿到json的所有数据"""
        with open(self.file_path) as f:
            data = json.load(f)
            return data

    def get_data(self, id, ):
        """拿到data数据 然后根据id取出来value值"""
        return self.data[id]

# if __name__ == '__main__':
#     ol = OpertionJson()
#     data_load = ol.get_data("loginusername")
#     data_load2 = ol.get_data("loginpwd")
#     # print(data_load["username"])
#     print(data_load,data_load2)
