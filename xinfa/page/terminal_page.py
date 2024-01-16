import os

from base_page import BasePage


class Terminal_Page(BasePage):
    def new_Ter(self):
        # 进入设备管理，li后面的数字是节目管理所在位置
        self.element_click(['xpath', '//*[@id="root"]/div/section/aside/div/ul/li[8]'])
        self.sleep(2)

    """设备管理中的素材列表模块功能操作
    注意：新打开页面第一次点击设备管理时，各个模块的中间定位tabs后面的数字都是1，也就是“rc-tabs-1-tab-1”，第二个点击设备管理时“rc-tabs-2-tab-1”，其他列表同理
    """
    """选择机构"""

    def choose_oz(self,data):
        self.element_click(['xpath', '//*[@class="dev___1Oj-b"]/div/div/span[1]'])
        self.move_to_element_click(['xpath', '//*[@class="ant-select-selection-item" and text()="%s"]' % (repr(data))])

    """新增终端分组"""

    def ter_input_group(self, data):
        self.move_to_element_click(['xpath', '//*[@class="ant-row ceBianDaoHang"]/div/img[2]'])
        self.sleep(2)
        file_name = data[0]
        self.type(['xpath', '//*[@class="ant-input ant-input-lg inputStyle"]'], file_name)
        self.element_click(['xpath', '//*[@class="ant-btn ant-btn-primary ant-btn-lg"]'])

    """编辑终端分组"""

    def ter_edit_group(self, data):
        #修改li后面的数字，可以编辑哪个分组
        self.move_to_element_click(['xpath', '//*[@class="ant-spin-container"]/ul/li[2]/div'])
        self.sleep(2)
        file_name = data[0]
        self.element_click(['xpath', '//*[@class="ant-input ant-input-lg inputStyle"]'])
        self.delete(['xpath', '//*[@class="ant-input ant-input-lg inputStyle"]'])
        self.type(['xpath', '//*[@class="ant-input ant-input-lg inputStyle"]'], file_name)
        #确定修改分组名
        self.element_click(['xpath', '//*[@class="ant-btn ant-btn-primary ant-btn-lg"]'])

    """通过审核状态选择节目"""
    def ter_edit_delete(self):
        #删除分组名
        #修改li后面的数字，可以编辑哪个分组
        self.move_to_element_click(['xpath', '//*[@class="ant-spin-container"]/ul/li[2]/div'])
        self.element_click(['xpath', '//*[@class="ant-btn ant-btn-primary ant-btn-lg delButton"]'])


    def ter_history_prev(self):
        # 选择节目，点击上一页
        self.element_click(['xpath', '//*[@class="ant-pagination-prev"]'])
        self.sleep(2)
    def ter_history_random(self,data):
        # 选择节目,点击随机页，数字代表哪一页
        self.element_click(['xpath', '//*[@class="ant-pagination-item ant-pagination-item-%d"]' % data])
        self.sleep(2)
    def ter_history_next(self):
        # 选择节目,点击下一页
        self.element_click(['xpath', '//*[@class="ant-pagination-next"]'])
        self.sleep(2)
    def ter_history_prev_five(self):
        # 选择节目,点击向前五页
        self.move_to_element_click(['xpath', '//*[@class="ant-pagination-jump-prev ant-pagination-jump-prev-custom-icon"]'])
        self.sleep(2)
    def ter_history_next_five(self):
        # 选择节目,点击向后五页
        self.move_to_element_click(['xpath', '//*[@class="ant-pagination-jump-next ant-pagination-jump-next-custom-icon"]'])
        self.sleep(2)