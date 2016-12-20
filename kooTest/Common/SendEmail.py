#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "NEW"
import os
import smtplib
import configparser
from Common.Logger import mylog
from Common.Public.System import System
from Common.Public.String import String
from email.header import Header
from email.mime.text import MIMEText
#from email.mime.image import MIMEImage
from email.utils import parseaddr, formataddr

def configure():
    #通过自带的configparser模块，读取发送邮件的配置文件，作为字典返回
    conf_file = configparser.RawConfigParser()
    try:
        conf_file.read(os.path.join(System().data_path , 'Config.ini'))
    except:
        mylog.error("%s : Config.ini not found" % System().data_path)
    else:
        conf_info  = []
        for i in conf_file.sections():   #返回所有的section
            #conf_file.options(i)        #以列表返回一个section中的所有key
            mail = {}
            for j in conf_file.items(i):
                mail[j[0]] = j[1]
            conf_info.append(mail)

        if len(conf_file.sections()) == 1:
            return conf_info[0]
        else:
            return conf_info             #以列表返回各section信息

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, String.UTF8).encode(), addr))

def sendEmail(html_path):
    conf_info =  configure()
    html = open(html_path,"rb")
    #SMTP发送邮件
    msg = MIMEText(html.read(),String.HTML,String.UTF8)
    html.close()
    msg[String.FROM] = _format_addr("new <%s>" % conf_info[String.SENDER])
    msg[String.TO] = _format_addr("<%s>" % conf_info[String.RECEIVER])
    msg[String.SUBJECT] = Header(String.TITLE,String.UTF8).encode()
    server = smtplib.SMTP(conf_info[String.SMTPSERVER],25)
    try:
        server.login(conf_info[String.USERNAME], conf_info[String.PASSWORD])
        server.sendmail(conf_info[String.SENDER], [conf_info[String.RECEIVER]], msg.as_string())
    except Exception as e:
        mylog.error("Send_mail Error : %s " % e)
    else:
        mylog.info("Send_mail Success...")
    finally:
        server.quit()