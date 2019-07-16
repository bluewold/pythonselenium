from util.read_ini import ReadIni

class findElement(object):
    def __init__(self,driver):
        self.driver = driver
    def get_element(self,key):
        try:
            read_ini = ReadIni()
            data = read_ini.get_value(key)
            by = data.split(":")[0]
            value = data.split(":")[1]

            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == "name":
                return self.driver.find_element_by_name(value)
            elif by == "className":
                return self.driver.find_element_by_class_name(value)
            elif by == "xpath":
                return self.driver.find_element_by_xpath(value)
        except:
            return None