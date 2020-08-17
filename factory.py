# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# PROJECT_NAME:         design_pattern
# Name:                 factory.py
# Author:               9824373
# Date:                 2020-08-15  10:37
# Contact:              9824373@qq.com
# Version:              V1.0
# Description:          工厂模式
#-------------------------------------------------------------------------------       

class operator(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def get_result(self):
        rst = 0
        return rst

class add_operator(operator):
    def get_result(self):
        return self.a + self.b

class minus_operator(operator):
    def get_result(self):
        return self.a - self.b

class operator_factory(object):
    operator_symbol = {'+':add_operator,
                       '-':minus_operator,
                       }

    # def __init__(self):
    @classmethod
    def get_operator(cls,type,a,b):
        return cls.operator_symbol.get(type)(a,b)


if __name__ == '__main__':
    a = operator_factory.get_operator('+', 4, 98).get_result()
    rst = operator_factory.get_operator('-',a,71).get_result()
    print(rst)

