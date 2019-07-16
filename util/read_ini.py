# coding=UTF-8
import configparser

class ReadIni(object):
    def __init__(self,filename=None,node=None):
        if filename == None:
            filename = r"C:\Users\edwardlee\PycharmProjects\自动化测试\config\localelement.ini"
        if node == None:
            self.node = "RegisterElement"
        else:
            self.node = node
        self.cf = self.load_ini(filename)

    def load_ini(self,filename):
        cf = configparser.ConfigParser()
        cf.read(r"C:\Users\edwardlee\PycharmProjects\自动化测试\config\localelement.ini")
        return cf

    def get_value(self,key):
        return self.cf.get(self.node,key)


if __name__ == "__main__":
    read_init  = ReadIni()
    print(read_init.get_value("user_email"))