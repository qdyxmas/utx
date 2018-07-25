#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import logging
import os
import getopt
import sys
import datetime
import requests
from utx import *
import json
def send_dingding(msg):
    url='https://oapi.dingtalk.com/robot/send?access_token=9abd2d571e04062a758732ec2b37b2c01e69b4249e24a37a68a76916028c4759'
    headers = {'content-type':'application/json'}
    datas = {"msgtype": "markdown", "markdown": {
            "title": "单元测试结果",
            "text": "@all单元测试结果:%s" %("http://192.168.20.3/report/"+msg)
            }}
    datas = json.dumps(datas)
    try:
        req = requests.post(url,headers=headers,data=datas)
    except:
        pass
    return True
rootdir = os.path.join(os.path.dirname(os.path.realpath(__file__)),"test")
# print("rootdir=",rootdir)
#os.chdir(rootdir)
if __name__ == '__main__':
    start_time=datetime.datetime.now()
    dirname= '{}'.format(start_time.strftime("%Y-%m-%d-%H-%M-%S"))
    kargs =  {'testName':'qdy@xkool.xyz','rootdir':rootdir,'report':'/var/www/html/report','dirname':dirname}
    try:
        options,args = getopt.getopt(sys.argv[1:],"h:",["user=",'rootdir=','report='])
    except getopt.GetoptError:
        print('error')
        sys.exit()
    for name,value in options:
        if name in ("--user"):
            kargs['testName'] = value
        elif name in ("--rootdir"):
            kargs['rootdir'] = value
        elif name in ("--report"):
            kargs['report'] = value
    log.set_level(logging.DEBUG)
    print(kargs)
    runner = TestRunner(**kargs)
    runner.add_case_dir(kargs['rootdir'])
    runner.run_test()
    send_dingding(dirname)
