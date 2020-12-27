import xlrd
from file.resourcemanager.resourcemanger import ResourcePath


class ExcelData:
    """
        @:param nrow:表格行数
                ncol:表格列数
    """

    def __init__(self, path):
        if not isinstance(path, ResourcePath):
            raise AttributeError()
        self.path = path
        self.data = xlrd.open_workbook(self.path.getPath())
        self.sheet = self.data.sheet_by_index(0)
        self.ncol = self.sheet.ncols
        self.nrow = self.sheet.nrows

        """
        获取表格内列有效内容
        @:param index 行的索引
        @:return 具有列有效内容的列表
        """

    def getRowsContent(self, index):
        row = self.sheet.row_values(index)
        del row[0]
        return row

    """ 
        获取表格内列有效内容
        @:param index 的索引
        @:return 具有行有效内容的列表
    """

    def getColsContent(self, index):
        col = self.sheet.col_values(index)
        del col[0]
        return col

    """
        获取表格内一个单元格
    """

    def getCell(self, row, col):
        return self.sheet.cell(row, col)
