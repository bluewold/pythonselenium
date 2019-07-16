# coding=UTF-8
from business.register_business import RegisterBusiness
from selenium import webdriver
import HTMLTestRunner
import os
from log.user_log import UserLog
import unittest
import sys
import time

sys.path.append(r"C:\Users\edwardlee\PycharmProjects\自动化测试\business")
sys.path.append(r'C:\Users\edwardlee\PycharmProjects\自动化测试\log')
sys.path.append(r"C:\Users\edwardlee\DeepML\Lib\site-packages\selenium")
sys.path.append(r"C:\Program Files (x86)\Google\Chrome\Application")
class firstCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.log = UserLog()
        self.logger = self.log.get_log()
        print("所有case执行之前的前置")

    @classmethod
    def tearDownClass(self):
        print("所有case执行之后的后置置")
        self.log.close()

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register?goto=/")

        self.logger.info("this is chrome")

        self.login = RegisterBusiness(self.driver)

    def tearDown(self):

        time.sleep(2)

        for method_name,error in self._outcome.errors:
            if error:
                casename = self._testMethodName
                file_path = os.path.join(os.getcwd() + "\\report\\"+casename+".png")
                self.driver.save_screenshot(file_path)

        self.driver.close()

    def test_login_email_error(self):
        email_error = self.login.login_email_error("22","user11","1111","2222")
        if email_error == True:
            print("邮箱验证成功，此条case成功")
        else:
            print("注册成功，此条case失败")
        self.assertTrue(email_error,"case执行成功")

    def test_login_username_error(self):
        username_error = self.login.login_name_error("22","user11","1111","2222")
        '''if username_error == True:
            print("用户名验证成功，此条case成功")
        else:
            print("注册成功，此条case失败")'''
        self.assertTrue(username_error,"case执行成功")

    def test_login_code_error(self):
        pass

    def test_login_success(self):
        success = self.login.user_base("1111","222","22","333")
        '''if self.login.register_success() == True:
            print("注册成功")'''
        self.assertTrue(self.login.register_success())

if __name__ == "__main__":
    #file_path = os.path.join(os.getcwd()+"\\report\\"+"first_case.html")
    #f = open(file_path,'wb+')

    unittest.main()
    suite = unittest.TestSuite()
    #suite.addTest(firstCase('test_login_email_error'))
    #unittest.TextTestRunner().run(suite)
    #runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='This is first report',description="这是第一个报告")
    #runner.run(suite)
    '''first = firstCase()
    first.test_login_code_error()
    first.test_login_email_error()
    first.test_login_username_error()
    #first.test_login_success()'''
