from base_page import BasePage

class Dest_Top_Page(BasePage):
    def first_page(self):
    #进入首页
        self.element_click(['xpath', '//*[@id="root"]/div/section/aside/div/ul/li[1]'])
        self.sleep(2)
    def user_info(self,username):
        #查看用户信息，并修改用户名
        self.move_to_element(['class','name___2eduw'])
        self.sleep(2)
        self.element_click(['xpath', '//*[@class="ant-dropdown-menu-item"][1]'])
        self.sleep(2)
        self.delete(['xpath','//*[@type="text"]'])
        self.sleep(1)
        self.type(['xpath','//*[@class="ant-input inputStyle___1IxfE"]'],username)
        self.element_click(['xpath', '//*[@type="button"]'])
    def soft_info(self):
        #查看软件版本信息
        self.move_to_element(['class', 'name___2eduw'])
        self.sleep(2)
        self.element_click(['xpath', '//*[@class="ant-dropdown-menu-item"][2]'])

    def mod_password(self,oldpassword,newpassword1,confirmPassword):
        #修改密码
        self.move_to_element(['class', 'name___2eduw'])
        self.sleep(2)
        self.element_click(['xpath', '//*[@class="ant-dropdown-menu-item"][3]'])
        self.type(['id','basic_oldPassword'],oldpassword)
        self.type(['id','basic_newPassword'],newpassword1)
        self.type(['id','basic_confirmPassword'],confirmPassword)
        self.element_click(['xpath', '//*[@type="submit"]'])

    def logout(self):
        # 退出登录
        self.move_to_element(['class', 'name___2eduw'])
        self.sleep(2)
        self.element_click(['xpath', '//*[@class="ant-dropdown-menu-item"][4]'])

    def look_info(self):
        # 标记未读信息为已读
        self.element_click(['class', 'inform___BAaZi'])
        self.sleep(2)
        self.element_click(['class', 'testBoxContent___37GN4'])
    def look_all_info(self):
        #查看全部消息
        self.element_click(['class', 'inform___BAaZi'])
        self.sleep(2)
        self.element_click(['link', '查看全部消息'])
        self.sleep(5)

    def delete_info(self):
        # 单个删除消息
        self.element_click(['xpath', '//*[@class="anticon anticon-rest"][1]'])
        self.sleep(2)
        self.element_click(['xpath', '//*[@class="ant-popover-buttons"]/button[2]'])
    def dissmiss_delete_info(self):
        # 取消删除消息
        self.element_click(['xpath', '//*[@class="anticon anticon-rest"][1]'])
        self.sleep(2)
        self.element_click(['xpath', '//*[@class="ant-popover-buttons"]/button[1]'])

    def read_info(self):
        # 读取单个消息
        self.element_click(['xpath', '//*[@class="icon"][1]'])

    def read_all_info(self):
        # 标记全部已读
        self.element_click(['xpath', '//*[text()="全部已读"]'])

    def delete_all_info(self):
        # 全部删除
        self.element_click(['xpath', '//*[text()="全部删除"]'])

    def previous_page(self):
        # 点击上一页
        self.element_click(['xpath', '//*[@class="ant-pagination"]/li[1]'])

    def next_page(self):
        # 点击下一页
        self.element_click(['xpath', '//*[@class="ant-pagination"]/li[9]'])
    def view_read(self):
        # 查询已读消息
        self.element_click(['class', 'ant-select-selection-item'])
        self.element_click(['xpath', '//*[@class ="ant-select-item-option-content" and text()="已读"]'])

    def view_no_read(self):
        # 查询未读消息
        self.element_click(['class', 'ant-select-selection-item'])
        self.element_click(['xpath', '//*[@class ="ant-select-item-option-content" and text()="未读"]'])

    def view_all(self):
        # 查询全部消息
        self.element_click(['class', 'ant-select-selection-item'])
        self.element_click(['xpath', '//*[@class ="ant-select-item-option-content" and text()="全部消息"]'])




