#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Bussniss.Bussniss import Bussniss
import unittest
import time

class UiLoginTr(unittest.TestCase):
    def setUp(self):
        self.b = Bussniss()
        self.b.c.solveWaring()

    def tearDown(self):
        self.b.c.closeBrowser()

    def test_001(self):
        """是否能正常登录上去"""
        try:
            self.assertEqual(
                self.b.UiLogin(
                    self.b.r.readxml("uilogin", "url"),
                    self.b.r.readxml("uilogin", "usn"),
                    self.b.r.readxml("uilogin", "pwd")),
                    self.b.r.readxml("uilogin", "epect")
            )
        except Exception as e:
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            pictfile = "../ErrorPict/"
            pictname = nowTime + 'a_uilogin' + '.png'
            self.b.c.getScreenShot(pictfile+pictname)
            self.b.l.Logg(e)
            print (e)

if __name__ == '__main__':
    unittest.main()
