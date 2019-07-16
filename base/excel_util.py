import xlrd
from xlutils.copy import copy
class ExcelUtil:
    def __init__(self,excel_path=None,index=None):
        if excel_path == None:
            self.excel_path = r"C:\Users\edwardlee\PycharmProjects\自动化测试\data\data.xlsx"
        else:
            self.excel_path = excel_path
        if index == None:
            index= 0
        self.data = xlrd.open_workbook(self.excel_path)
        self.table = self.data.sheet_by_index(index)
        self.rows = self.table.nrows

    def get_data(self):
        result = []
        for i in range(self.rows):
            col = self.table.row_values(i)
            result.append(col)
        return result

    def get_lines(self):
        rows = self.table.nrows
        if rows  >= 1:
            return rows
        return None

    def get_col_value(self,i,j):
        data = self.table.cell_value(i,j)
        return data

    def has_next(self):
        pass

    def write_value(self,row,value):
        read_value = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row,9,value)
        write_data.save(r"C:\Users\edwardlee\PycharmProjects\自动化测试\data\keyword_data.xlsx")

#ex = ExcelUtil()
#print(ex.write_value(7,'test'))
