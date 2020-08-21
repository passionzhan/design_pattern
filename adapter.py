# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# PROJECT_NAME:         design_pattern
# Name:                 adapter.py
# Author:               9824373
# Date:                 2020-08-19  15:24
# Contact:              9824373@qq.com
# Version:              V1.0
# Description:
#-------------------------------------------------------------------------------       

class Target(object):
    def request(self):
        print("普通请求")

class Adaptee(object):
    def specific_request(self):
        print("特殊请求")

class Adapter(Target):
    def __init__(self):
        self.adaptee = Adaptee()

    def request(self):
        self.adaptee.specific_request()

if __name__ == "__main__":
    target = Adapter()
    target.request()


