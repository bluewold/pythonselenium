from handle.register_handle import RegisterHandler
class RegisterBusiness(object):
    def __init__(self,driver):
        self.register_handle = RegisterHandler(driver)

    def user_base(self,email,name,password,code):
        self.register_handle.send_user_email(email)
        self.register_handle.send_user_name(name)
        self.register_handle.send_user_password(password)
        self.register_handle.send_user_code(code)
        self.register_handle.click_register_button()

    def register_success(self):
        if self.register_handle.get_register_text() == None:
            return True
        else:
            return False

    def login_email_error(self,email,name,password,code):
        self.user_base(email,name,password,code)
        print("测试")
        if self.register_handle.get_user_text("email_error","请输入有效的电子邮件地址"):
            print("邮箱验证成功")
            return True
        else:
            return False

    def register_function(self,email,username,password,code,assertcode,asserttext):
        self.user_base(email, username, password, code)
        if self.register_handle.get_user_text(assertcode,asserttext):

            return True
        else:
            return False

    def login_name_error(self,email,name,password,code):
        self.user_base(email, name, password, code)
        if self.register_handle.get_user_text("user_name_error","字符长度必须大于等于4，一个中文字算2个字符"):
            print("用户名验证成功")
            return True
        else:
            return False

    def login_password_error(self,email,name,password,code):
        self.user_base(email, name, password, code)
        if self.register_handle.get_user_text("password_error","最少需要输入 5 个字符"):
            print("密码验证成功")
            return True
        else:
            return False





