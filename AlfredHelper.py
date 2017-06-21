#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Du'

from workflow import Workflow
import FBSimctrlTool
import sys

def showSimulatorList(wf):
    simulatorList = FBSimctrlTool.getSimulatorDescList(FBSimctrlTool.simulatorFileName)
    for line in simulatorList:
        subtitle = "按下回车删除此设备".encode('utf-8')
        wf.add_item(line, subtitle)
    wf.send_feedback()

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding("utf-8")
    wf = Workflow()
    sys.exit(wf.run(showSimulatorList))