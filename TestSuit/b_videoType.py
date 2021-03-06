#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Bussniss.Bussniss import Bussniss
import unittest
import time

class TestVideoType(unittest.TestCase):
    def setUp(self):
        self.b = Bussniss()
        self.b.c.solveWaring()

    def test_001(self):
        """上传限制格式之外的视频格式"""
        try:
            self.assertEqual(
                self.b.LoadVideoType(
                    self.b.r.readxml("baseurl", "loadvideoUrl"),
                    self.b.r.readxml("login", "username"),
                    self.b.r.readxml("login", "password"),
                    self.b.r.readxml("videotype", "typetxt"))
                ,
                self.b.r.readxml("videotype", "alterText")
            )
        except Exception as e:

            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            pictfile = "../ErrorPict/"
            pictname = nowTime + 'a_videoType' + '.png'
            self.b.c.getScreenShot(pictfile+pictname)
            self.b.l.Logg(e)

    def tearDown(self):
        self.b.c.closeBrowser()


if __name__ == '__main__':
    unittest.main()
