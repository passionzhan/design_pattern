# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# PROJECT_NAME:         design_pattern
# Name:                 factory_method.py
# Author:               9824373
# Date:                 2020-08-18  08:36
# Contact:              9824373@qq.com
# Version:              V1.0
# Description:          工厂方法类
#-------------------------------------------------------------------------------       

from factory import operator,add_operator,minus_operator

class operator_factory(object):
    """
    工厂类operator_factory为抽象的工厂类，而add_factory，add_factory为具体的工厂类。
    """
    type = ""
    def create_operator(self,operator,param_a,param_b):
        print(self.type," factory produce a instance.")
        operator_instance=operator(param_a,param_b)
        return operator_instance

class add_factory(operator_factory):
    def __init__(self):
        self.type = 'add_operator factory'

class minus_factory(operator_factory):
    def __init__(self):
        self.type = 'minus_operator factory'

if __name__ == '__main__':
    add_factory_instance = add_factory()
    minus_operator_instance = minus_factory()
    add_operator_instance = add_factory_instance.create_operator(add_operator,4, 98)
    param_a = add_operator_instance.get_result()
    rst = minus_operator_instance.create_operator(minus_operator,param_a,71).get_result()
    print(rst)


