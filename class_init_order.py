# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# PROJECT_NAME:         design_pattern
# Name:                 class_init_order.py
# Author:               9824373
# Date:                 2020-08-14  16:42
# Contact:              9824373@qq.com
# Version:              V1.0
# Description:          python类  初始化时的执行顺序
#-------------------------------------------------------------------------------       

class MyObject(object):
    _instance = None
    print('B')

    def __new__(cls, *args, **kwargs):
        print('F')
        # cls._instance = 'G'
        return super(MyObject,cls).__new__(cls)

    def __init__(self, name):
        print('C')
        self.name = name
        print('D')
        # print(MyObject._instance)

if __name__ == '__main__':
    print('A')

    print('E')
    my_object1 = MyObject('Hello')
    my_object1 = MyObject('xxxxxx')

