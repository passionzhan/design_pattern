# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# PROJECT_NAME:         design_pattern
# Name:                 facede.py
# Author:               9824373
# Date:                 2020-08-25  19:43
# Contact:              9824373@qq.com
# Version:              V1.0
# Description:          外观模式
#-------------------------------------------------------------------------------       

class alarm_sensor:
    def run(self):
        print("Alarm Ring...")

class water_sprinker:
    def run(self):
        print("Spray Water...")

class emergency_dialer:
    def run(self):
        print("Dial 119...")

class emergency_facade:
    def __init__(self):
        self.alarm_sensor=alarm_sensor()
        self.water_sprinker=water_sprinker()
        self.emergency_dialer=emergency_dialer()

    def runAll(self):
        self.alarm_sensor.run()
        self.water_sprinker.run()
        self.emergency_dialer.run()



if __name__ == '__main__':

    emergency = emergency_facade()
    emergency.runAll()


