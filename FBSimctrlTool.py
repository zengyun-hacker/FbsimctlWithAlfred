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
        errorText = "设备ID不能为空"
        print(errorText)
        return False, errorText
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
                    errorText = "该设备已存在"
                    print(errorText)
                    printSimulatorList()
                    return False, errorText

            if os.path.isfile(simulatorFileName) and os.path.getsize(simulatorFileName) > 0:
                writeText = "\n%s" % writeText
            f = open(simulatorFileName, 'a+')
            f.write(writeText)
            f.close()
            text = "添加模拟器成功"
            print(text)
            printSimulatorList()
            return True, text
            break
    if foundSimulatorID == False:
        errorText = "您输入的设备ID不在模拟器列表中,请检查之后重试"
        print(errorText)
        return False, errorText

def getSimulatorDescList(fileName):
    f = open(fileName, 'r')
    simulatorList = f.readlines()
    f.close()
    return simulatorList

def bootSimulator():
    simulatorDescList = getSimulatorDescList(simulatorFileName)
    if len(simulatorDescList) == 0:
        errorText = "设备列表为空"
        print(errorText)
        return False, errorText

    simulatorList = []
    for simulatorDesc in simulatorDescList:
        parts = simulatorDesc.split(simulatorDescSeparator)
        simulatorList.append(parts[0])
    simulatorListString = ""
    for simulator in simulatorList:
        simulatorListString = "%s " % simulator

    command = "%s %sboot" % (fbCommand, simulatorListString)
    os.system(command)
    return True, "启动模拟器成功"

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
        errorText = "设备列表为空"
        print(errorText)
        return False, errorText

    command = "%s install %s" % (fbCommand, appPath)
    os.system(command)
    return True, "app安装成功"

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
        errorText = "设备列表为空"
        print(errorText)
        return False, errorText
    command = "%s launch %s" % (fbCommand, bundleID)
    os.system(command)
    return True, "app启动成功"

def autoLaunchApp():
    result, error = bootSimulator()
    if result:
        result, error = installApp()
        if result:
            result, error = launchApp()
    return result, error

def printSimulatorList():
    fileName = "simulators"
    f = open(fileName, 'r')
    print('==============================')
    print("已添加的设备列表为:")
    print(f.read())
    f.close()
