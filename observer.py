# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# PROJECT_NAME:         design_pattern
# Name:                 observer.py
# Author:               Administrator
# Date:                 2020-08-31  16:08
# Contact:              9824373@qq.com
# Version:              V1.0
# Description:          观察者模式（发布/订阅模式）
#-------------------------------------------------------------------------------       

import abc

class subject(metaclass=abc.ABCMeta):
    observers = []
    action = ""

    @abc.abstractmethod  # 定义抽象方法，无需实现功能
    def attach(self):
        pass

    @abc.abstractmethod  # 定义抽象方法，无需实现功能
    def detach(self, observer):
        pass

    @abc.abstractmethod  # 定义抽象方法，无需实现功能
    def notity(self):
        pass

class boss(subject):
    observers = []
    action = ""

    def __init__(self,action):
        self.action = action

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notity(self):
        for observer in self.observers:
            observer.update()

class secretary(subject):
    '''

    '''
    observers = []
    action = ""

    def __init__(self,action):
        self.action = action

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notity(self):
        for observer in self.observers:
            observer.update()

class observer(metaclass=abc.ABCMeta):
    '''
    观察者抽象类
    '''
    @abc.abstractmethod
    def update(self):
        pass

class stock_observer(observer):
    '''
    股票观察者
    '''
    def __init__(self,name,sub):
        self.name = name
        self.sub = sub

    def update(self):
        print('通知者发布了{0}通知。'.format(self.sub.action))
        print(self.name  +  "关闭股票窗口！")

class nba_observer(observer):
    '''
    nba观察者
    '''
    def __init__(self,name,sub):
        self.name = name
        self.sub = sub

    def update(self):
        print('通知者发布了{0}通知。'.format(self.sub.action))
        print(self.name  +  "关闭NBA窗口！")


if __name__ == '__main__':
    boss_a = boss("开会！")
    secretary_xiaomei = secretary("老板要回来了")

    stock_observer_a = stock_observer("ZHAN",boss_a)
    nba_observer_a = nba_observer("LIU",boss_a)

    boss_a.attach(stock_observer_a)
    boss_a.attach(nba_observer_a)

    boss_a.notity()

    stock_observer_b = stock_observer('WANG', secretary_xiaomei)
    nba_observer_b = nba_observer('GAO', secretary_xiaomei)

    secretary_xiaomei.attach(stock_observer_b)
    secretary_xiaomei.attach(nba_observer_a)
    secretary_xiaomei.attach(nba_observer_b)
    secretary_xiaomei.detach(nba_observer_a)

    secretary_xiaomei.notity()










