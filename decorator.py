# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# PROJECT_NAME:         design_pattern
# Name:                 decorator.py
# Author:               9824373
# Date:                 2020-08-22  21:51
# Contact:              9824373@qq.com
# Version:              V1.0
# Description:          修饰器模式，设计迭代递归函数，提高计算性能
#-------------------------------------------------------------------------------       

from functools import wraps

class component(object):
    def __init__(self,name):
        self.name = name

    def operator(self):
        print('我是component抽象类，名字为：' + self.name)

class concrete_component_a(component):
    def operator(self):
        print('我具体component类，名字为：' + self.name)

class decorator_base(component):
    def __init__(self,name,component):
        super(decorator_base, self).__init__(name)  # 此处修改了
        self.component = component

    def operator(self):
        # print('我decorator_base类，名字为：' + self.name)
        self.component.operator()

class decorator_a(decorator_base):
    def operator(self):
        print('我decorator_a类，名字为：' + self.name)
        self.component.operator()
        # super(decorator_a,self).operator()

class decorator_b(decorator_base):
    def operator(self):
        print('我decorator_b类，名字为：' + self.name)
        self.component.operator()

class decorator_c(decorator_base):
    def operator(self):
        print('我decorator_c类，名字为：' + self.name)
        self.component.operator()


def memoize(fn):
    known = dict()
    @wraps(fn)
    def memoizer(*args):
        if args not in known:
            known[args] = fn(*args)
        return known[args]
    return memoizer

@memoize
def nsum(n):
    '''返回前n个数字的和'''
    assert(n >= 0), 'n must be >= 0'
    return 0 if n == 0 else n + nsum(n-1)

@memoize
def fibonacci(n):
    '''返回字典记忆(dp)斐波那契数列的第n个数'''
    assert(n >= 0), 'n must be >= 0'
    return n if n in (0, 1) else fibonacci(n-1) + fibonacci(n-2)

def fibonacci_org(n):
    '''返回斐波那契数列的第n个数'''
    assert(n >= 0), 'n must be >= 0'
    return n if n in (0, 1) else fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    '''
    from timeit import Timer
    measure = [ {'exec':'fibonacci(400)', 'import':'fibonacci',
    'func':fibonacci},{'exec':'nsum(200)', 'import':'nsum',
    'func':nsum},{'exec':'fibonacci_org(400)', 'import':'fibonacci_org',
    'func':fibonacci_org},]
    for m in measure:
        t = Timer('{}'.format(m['exec']), 'from __main__ import {}'.format(m['import']))
        print('name: {}, doc: {}, executing: {}, time:{}'.format(m['func'].__name__, m['func'].__doc__,m['exec'], t.timeit()))
    '''

    # t = Timer('{}'.format('fibonacci_org(200)'), 'from __main__ import {}'.format('fibonacci_org'))
    # print('name: {}, doc: {}, executing: {}, time:{}'.format(fibonacci_org.__name__, fibonacci_org.__doc__,'fibonacci_org(200)', t.timeit()))

    zhan = concrete_component_a('zhan')
    a_zhan = decorator_a('a_',zhan)
    b_zhan = decorator_b('b_',a_zhan)
    b_zhan.operator()


    c_zhan = decorator_c('c_',zhan)
    a_zhan = decorator_a('a_', c_zhan)
    a_zhan.operator()
