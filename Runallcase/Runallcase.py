#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from Commonlib.CreateReporter import CreateReporter
c = CreateReporter()

class Tsuit(unittest.TestCase):
    def testT(self):
        #找到测试案例的路径
        case_dir = '../TestSuit'

        #加载测试案例
        discover = unittest.defaultTestLoader.discover(case_dir,pattern="*.py",top_level_dir=None)

        #把测试案例传给reporter
        c.create_report(discover)

    def runTest(self):
        pass


if __name__ == '__main__':
    unittest.main()





















