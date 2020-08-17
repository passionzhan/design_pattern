# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# PROJECT_NAME:         design_pattern
# Name:                 builder.py
# Author:               9824373
# Date:                 2020-08-15  16:49
# Contact:              9824373@qq.com
# Version:              V1.0
# Description:          建造模式
#-------------------------------------------------------------------------------       
from abc import ABC, ABCMeta, abstractmethod

class product(object):
    def __init__(self):
        self.parts = []

    def show(self):
        for part in self.parts:
            print(repr(part))

class builder(ABC):
    @abstractmethod
    def build_name(self):
        pass

    @abstractmethod
    def build_age(self):
        pass

    @abstractmethod
    def build_sex(self):
        pass

class undergraduate_builder(builder):
    def __init__(self):
        self.product = product()

    def build_name(self):
        self.product.parts.append('student')

    def build_age(self):
        self.product.parts.append(24)

    def build_sex(self,):
        self.product.parts.append('female')

class farmer_builder(builder):
    def __init__(self,):
        self.product = product()

    def build_name(self,):
        self.product.parts.append('farmer')

    def build_age(self,):
        self.product.parts.append(54)

    def build_sex(self,):
        self.product.parts.append('male')

class director(object):
    @classmethod
    def build(self,builder):
        builder.build_name()
        builder.build_age()
        builder.build_sex()

if __name__ == '__main__':
    student_builder = undergraduate_builder()
    farmer_builder = farmer_builder()

    director.build(student_builder)
    director.build(farmer_builder)
    student_builder.product.show()
    farmer_builder.product.show()








