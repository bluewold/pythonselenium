from selenium import webdriver
import time
import random
from PIL import Image
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
driver  = webdriver.Chrome()

def driver_init():
    driver.get("http://www.5itest.cn/register?goto=/")
    time.sleep(5)

def get_element(id):
    element = driver.find_element_by_id(id)
    return element

def get_range_user():
    user_email = ''.join(random.sample("123456789abcdefg", 5))
    return user_email

def get_img(file_name):
    driver.save_screenshot(file_name)
    code_element = driver.find_element_by_id("getcode_num")
    left = code_element.location['x']
    top = code_element.location['y']
    right = code_element.size['width'] + left
    height = code_element.size['height'] + top
    im = Image.open(file_name)
    # im.crop((left,top,right,height))
    # print(left,top,right,height)
    im.crop((100, 100, 200, 200))
    im.save(file_name)

def code_online():
    return

def run_main():
    user_email = get_range_user()+ "@163.com"
    username = get_range_user()
    driver_init()
    get_element("register_email").send_keys(user_email)
    get_element("register_nickname").send_keys(username)
    get_element("register_password").send_keys("11111")
