#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

__author__ = 'Du'

import sys

# query = sys.argv[1]


simulatorFileName = "simulators"
appPathFileName = "appPath"
appBundleIDFileName = "bundleID"

simulatorDescSeparator = '|'
fbCommand = '/usr/local/bin/fbsimctl'

def addSimulator(simulatorID):
    if len(simulatorID) == 0:
        print("设备ID不能为空")
        return
    simListReader = os.popen('%s list' % fbCommand)
    simList = simListReader.readlines()
    foundSimulatorID = False


    for line in simList:
        if line.startswith(simulatorID):
            foundSimulatorID = True
            parts = line.split(simulatorDescSeparator)
            writeText = "%s %s %s %s %s" % (parts[0], simulatorDescSeparator, parts[1], simulatorDescSeparator, parts[4])

            #重复判断
            if os.path.isfile(simulatorFileName):
                f = open(simulatorFileName, 'r')
                currentSimulators = f.read().split('\n')
                f.close()
                if writeText in currentSimulators:
                    print("该设备已存在")
                    printSimulatorList()
                    return

            if os.path.isfile(simulatorFileName) and os.path.getsize(simulatorFileName) > 0:
                writeText = "\n%s" % writeText
            f = open(simulatorFileName, 'a+')
            f.write(writeText)
            f.close()
            print("添加模拟器成功")
            printSimulatorList()
            break
    if foundSimulatorID == False:
        print("您输入的设备ID不在模拟器列表中,请检查之后重试")

def getSimulatorDescList(fileName):
    f = open(fileName, 'r')
    simulatorList = f.readlines()
    f.close()
    return simulatorList

def bootSimulator():
    simulatorDescList = getSimulatorDescList(simulatorFileName)
    if len(simulatorDescList) == 0:
        print("设备列表为空")
        return False

    simulatorList = []
    for simulatorDesc in simulatorDescList:
        parts = simulatorDesc.split(simulatorDescSeparator)
        simulatorList.append(parts[0])
    simulatorListString = ""
    for simulator in simulatorList:
        simulatorListString = "%s " % simulator

    command = "%s %sboot" % (fbCommand, simulatorListString)
    os.system(command)
    return True

def setAppPath(appPath):
    f = open(appPathFileName, 'w')
    f.write(appPath)
    f.close()

def getAppPath():
    f = open(appPathFileName, 'r')
    appPath = f.read()
    f.close()
    return appPath

def installApp():
    appPath = getAppPath()
    if len(appPath) == 0:
        print("设备列表为空")
        return False

    command = "%s install %s" % (fbCommand, appPath)
    os.system(command)
    return True

def setAppBundleID(bundleID):
    f = open(appBundleIDFileName, 'w')
    f.write(bundleID)
    f.close()

def getAppBundleID():
    f = open(appBundleIDFileName, 'r')
    bundleID = f.read()
    f.close()
    return bundleID

def launchApp():
    bundleID = getAppBundleID()
    if len(bundleID) == 0:
        print("设备列表为空")
        return False
    command = "%s launch %s" % (fbCommand, bundleID)
    os.system(command)
    return True

def autoLaunchApp():
    if bootSimulator():
        if installApp():
            if launchApp():
                return True
    return False

def printSimulatorList():
    fileName = "simulators"
    f = open(fileName, 'r')
    print('==============================')
    print("已添加的设备列表为:")
    print(f.read())
    f.close()
