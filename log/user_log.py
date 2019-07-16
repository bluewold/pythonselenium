# coding=UTF-8
import logging
import os
import datetime
class UserLog():
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        #console = logging.StreamHandler()
        #self.logger.addHandler(console)

        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir,"logs")
        log_file =datetime.datetime.now().strftime("%Y-%m-%d")+".log"
        log_name = log_dir+"\\"+log_file


        self.file = logging.FileHandler(log_name,"a",encoding="utf-8")
        formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s %(levelno)s %(levelname)s %(message)s')
        self.file.setLevel(logging.INFO)
        self.file.setFormatter(formatter)
        self.logger.addHandler(self.file)


        #console.close()
        #file.close()
        #self.logger.removeHandler(console)

    def get_log(self):
        return self.logger

    def close(self):
        self.logger.removeHandler(self.file)
        self.file.close()
