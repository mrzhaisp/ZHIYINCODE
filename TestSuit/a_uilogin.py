#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Bussniss.Bussniss import Bussniss
import unittest

class UiLoginTr(unittest.TestCase):
    def setUp(self):
        self.b = Bussniss()
        self.b.c.solveWaring()

    def tearDown(self):
        self.b.c.closeBrowser()

    def test_001(self):
        """是否能正常登录上去"""
        self.assertEqual(
            self.b.UiLogin(
                self.b.r.readxml("uilogin", "url"),
                self.b.r.readxml("uilogin", "usn"),
                self.b.r.readxml("uilogin", "pwd")),
                self.b.r.readxml("uilogin", "epect")
        )

if __name__ == '__main__':
    unittest.main()
