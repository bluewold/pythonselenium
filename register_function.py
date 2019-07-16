import sys

from selenium import webdriver

sys.path.append('C:\\Users\\edwardlee\\PycharmProjects\\自动化测试')
import time
import random
from base.find_element import findElement
class RegisterFunction(object):
    def __init__(self,url):
        self.driver = self.get_driver(url)

    def get_driver(self,url):
        driver = webdriver.Chrome()
        driver.get(url)
        return driver

    def send_user_info(self,key,data):
        self.get_user_element(key).send_keys(data)

    def get_user_element(self,key):
        find_element = findElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    def get_range_user(self):
        user_email = ''.join(random.sample("123456789abcdefg", 5))
        return user_email

    def get_img(self,file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.driver.find_element_by_id("getcode_num")
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_name)
        # im.crop((left,top,right,height))
        # print(left,top,right,height)
        im.crop((100, 100, 200, 200))
        im.save(file_name)

    def code_online(self):
        return

    def main(self):
        user_name_infp = self.get_range_user()
        user_email = user_name_infp+"@163.com"
        filename= r"C:\Users\edwardlee\PycharmProjects\自动化测试\config\localelement.ini"
        self.send_user_info('user_email',user_email)
        self.send_user_info('user_name',user_name_infp)
        self.send_user_info('password',"111111")
        self.get_user_element("register_button").click()
        code_error = self.get_user_element("code_text_error")
        if code_error == None:
            print("注册成功")
        else:
            self.driver.save_screenshot("error.png")
        time.sleep(5)

if __name__ == '__main__':
    register = RegisterFunction("http://www.5itest.cn/register?goto=/")
    register.main()