# coding=UTF-8
from selenium import webdriver
from base.find_element import findElement
import time
class ActionMethod(object):
    def __init__(self):
        pass

    def open_browser(self,browser):
        #if browser == 'chrome':
          #  driver = webdriver.Chrome()
        self.driver = webdriver.Chrome()

    def get_url(self,url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_element(self,key):
        find_element = findElement(self.driver)
        element = find_element.get_element(key)
        return element

    def element_send_keys(self,key,value):
        element = self.get_element(key)
        element.send_keys(value)

    def click_element(self,key):
        self.get_element(key).click()

    def sleep_time(self):
        time.sleep(3)

    def close_browser(self):
        self.driver.close()