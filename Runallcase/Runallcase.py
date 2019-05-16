#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import sys
import time
from Commonlib.CreateReporter import CreateReporter
from Commonlib.SendEmail import SendEmail
c = CreateReporter()
s = SendEmail()

class Tsuit(unittest.TestCase):
    def testT(self):
        #找到测试案例的路径
        case_dir = '../TestSuit'

        #加载测试案例
        discover = unittest.defaultTestLoader.discover(case_dir,pattern="*.py",top_level_dir=None)

        #把测试案例传给reporter
        c.create_report(discover)
        # s.sendmail("../Reporter/151test_UI_report.htm")
        # for i in range(100):
        #     k = i + 1
        #     str = '/' * i + '' * (100 - k)
        #     sys.stdout.write('\r' + str + '[%s%%]' % (i + 1))
        #     sys.stdout.flush()
        #     time.sleep(0.05)
        # print(u"Emal send----->%100")

    def runTest(self):
        # 原因是因为sub_class里缺少runTest方法，不加上该方法，上边的tetsT会报错，直接在Tsuit的类中增加
        pass


if __name__ == '__main__':
    unittest.main()





















