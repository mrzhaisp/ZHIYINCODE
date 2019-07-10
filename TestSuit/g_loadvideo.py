#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Bussniss.Bussniss import Bussniss
import unittest
import time

class loadvideo(unittest.TestCase):
    """上传视频"""
    def setUp(self):
        self.b = Bussniss()
        self.b.c.solveWaring()

    def tearDown(self):
        self.b.c.waite(20)
        self.b.c.closeBrowser()

    def test_001(self):
        """上传符合格式的视频"""
        try:
            self.assertEqual(
                self.b.LoadVideo(),
                self.b.r.readxml("loadvideo","text")
            )
        except Exception as e:
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            pictfile = "../ErrorPict/"
            pictname = nowTime + 'g_loadvideo' + '.png'
            self.b.c.getScreenShot(pictfile + pictname)
            self.b.l.Logg(e)

if __name__ == '__main__':
    unittest.main()

