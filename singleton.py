# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# PROJECT_NAME:         design_pattern
# Name:                 singleton.py
# Author:               9824373
# Date:                 2020-08-14  22:41
# Contact:              9824373@qq.com
# Version:              V1.0
# Description:          单例模式
#-------------------------------------------------------------------------------       


class singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self,name,age,edu):
        self.name = name
        self.age = age
        self.edu = edu

if __name__ == '__main__':
    a = singleton('zhan',24,'famale')
    b = singleton('zhang',20,'male')
    print(a)
    print(b)
    print(a.name,a.age,a.edu)
    print(b.name,b.age,b.edu)



