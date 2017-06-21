#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Du'

from workflow import Workflow

def main(wf):
    import FBSimctrlTool
    

result,error = FBSimctrlTool.addSimulator("614279E8-C81A-42BD-B6AE-F3591E26A322")
FBSimctrlTool.addSimulator("58B41543-C744-40FC-95E8-D47084A45B1F")
FBSimctrlTool.addSimulator("1020995A-7F8B-4C66-9551-889D81193D2F")
FBSimctrlTool.addSimulator("D329D8D6-EBB6-4FDF-865E-063F67D45CA1")
FBSimctrlTool.setAppPath("~/Library/Developer/Xcode/DerivedData/OneTouchPartner-gscwnthmhtmwekfthzrgxwihmnza/Build/Products/Debug-iphonesimulator/OneTouchPartner.app")
FBSimctrlTool.setAppBundleID("com.alibaba.onetouchpartner")
FBSimctrlTool.autoLaunchApp()
