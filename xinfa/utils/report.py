import os
import unittest
import time
from unittestreport import TestRunner




class Runing(object):
    #获取当前文件所在目录
    cur_path = os.path.dirname(os.path.abspath(__file__))
    #用例路径
    test_dir= os.path.join(cur_path, 'D:\\Python\\xinfa\\testcase\\')
    #报告路径
    result_dir = os.path.join(cur_path, 'D:\\Python\\xinfa\\report')

    def creatsuite(self):
        #创建测试套件
        testunit = unittest.TestSuite()
        # 定义测试文件查找的目录
        case_dir = Runing.test_dir
        # 定义 discover 方法的参数（测试用例都以test开头命名）
        suit_tests = unittest.defaultTestLoader.discover(case_dir,pattern='test_login.py',top_level_dir=None)
        # discover 方法筛选出来的用例，循环添加到测试套件中
        for test_suite in suit_tests:
            for test_case in test_suite:
                #将测试用例添加到测试套件中
                testunit.addTests(test_case)
                print(testunit)
        return testunit

    def runtestsuit(self,filename,testername):
        # 报告路径
        report_dir = Runing.result_dir
        now = time.strftime("%Y%m%d-%H_%M_%S")
        suit_tests = Runing.creatsuite(self)
        #执行并自动生成测试报告
        runner = TestRunner(suit_tests,
                            filename=filename + now + 'report.html',
                            report_dir=report_dir,
                            title=filename+'测试报告',
                            tester=testername,
                            desc=filename+'自动化测试')
        runner.run()


