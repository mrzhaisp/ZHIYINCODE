#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Commonlib.Readxml import Readxml
from Bussniss.Bussniss import Bussniss
import unittest
from Commonlib.Commonlib import Commonlib

class PublicPeopleLib(unittest.TestCase):
    def setUp(self):
        self.b = Bussniss()
        self.r = Readxml()
        self.c = Commonlib()
        self.c.solveWaring()

    def tearDown(self):
        self.b.pu.pub.closeBrowser()

    def test_001(self):
        u"""点击人物库，跳转到知名人物页面"""
        self.assertEqual(
            self.b.login_people_lib(self.r.readxml("renwuku","username"),
                                    self.r.readxml("renwuku","password")),
                                    self.r.readxml("renwuku","epxect")
        )
if __name__ == '__main__':
    unittest.main()





















































