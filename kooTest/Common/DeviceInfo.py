#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "NEW"

import os
import tempfile
import zipfile
from math import floor
from Common.Command import Command
from Common.Logger import mylog
from Common.Public import AXMLParser
from Common.Public.String import String

class DeviceInfo:
    def __init__(self):
        self.sdk = Command().shell(String.SDK).stdout.read().decode(String.UTF8).strip()
        self.tempFile = tempfile.gettempdir()

    def sysInfo(self):
        sdk = self.sdk
        mylog.info("Android SDK版本：%s" % sdk)
        release = Command().shell(String.RELEASE).stdout.read().decode(String.UTF8).strip()
        mylog.info("Android 版本：%s" % release)
        model = Command().shell(String.MODEL).stdout.read().decode(String.UTF8).strip()
        mylog.info("Android 产品型号：%s" % model)
        brand = Command().shell(String.BRAND).stdout.read().decode(String.UTF8).strip()
        mylog.info("Android 产品品牌：%s" % brand)
        return sdk,release,model,brand

    def appInfo(self):
        if os.name == String.WINDOWS:
            __find = String.FIND
        else:
            __find = String.GREP
        # 返回第一行app路径
        __app = Command().shell("dumpsys activity activities | %s baseDir" % __find).stdout.readlines()[0].decode(String.UTF8).strip()
        mylog.info("当前APK文件在Android中路径：%s" %(__app.split("=")[1]))
        # 拉取到本地的app相对路径
        Command().adb("pull {0} {1}".format(__app.split("=")[1],self.tempFile),"-s")
        __appPath = self.tempFile + "\\" + __app.split("/")[-1]
        mylog.info("APK 文件相对路径：%s" %__appPath)
        try:
            __zipFile = zipfile.ZipFile(__appPath)
            __data = __zipFile.read(__zipFile.namelist()[0])
        except Exception as e:
            mylog.warn("zipfile Error：%s" %e)
            return False
        # 从压缩包里解压缩出AndroidManifest.xml
        else:
            # 将解压出的AndroidManifest.xml文件保存到本地，二进制的xml文件
            mylog.info("解压后AndroidManifest.xml文件路径：%s" %(self.tempFile + "\\AndroidManifest.xml"))
            with open(self.tempFile + "\\AndroidManifest.xml",'wb') as xml:
                xml.write(__data)
            __apkInfo = AXMLParser.APK(__data)
            packageName = __apkInfo.packageName
            mylog.info("当前APK包名：%s" % packageName)
            name = __apkInfo.versionName
            mylog.info("当前APK版本：%s" % name)
            # 得到app的文件大小
            size = floor(os.path.getsize(__appPath)/(1024*1000))
            mylog.info("APK 文件大小：%s M" %str(size))
            # apk大小，版本名称
            return packageName,size,name

#DeviceInfo().sysInfo()