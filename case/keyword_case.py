# coding=UTF-8
from base.excel_util import ExcelUtil
from KeyWordMethod.ActionMethod import ActionMethod
class keywordCase:
    def run_main(self):
        self.action_method = ActionMethod()
        handle_excel = ExcelUtil(r"C:\Users\edwardlee\PycharmProjects\自动化测试\data\keyword_data.xlsx")
        col_lines = handle_excel.get_lines()
        if col_lines:
            for i in range(1,col_lines):
                is_run = handle_excel.get_col_value(i,3)
                if is_run == 'yes':
                    method = handle_excel.get_col_value(i,4)
                    send_value = handle_excel.get_col_value(i, 5)
                    handle_value = handle_excel.get_col_value(i, 6)

                    except_result_method = handle_excel.get_col_value(i, 7)
                    except_result = handle_excel.get_col_value(i, 8)

                    print(method,send_value,handle_value)
                    self.run_method(method,send_value,handle_value)
                    if except_result != "":
                        except_value = self.get_except_result_value(except_result)
                        if except_value[0] == "text":
                            result = self.run_method(except_result_method)

                            if except_value[1] in result:
                                handle_excel.write_value(i,'pass')
                            else:
                                handle_excel.write_value(i,'fail')
                        elif except_value[0] == "element":
                            result = self.run_method(except_result_method,except_value[1])
                            print(result)
                            if result:
                                handle_excel.write_value(i,'pass')
                            else:
                                handle_excel.write_value(i,'fail')

                    else:
                        print("预期结果为空")

    def get_except_result_value(self,data):
        return data.split("=")

    def run_method(self,method,send_value='',handle_value=''):
        method_value = getattr(self.action_method,method)
        if send_value == '' and handle_value != '':
            result = method_value(handle_value)
        elif handle_value != '' and handle_value != '':
            result = method_value(handle_value,send_value)
        elif send_value != '' and handle_value == '':
            result = method_value(send_value)
        else:
            result = method_value()
        return result


    #获取行数
    #循环行数,去执行每一条case
    #是否执行
        #拿到执行方法
        #拿到操作值
        #拿到输入数据
        #if 是否由输入数据
            #执行方法（输入数据，操作元素)
        #if 没有输入数据
            #执行方法（操作元素）

keywordCase().run_main()