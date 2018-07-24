#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import unittest
import datetime
from utx import log
from utx.BSTestRunner import BSTestRunner
import coverage

class TestRunner():

    def __init__(self,**kargs):
        self.case_dirs = []
        if not kargs:
            self.reserved['testName'] = 'qudeyong'
            self.reserved['report'] = '/var/www/html/report'
        else:
            self.reserved = kargs
        self.start_time=datetime.datetime.now()
    def add_case_dir(self, dir_path):
        """添加测试用例文件夹，多次调用可以添加多个文件夹，会按照文件夹的添加顺序执行用例

            runner = TestRunner()
            runner.add_case_dir(r"testcase\chat")
            runner.add_case_dir(r"testcase\battle")
            runner.run_test(report_title='接口自动化测试报告')

        :param dir_path:
        :return:
        """
        if not os.path.exists(dir_path):
            raise Exception("测试用例文件夹不存在：{}".format(dir_path))
        if dir_path in self.case_dirs:
            log.warn("测试用例文件夹已经存在了：{}".format(dir_path))
        else:
            self.case_dirs.append(dir_path)

    def run_test(self, report_title='接口自动化测试报告'):
        cov = coverage.Coverage(source=self.case_dirs)
        cov.start()
        if not self.case_dirs:
            raise Exception("请先调用add_case_dir方法，添加测试用例文件夹")

        if not os.path.exists(self.reserved['report']):
            os.mkdir(self.reserved['report'])
        dirname = '{}'.format(self.start_time.strftime("%Y-%m-%d-%H-%M-%S"))
        report_dir = os.path.abspath(self.reserved['report']+'/'+dirname)
        os.mkdir(report_dir)
        os.mkdir(report_dir+'/coverage')
        suite = unittest.TestSuite()
        for case_path in self.case_dirs:
            # print("case_path=",case_path)
            suite.addTests(unittest.TestLoader().discover(case_path,pattern='*test.py'))
        BSTestRunner(report_dir=report_dir, report_title=self.reserved['testName'],**self.reserved).run(suite)
        # BSTestRunner(report_dir=report_dir, report_title=report_title,**self.reserved).run(suite)

        print("测试完成，请查看报告")
        os.chdir(report_dir)
        cov.stop()
        cov.save()
        cov.html_report(directory=report_dir+'/coverage')
        #os.system("tar -zcvf test_result.tar.gz ./*")
        #fzip = report_dir+'/test_report.zip'
        #os.system('sz test_result.tar.gz')
