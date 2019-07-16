from selenium import webdriver
import time
import random
from PIL import Image
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

driver.get("http://www.5itest.cn/register?goto=/")
end_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(random.random()*10)
    new_height = driver.execute_script('return document.body.scrollHeight')
    print(end_height, new_height)
    if new_height == end_height:
        break
    end_height = new_height

time.sleep(1)
print(EC.title_contains("注册"))

#element = driver.find_elements_by_class_name("controls")[1]
locator = (By.CLASS_NAME,"controls")
WebDriverWait(driver,1).until(EC.visibility_of_element_located(locator))
for i in range(5):
    user_email = ''.join(random.sample("123456789abcdefg",5))+"@163.com"


driver.save_screenshot("1.png")
code_element = driver.find_element_by_id("getcode_num")
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width']+left
height = code_element.size['height']+top
im = Image.open("1.png")
#im.crop((left,top,right,height))
#print(left,top,right,height)
im.crop((100,100,200,200))
im.save("2.png")

email = driver.find_element_by_id("register_email")
print(email.get_attribute("placeholder"))
driver.find_element_by_id("register_email").send_keys("111")
print(email.get_attribute("value"))
driver.find_elements_by_class_name("controls")[1].find_element_by_class_name("form-control").send_keys("2222")
driver.find_element_by_name("password").send_keys("2222")
driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys("ased")
#driver.close()