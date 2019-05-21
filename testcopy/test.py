#coding=utf-8


from Commonlib.Commonlib import Commonlib

co = Commonlib()

class Alert:

    def alert_html(self):
        co.openBrowser("file:///C:/Users/admin/Desktop/alert.html")
        co.activeEvent(".//*[@id='alert']")
        co.waite(2)
        co.dissMissAlter()
        co.waite(2)
        co.activeEvent(".//*[@id='alert']")
        co.waite(2)
        co.dissMissAlter()

mp = Alert()
mp.alert_html()














