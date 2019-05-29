#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
# sys.getdefaultencoding() != 'utf-8'
# reload(sys)
# sys.setdefaultencoding('utf-8')
import HTMLTestRunnerNew

class CreateReporter:
    """制作测试报告，把执行的结果传进来，discover方法执行的用例结果传进去"""

    def create_report(self, mysuit):
        filepath = "../Reporter/151_selenium_UI_report.htm"
        with open(filepath, "wb") as f:
            HTMLTestRunnerNew.HTMLTestRunner(
                stream=f,
                verbosity=2,
                title="151--声像情报分析系统测试报告",
                description="声像情报分析系统UI自动化测试"
            ).run(mysuit)
