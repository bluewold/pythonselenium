# coding=UTF-8
from business.register_business import RegisterBusiness
from selenium import webdriver
import HTMLTestRunner
import os
import unittest
from base.excel_util import ExcelUtil
import sys
import time
import ddt
ex = ExcelUtil()
data = ex.get_data()

@ddt.ddt
class firstDdtCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register?goto=/")
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        time.sleep(2)

        for method_name,error in self._outcome.errors:
            if error:
                casename = self._testMethodName
                file_path = os.path.join(os.getcwd() + "\\report\\"+casename+".png")
                self.driver.save_screenshot(file_path)

        self.driver.close()
    '''
    @ddt.data(
        ['111','22','333','11','email_error','请输入有效的电子邮件地址'],
        ['22222@163.com', '22', '333', '11', 'email_error', '请输入有效的电子邮件地址'],
        ['111', '22', '333', '11', 'email_error', '请输入有效的电子邮件地址']

    )'''
    @ddt.data(*data)
    def test_register_case(self,data):
        email,username,password,code,assertcode,asserttext = tuple(data)
        print(data)
        email = str(email)
        username = str(username)
        password = str(password)
        code = str(code)
        assertcode = str(assertcode)
        asserttext = str(asserttext)
        email_error = self.login.register_function(email,username,password,code,assertcode,asserttext)
        return self.assertTrue(email_error,"case执行成功")

if __name__  == "__main__":
    file_path = os.path.join(os.getcwd() + "\\report\\" + "first_case.html")
    f = open(file_path, 'wb+')
    suite = unittest.TestLoader().loadTestsFromTestCase(firstDdtCase)
    #suite = unittest.TestSuite()
    #suite.addTest(firstDdtCase('test_register_case'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='This is first report', description="这是第一个数据驱动报告")
    runner.run(suite)