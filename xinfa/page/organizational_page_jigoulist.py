from selenium.webdriver.support.select import Select

from xinfa.page.base_page import BasePage


class Organizational_Page_JigouList(BasePage):
    def new_oz(self):
        # 进入机构列表
        self.element_click(['xpath', '//*[@id="root"]/div/section/aside/div/ul/li[5]'])
        self.sleep(2)

    """机构列表模块功能操作
    注意：第一次点击机构列表时，各个模块的定位都是1，也就是“rc-tabs-1-tab-1”，第二个点击机构列表时“rc-tabs-2-tab-1”，其他列表同理
    """
    """新增机构"""

    def input_oz(self, data, json1,json2):
        # 新增机构，输入新增机构的值
        # self.click(['id','rc-tabs-1-tab-1'])
        self.element_click(['xpath', '//*[@class="ant-col"]/button'])
        self.sleep(2)
        basic_name = data[0]
        basic_orgCode = data[1]
        basic_address = data[2]
        basic_remarkInfo = data[5]
        self.type(['id', 'basic_name'], basic_name)
        self.type(['id', 'basic_orgCode'], basic_orgCode)
        self.type(['id', 'basic_address'], basic_address)
        self.element_click(['id', 'basic_parentOrgCode'])
        self.sleep(1)
        # 可以根据需求添加哪个机构，修改text机构名称
        self.element_click(['xpath', '//*[@class="ant-select-tree-title" and text()="%s"]' % (repr(json1))])
        # self.click(['xpath','//*[@class="ant-select-tree-list-holder-inner"]/div[3]'])
        self.sleep(1)
        self.element_click(['id', 'basic_organTypeId'])
        self.sleep(1)
        # 可以根据需求添加哪个机构类型，修改text机构名称
        self.element_click(['xpath', '//*[@class="ant-select-tree-title" and text()="%s"]' % (repr(json2))])
        self.sleep(1)
        self.type(['id', 'basic_remarkInfo'], basic_remarkInfo)
        self.sleep(2)
        self.element_click(['xpath', '//*[@type="submit"]'])

    """编辑机构"""

    def edit_oz(self, data,json1,json2):
        # tr后面的数字代表要修改哪个机构的数据
        self.element_click(['xpath', '//*[@class="ant-table-tbody"]/tr[2]/td[5]/span/a[1]'])
        self.sleep(2)
        basic_name = data[0]
        basic_orgCode = data[1]
        basic_address = data[2]
        basic_remarkInfo = data[5]
        self.type(['id', 'basic_name'], basic_name)
        self.type(['id', 'basic_orgCode'], basic_orgCode)
        self.type(['id', 'basic_address'], basic_address)
        self.element_click(['id', 'basic_parentOrgCode'])
        self.sleep(1)
        # 可以根据需求添加哪个机构，修改text机构名称
        self.element_click(['xpath', '//*[@class="ant-select-tree-title" and text()="%s"]' % (repr(json1))])
        # self.click(['xpath','//*[@class="ant-select-tree-list-holder-inner"]/div[3]'])
        self.sleep(1)
        self.element_click(['id', 'basic_organTypeId'])
        self.sleep(1)
        # 可以根据需求添加哪个机构类型，修改text机构名称
        self.element_click(['xpath', '//*[@class="ant-select-tree-title" and text()="%s"]' % (repr(json2))])
        self.sleep(1)
        self.type(['id', 'basic_remarkInfo'], basic_remarkInfo)
        self.sleep(2)
        self.element_click(['xpath', '//*[@type="submit"]'])

    """删除机构"""

    def delete_oz(self):
        # tr后面的数字代表要删除哪个机构的数据，button后面的数字，1是取消，2是确定
        self.element_click(['xpath', '//*[@class="ant-table-tbody"]/tr[2]/td[5]/span/a[2]'])
        self.element_click(['xpath', '//*[@class="ant-popover-buttons"]/button[2]'])

    """缺少批量导入的功能"""

    """用户列表模块功能操作"""

    def choose_oz(self,data):
        """选择机构"""
        self.element_click(['xpath', '//*[@class="dev___ndHbd"]/div/div/span[1]'])
        self.move_to_element_click(['xpath', '//*[@class="ant-select-selection-item" and text()="%s"]' % (repr(data))])
    def input_user(self, data,json1,json2):
        # 新增用户，输入新增用户的数据,
        self.element_click(['id', 'rc-tabs-1-tab-2'])
        self.element_click(['xpath', '//*[@class="ant-col"]/button'])
        self.sleep(2)
        basic_account = data[0]
        basic_username = data[1]
        basic_tel = data[2]
        basic_password = data[3]
        self.type(['id', 'basic_account'], basic_account)
        self.type(['id', 'basic_username'], basic_username)
        self.type(['id', 'basic_tel'], basic_tel)
        self.type(['id', 'basic_password'], basic_password)
        self.sleep(2)
        self.element_click(['id', 'basic_roleId'])
        # 商业银行测试，网点管理员，总行管理员，自定义角色，可以在text处修改角色信息
        self.element_click(['xpath', '//*[@class="ant-select-item-option-content" and text()="%s"]' % (repr(json1))])
        self.sleep(2)
        self.element_click(['id', 'basic_companyDeptId'])
        # 可以根据需求添加哪个机构的用户，修改text机构名称
        self.element_click(['xpath', '//*[@class="ant-select-tree-title" and text()="%s"]' % (repr(json2))])
        self.sleep(2)
        self.element_click(['xpath', '//*[@type="submit"]'])

    """重置密码功能"""

    def reset_password(self, data):
        self.element_click(['id', 'rc-tabs-1-tab-2'])
        # tr后面的数字代表要修改哪个用户的密码
        self.element_click(['xpath', '//*[@class="ant-table-tbody"]/tr[2]/td[6]/span/a[1]'])
        self.type(['xpath', '//*[@class="ant-modal-body"]/span/input'], data)
        # button后面的数字，1是取消，2是确定
        self.element_click(['xpath', '//*[@class="ant-modal-footer"]/button[2]'])

    """编辑用户信息"""

    def edit_user(self, data,json1,json2):
        self.element_click(['id', 'rc-tabs-1-tab-2'])
        # tr后面的数字代表要修改哪个用户信息
        self.element_click(['xpath', '//*[@class="ant-table-tbody"]/tr[2]/td[6]/span/a[2]'])
        basic_username = data[0]
        basic_tel = data[1]
        self.type(['id', 'basic_username'], basic_username)
        self.type(['id', 'basic_tel'], basic_tel)
        # 商业银行测试，网点管理员，总行管理员，自定义角色，可以在text处修改角色信息
        self.element_click(['xpath', '//*[@class="ant-select-item-option-content" and text()="%s"]' % (repr(json1))])
        self.sleep(2)
        # 可以根据需求添加哪个机构的用户，修改text机构名称
        self.element_click(['xpath', '//*[@class="ant-select-tree-title" and text()="%s"]' % (repr(json2))])
        self.sleep(2)
        self.element_click(['xpath', '//*[@type="submit"]'])

    """删除用户功能"""

    def delete_user(self):
        self.element_click(['id', 'rc-tabs-1-tab-2'])
        # tr后面的数字代表要删除哪个用户
        self.element_click(['xpath', '//*[@class="ant-table-tbody"]/tr[2]/td[6]/span/a[3]'])
        self.element_click(['xpath', '//*[@class="ant-modal-body"]/span/input'])
        # button后面的数字，1是取消，2是确定
        self.element_click(['xpath', '//*[@class="ant-popover-buttons"]/button[2]'])

    """角色列表模块功能操作"""

    def input_role(self, data):
        # 新增角色，输入新增角色的数据
        self.element_click(['id', 'rc-tabs-1-tab-3'])
        self.element_click(['xpath', '//*[@class="ant-col"]/button'])
        self.sleep(2)
        basic_account = data[0]
        basic_username = data[1]
        self.type(['xpath', '//*[@class="ant-modal-body"]/div[1]/div[2]/input'], basic_account)
        self.type(['xpath', '//*[@class="ant-modal-body"]/div[2]/div[2]/input'], basic_username)
        # 权限需要改div数字标号
        self.element_click(['xpath', '//*[@class="ant-tree-list-holder-inner"]/div[1]/span[2]/span'])
        self.sleep(2)
        self.element_click(['xpath', '//*[@type="button"]'])

    """编辑角色信息"""

    def edit_role(self, data):
        # 修改角色，输入修改角色的数据
        self.element_click(['id', 'rc-tabs-1-tab-3'])
        # tr后面的数字代表要修改哪个用户信息
        self.element_click(['xpath', '//*[@class="ant-table-tbody"]/tr[1]/td[5]/span/a[1]'])
        self.sleep(2)
        basic_account = data[0]
        basic_username = data[1]
        self.type(['xpath', '//*[@class="ant-modal-body"]/div[1]/div[2]/input'], basic_account)
        self.type(['xpath', '//*[@class="ant-modal-body"]/div[2]/div[2]/input'], basic_username)
        # 权限需要改div数字标号
        self.element_click(['xpath', '//*[@class="ant-tree-list-holder-inner"]/div[1]/span[2]/span'])
        self.sleep(2)
        self.element_click(['xpath', '//*[@type="button"]'])

    """删除角色信息"""

    def delete_role(self):
        self.element_click(['id', 'rc-tabs-1-tab-3'])
        # tr后面的数字代表要删除哪个用户
        self.element_click(['xpath', '//*[@class="ant-table-tbody"]/tr[1]/td[5]/span/a[2]'])
        self.element_click(['xpath', '//*[@class="ant-modal-body"]/span/input'])
        # button后面的数字，1是取消，2是确定
        self.element_click(['xpath', '//*[@class="ant-popover-buttons"]/button[2]'])

    def choose_oz_logs(self,data):
        """选择机构"""
        self.element_click(['xpath', '//*[@class="dev___ndHbd"]/div/div/span[1]'])
        self.move_to_element_click(['xpath', '//*[@class="ant-select-selection-item" and text()="%s"]' % (repr(data))])
    """根据操作人搜索日志信息"""
    def search_logs_user(self,data):
        self.element_click(['id', 'rc-tabs-1-tab-4'])
        self.type(['id','operatorName'],data)
        self.element_click(['class', 'ant-btn ant-btn-primary ant-btn-round'])
    """根据操作内容搜索日志信息"""
    def search_logs_file(self,data):
        self.element_click(['id', 'rc-tabs-1-tab-4'])
        self.type(['id','inputValue'],data)
        self.element_click(['class', 'ant-btn ant-btn-primary ant-btn-round'])
    def prev_page(self):
        # 点击上一页
        self.element_click(['xpath', '//*[@class="ant-pagination-prev"]'])
        self.sleep(2)
    def random_page(self,data):
        # 点击随机页，数字代表哪一页
        self.element_click(['xpath', '//*[@class="ant-pagination-item ant-pagination-item-%d"]' % data])
        self.sleep(2)
    def next_page(self):
        # 点击下一页
        self.element_click(['xpath', '//*[@class="ant-pagination-next"]'])
        self.sleep(2)
    def prev_five(self):
        # 点击向前五页
        self.move_to_element_click(['xpath', '//*[@class="ant-pagination-jump-prev ant-pagination-jump-prev-custom-icon"]'])
        self.sleep(2)
    def next_five(self):
        # 点击向后五页
        self.move_to_element_click(['xpath', '//*[@class="ant-pagination-jump-next ant-pagination-jump-next-custom-icon"]'])
        self.sleep(2)


