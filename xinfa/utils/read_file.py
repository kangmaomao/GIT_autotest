import json
import re

from base_page import BasePage
import xlrd
import xlwt

class Read_file(BasePage):

    def read_excel_rows(file_path):
        # 读取xlsx文件路径
        file_test = xlrd.open_workbook(file_path)
        #获取总页数
        nsheets = file_test.nsheets
        # 定义一个空列表
        all_data = []
        for i in range(nsheets):
            # 通过索引顺序获取
            table = file_test.sheet_by_index(i)
            # 获取工作簿行数
            nrows = table.nrows
            # 获取工作簿列数
            ncols = table.ncols
            # 定义一个空列表
            sheet_data = []
            # 循环读取每一行的值，从第二行开始，第一行为标题
            for row in range(1, nrows):
                #每行的值
                row_data=[]
                # 循环读取每一列的值，从第二列开始，第一列为序号
                for col in range(1, ncols):
                    # 按列读取单元格数据
                    cell_value = table.cell_value(row,col)
                    # 去除特殊字符
                    #col_value = re.sub(r'[0-9A-Za-z.\xa0▲△]', '', cell_value)
                    #增加读取的每一列的值
                    row_data.append(cell_value)
                #增加读取的每一行的值
                sheet_data.append(row_data)
            #增加读取每一个sheet页的值
            all_data.append(sheet_data)
        #返回整个excel的值
        print(all_data)
        return all_data


    def read_excel_cols(file_path):
        # 读取xlsx文件路径
        file_test = xlrd.open_workbook(file_path)
        #获取总页数
        nsheets = file_test.nsheets
        # 定义一个空列表
        all_data = []
        for i in range(nsheets):
            # 通过索引顺序获取
            table = file_test.sheet_by_index(i)
            # 获取工作簿行数
            nrows = table.nrows
            # 获取工作簿列数
            ncols = table.ncols
            # 定义一个空列表
            sheet_data = []
            # 循环读取每一列的值，从第二列开始，第一列为标题
            for col in range(1, ncols):
                col_data = []
                col_data.append(table.name)
                for row in range(1, nrows):
                    # 按列读取单元格数据
                    cell_value = table.cell_value(col, row)
                    # 去除特殊字符
                    row_value = re.sub(r'[0-9A-Za-z.\xa0▲△]', '', cell_value)
                    # 增加读取的每一行的值
                    col_data.append(row_value)
                # 增加读取的每一列的值
                sheet_data.append(col_data)
            # 增加读取每一个sheet页的值
            all_data.append(sheet_data)
        # 返回整个excel的值
        return all_data

    def read_json(file_path):
        # 指定文件路径
        json_file = file_path
        # 打开json文件
        test_data = []
        with open(json_file, encoding="utf-8") as f:
            json_data = json.load(f)
            for case_data in json_data:
                username = case_data.get("username")
                password = case_data.get("password")
                test_data.append((username, password))
        return test_data

    def read_txt(file_path):
        # 指定文件路径
        txt_file = file_path
        # 打开txt文件
        with open(txt_file,'r' ,encoding='utf-8') as f:
            # read()：读取整个文件;readline()：读取一行数据; readlines()：读取所有行的数据。
            data = f.readlines()
            # 格式化处理
            test_datas = []
            for line in data:
                # 参数之间用冒号“:”隔开
                # [:-1] 可对字符串进行切片，以省略最后一个字符，因为读取的每一行数据结尾都有一个换行符“\n”
                test_data = line[:-1].split(":")
                test_datas.append(test_data)
        return test_data





    """
    def read_file(file_path):

        # 读取xlsx文件路径
        file_test = xlrd.open_workbook(file_path)
        # 获取该文件中的工作簿数
        count = len(file_test.sheets())
        print("工作簿总数为：",count)
        # 根据工作簿名字获取该工作簿的数据
        #table=file_test.sheet_by_name(name)
        # 通过索引顺序获取
        table=file_test.sheet_by_index(0)
        # 通过索引顺序获取
        #table = file_test.sheets()[0]
        # 获取工作簿行数
        nrows = table.nrows
        # # 获取工作簿列数
        # ncols=table.ncols
        # # 获取A1单元格的值
        # cell_A1 = table.cell(0, 0).value
        # # 通过行索引单元格A1的值
        # cell_A1 = table.row(0)[0].value
        # # 通过列索引单元格A1的值
        # cell_A1 = table.col(0)[0].value

        # 从第二行开始，遍历Sheet1中的数据（第一行为表头）
        #print("Sheet1的行数为：", nrows, "列数为：", ncols)
        data = []
        for i in range(1, nrows):
            table.row_values(i)  # 获取某行值
            #table.col_values(i)  # 获取某列值
            # 按行读取数据
            rowvalues = table.row_values(i)
            # 按列读取数据
            #colvalues = table.col_values(i)
            # 第一列为序号，我们取第二列的搜索词
            # key = rowvalues[0]
            # print("搜索词：", key)
            # time.sleep(2)
            data.append(rowvalues)
        return data
        """
    # def read_excel_value(file_path):
    #     # 读取xlsx文件路径
    #     file_test = xlrd.open_workbook(file_path)
    #     #获取总页数
    #     nsheets = file_test.nsheets
    #     for i in range(nsheets):
    #         # 通过索引顺序获取
    #         table = file_test.sheet_by_index(i)
    #         # 获取工作簿列数
    #         ncols = table.ncols
    #         # 定义一个空列表
    #         data = []
    #         # 循环读取每一列的值，从第二列开始，第一列为标题
    #         for col in range(1, ncols):
    #             # 获取某列值
    #             table.col_values(col)
    #             # 按列读取数据
    #             colvalues = table.col_values(col)
    #             a = re.sub(r'[0-9A-Za-z.\xa0▲△]', '', colvalues)
    #             # 将值增加到列表中
    #             data.append(a)
    #         return data