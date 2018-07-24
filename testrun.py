#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import logging
import os
import getopt
import sys

from utx import *

rootdir = os.path.join(os.path.dirname(os.path.realpath(__file__)),"xkool_site")
print("rootdir=",rootdir)
#os.chdir(rootdir)
if __name__ == '__main__':
    kargs =  {'testName':'qdy@xkool.xyz','rootdir':rootdir,'report':'/var/www/html/report'}
    try:
        options,args = getopt.getopt(sys.argv[1:],"h:",["user=",'rootdir=','report'])
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
