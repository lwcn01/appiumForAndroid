#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "NEW"

import os
import time
import subprocess
from Common.Public.System import System
from Common.Public.String import String

def myLog(func):
    def wrapper(*args, **kw):
        subprocess.Popen(String.CLEAR_LOGCAT)
        time.sleep(String.WAIT_TIME)
        __filename = os.path.join(System().log_path,"Log_" + System().sysTime + ".log")
        __efilename = os.path.join(System().log_path,"ErrorLog_" + System().sysTime + ".log")
        __logfile = open(__filename, 'w')
        __elogfile = open(__efilename,'w')
        __capturelog = subprocess.Popen(String.LOGCAT,stdout=__logfile,stderr=__elogfile)
        func()
        time.sleep(String.WAIT_TIME)
        __capturelog.terminate()
        __logfile.close()
        __elogfile.close()
        try:
            System().removeFile(System().log_path)
        except:
            pass
        #return func(*args, **kw)
    return wrapper
#Command().adb("logcat -d -v time *:E > %s" %(os.path.join(FilePath().creatDir(),"ErrorLog_" + sysTime() + ".log")))