#coding=utf-8
from Commonlib.Commonlib import Commonlib
import time as t
class Login:

    def __init__(self):
        self.p = Commonlib()

    def login_pub(self):
        self.p.openBrowser("http://10.168.103.151/web/#/login")
        self.p.waite(1)
        self.p.clearKeys(".//*[@class='el-input el-input-group el-input-group--prepend'][1]/input")
        self.p.waite(1)
        self.p.inputKeys(".//*[@class='el-input el-input-group el-input-group--prepend'][1]/input","admin")
        self.p.waite(1)
        self.p.clearKeys(".//*[@class='el-input el-input-group el-input-group--prepend'][2]/input")
        self.p.waite(1)
        self.p.inputKeys(".//*[@class='el-input el-input-group el-input-group--prepend'][2]/input","111111")
        self.p.waite(1)
        self.p.activeEvent(".//*[contains(text(),'立即登录')]")
if __name__ == '__main__':
    lo = Login()
    lo.login_pub()



















