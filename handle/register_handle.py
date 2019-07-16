# coding=UTF-8
from page.register_page import RegisterPage
class RegisterHandler(object):
    def __init__(self,driver):
        self.register_page = RegisterPage(driver)
    #输入邮箱
    def send_user_email(self,email):
        self.register_page.get_email_element().send_keys(email)

    def send_user_name(self,username):
        self.register_page.get_username_element().send_keys(username)

    def send_user_password(self,password):
        self.register_page.get_password_element().send_keys(password)

    def send_user_code(self,code):
        self.register_page.get_code_element().send_keys(code)

    def get_user_text(self,info,user_info):
        try:
            print(info)
            if info == "email_error":
                text = self.register_page.get_email_error_element().text
                print("ggg"+text)
            elif info == "name_error":
                text = self.register_page.get_name_error_element().text
            elif info == "password":
                text = self.register_page.get_password_element().text
            else:
                text = self.register_page.get_code_element().text
        except:
            text = None
        return text

    def click_register_button(self):
        self.register_page.get_register_button().click()

    def get_register_text(self):
        return self.register_page.get_register_button().text