#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from Commonlib.Commonlib import Commonlib
from Commonlib.Readxml import Readxml
from Bussniss.Bussniss import Bussniss
from Public.Public import PubLic
from Commonlib.Loggin import LoggIn
r = Readxml()
l  = LoggIn()

class LoginTatle(unittest.TestCase):
    l.Logg("this class name is LoginTatle")

    @classmethod
    def setUpClass(cls):
        pu = PubLic()
        cls.pu = pu
        cls.pu.login_pub(r.readxml("login","username"),r.readxml("login","password"))
        l.Logg("LoginTatle open broswer")

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()








