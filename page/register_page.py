# coding=UTF-8
from base.find_element import findElement
class RegisterPage(object):
    def __init__(self,driver):
        self.find_element = findElement(driver)
    def get_email_element(self):
        return self.find_element.get_element("user_email")

    def get_username_element(self):
        return self.find_element.get_element("user_name")

    def get_email_element(self):
        return self.find_element.get_element("user_email")

    def get_password_element(self):
        return self.find_element.get_element("password")

    def get_code_element(self):
        return self.find_element.get_element("code_text")

    def get_register_button(self):
        return self.find_element.get_element("register_button")

    def get_email_error_element(self):
        return self.find_element.get_element("user_email_error")

    def get_name_error_element(self):
        return self.find_element.get_element("user_name_error")

    def get_password_error_element(self):
        return self.find_element.get_element("password_error")

    def get_code_error_element(self):
        return self.find_element.get_element("code_text_error")
