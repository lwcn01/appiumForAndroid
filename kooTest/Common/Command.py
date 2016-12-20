#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "NEW"
import sys
import os,re
import subprocess
from Common.Public.String import String
from Common.Logger import mylog
from Common.Public.System import System

class Initialize:
    def adbEnv(self):
        if os.name == String.WINDOWS:
            env = os.getenv(String.PATH)
            adb_env = re.findall(String.PLATFORM_TOOLS, env)
            if len(adb_env) == 0:
                raise EnvironmentError('env_configure error')
            elif len(adb_env) != 0:
                for i in re.split(";", env):
                    adb_env = re.findall(r"[A-Za-z]\:.*\\platform-tools", i)
                    if len(adb_env) != 0:
                        adb_env = adb_env[0]
                        break
                if String.ADBD not in os.listdir(adb_env):
                    raise EnvironmentError('adb not found in platform-tools')
                else:
                    return True
        else:
            return False

    def deviceList(self):

        __deviceList = subprocess.Popen(String.DEVICESLIST,
                                        shell=True,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE).stdout.read().decode(String.UTF8).strip()
        devicelist = []
        if len(__deviceList.split("\n")) == 1:
            mylog.warn("ADB连接...失败")
            os.system(String.PAUSE)
            sys.exit(-1)
        elif len(__deviceList.split("\n")) == 2:
            if __deviceList.split("\n")[1].split()[1] == String.DEVICE:
                devicelist.append(__deviceList.split("\n")[1].split()[0])
                return devicelist
            elif __deviceList.split("\n")[1].split()[1] != String.DEVICE:
                mylog.warn(__deviceList.split("\n")[1].split()[1])
                mylog.warn("ADB连接...失败")
                os.system(String.PAUSE)
                sys.exit(-1)
        else:
            for i in range(1, len(__deviceList.split("\n"))):
                devicelist.append(__deviceList.split("\n")[i].split()[0])
            return devicelist

    def checkEnv(self):
        __version = subprocess.check_output(String.PYTHON_VERSION).decode(String.UTF8).strip()
        mylog.info("当前Python 版本：%s" % __version)
        __versionNum = __version.split(String.PYTHON)[1].strip()
        if __versionNum.split(".")[0] == "2":
            mylog.info("当前Python 版本：%s\n请安装Python 3.x版本..." % __version)
            os.system(String.PAUSE)
            sys.exit(-1)
        else:
            devicelist = self.deviceList()
            if len(devicelist) == 1:
                mylog.info("ADB当前连接设备：%s" % (devicelist))
            else:
                mylog.info("ADB当前连接共 %s 个设备：%s" % (len(devicelist),devicelist))

class Command:
    def __init__(self):
        devicelist = Initialize().deviceList()
        if len(devicelist) == 1:
            self.devicelist = devicelist[0]
        else:
            for device in devicelist:
                self.devicelist = device

    def adb(self, cmd, arg=""):
        """
        :Args:
        - args - adb command
        :Usage:
            Command.adb('cmd','-s')
        """
        if arg == "-s":
            arg = "-s " + self.devicelist
        cmds = "%s %s %s" % (String.ADB, arg, str(cmd))
        try:
            subprocess.Popen(cmds, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except Exception as e:
            mylog.error("%s : %s" %(cmds,e))
        else:
            return subprocess.Popen(cmds, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def shell(self, cmd):
        cmds = "%s -s %s shell %s" % (String.ADB, self.devicelist, str(cmd))
        try:
            subprocess.Popen(cmds, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except Exception as e:
            mylog.error("%s : %s" %(cmds,e))
        else:
            return subprocess.Popen(cmds, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            # Command().adb("shell pm list package -3","-s").stdout.read().decode('utf-8').strip()

    def whatsApp(self,system = None):
        """
        Usage:whatsApp()
             or whatsApp(String.SYSTEM)
        """
        if system == String.SYSTEM:
            cmd = String.SYSTEM_CMD
        else:
            cmd = String.THIRD_CMD
        AppList = []
        for package in self.shell(cmd).stdout.readlines():
            AppList.append(re.split(r"[:=]",str(package))[-1].splitlines()[0])
        for i in range(len(AppList)):
            AppList[i] = AppList[i].split("\\")[0]
        # 以列表返回 系统已安装应用包名
        return AppList

    def isAppInstall(self,bundle_id):
        """
        :arg bundle_id: packageName
        """
        if bundle_id in self.whatsApp():
            return True
        else:
            return False

    def installApp(self,app_path=None,app_dir=None):
        """
        APK在PC端
        :arg app_path: app的完整路径
             app_dir:app所在的目录
        Usage:
        InstallApp(System().data_path)
        or InstallApp("G:\workspace\kooTest\Data\test.apk")
        """
        if app_dir:
            for app in System().listFile(app_dir):
                if app.endswith(".apk"):
                    app_path = os.path.join(app_dir,app)
                    break
        elif os.path.isfile(app_path):
            app_path = app_path.strip()
        if app_path:
            try:
                Command().adb('install -r {}'.format(app_path)).wait()
            except Exception as e:
                mylog.warn("%s 安装失败：%s" %(os.path.basename(app_path),e))
            else:
                mylog.info("%s 安装成功.." %os.path.basename(app_path))
        else:
            pass