#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "NEW"

from Common.DeviceInfo import DeviceInfo
from Common.Command import Command
from Common.Public.String import String
from Common.Public.System import System

class Dash:

    def uiDump(self):
        """
        获取当前Activity的控件树
        """
        dump_name = "%s.xml" % System().sysTime
        if int(DeviceInfo().sdk) >= 19:
            Command().shell(String.UIAUTOMATOR_DUMP_NEWMETHOD + String.TMP_PATH + dump_name).wait()
        else:
            Command().shell(String.UIAUTOMATOR_DUMP_OLDMETHOD + String.TMP_PATH + dump_name).wait()
        Command().adb("pull {0} {1}".format(String.TMP_PATH + dump_name,DeviceInfo().tempFile),"-s").wait()
        try:
            Command().shell("rm "+ String.TMP_PATH + dump_name).wait()
        except Exception as e:
            print(e)
        return DeviceInfo().tempFile + "\\" + dump_name

    def handleXml(self):
        xml_path = self.uiDump()

if __name__ == "__main__":
    Dash().handleXml()