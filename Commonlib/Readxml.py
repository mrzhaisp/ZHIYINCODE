#!/usr/bin/env python
# -*- coding: utf-8 -*-
from xml.dom import minidom

class Readxml:

    def readxml(self,oneNode,twonode):

        """找到本地的xml文件"""
        root = minidom.parse("../Data/Data.xml")
        #找到第一个节点
        firstnode = root.getElementsByTagName(oneNode)[0]

        #找到节点下的子节点里的值
        secondnode = firstnode.getElementsByTagName(twonode)[0].firstChild.data
        return secondnode

# if __name__ == '__main__':
#     r = Readxml()
#     print(r.readxml("login","password"))




























