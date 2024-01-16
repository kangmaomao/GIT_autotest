import os

from selenium.webdriver.support.select import Select

from base_page import BasePage


class Resource_Page(BasePage):
    def new_res(self):
        # 进入资源管理，li后面的数字是资源管理所在位置
        self.element_click(['xpath', '//*[@id="root"]/div/section/aside/div/ul/li[4]'])
        self.sleep(2)

    """资源管理中的素材列表模块功能操作
    注意：新打开页面第一次点击资源管理时，各个模块的中间定位tabs后面的数字都是1，也就是“rc-tabs-1-tab-1”，第二个点击资源管理时“rc-tabs-2-tab-1”，其他列表同理
    """
    """选择机构"""

    def res_choose_oz(self,data):
        self.element_click(['xpath', '//*[@class="dev___1QLCE"]/div/div/span[1]'])
        self.move_to_element_click(['xpath', '//*[@class="ant-select-selection-item" and text()="%s"]' % (repr(data))])

    """新增素材分组"""

    def res_input_group(self, data):
        self.element_click(['xpath', '//*[@class="ant-row sideNavigation___1MAPi"]/div/div/div[2]'])
        self.sleep(2)
        file_name = data[0]
        self.type(['xpath', '//*[@class="ant-modal-body"]/div/div/div/div[2]/input'], file_name)
        self.element_click(['xpath', '//*[@class="ant-modal-body"]/div/div[3]/div/div/button'])

    """编辑素材分组"""

    def res_edit_group(self, data):
        #修改li后面的数字，可以编辑哪个分组
        self.move_to_element_click(['xpath', '//*[@class="ant-spin-container"]/ul/li[2]/div/div[2]/img'])
        self.sleep(2)
        file_name = data[0]
        self.element_click(['xpath', '//*[@class="ant-modal-body"]/div/div/div/div[2]/input'])
        self.delete(['xpath', '//*[@class="ant-modal-body"]/div/div/div/div[2]/input'])
        self.type(['xpath', '//*[@class="ant-modal-body"]/div/div/div/div[2]/input'], file_name)
        # 修改button前面的div的数字，1是确定，2是删除
        self.element_click(['xpath', '//*[@class="ant-modal-body"]/div/div[3]/div/div[1]/button'])

    """删除素材分组"""

    def res_delete_group(self):
        self.move_to_element_click(['xpath', '//*[@class="ant-spin-container"]/ul/li[2]/div/div[2]/img'])
        self.sleep(2)
        # tr后面的数字代表要删除终端类型的数据，button后面的数字，1是取消，2是确定
        self.element_click(['xpath', '//*[@class="ant-modal-body"]/div/div[3]/div/div/button'])
        self.element_click(['xpath', '//*[@class="ant-popover-buttons"]/button[2]'])

    """通过审核状态选择素材"""

    def res_find_auditing(self, data):
        self.element_click(['xpath', '//*[@class="ant-row ant-row-end"]/div[1]'])
        self.sleep(2)
        # 1是审核状态，2是待审核，3是审核中，4是审核通过，5是审核拒绝
        self.element_click(['xpath', '//*[@class="ant-select-item ant-select-item-option" and @title=%s]' % (repr(data))])
        self.sleep(2)

    """通过文件类型选择素材"""

    def res_find_filetype(self,data):
        self.element_click(['xpath', '//*[@class="ant-row ant-row-end"]/div[2]'])
        self.sleep(2)
        # 1是文件类型，2是WORD，3是PDF，4是视频，5是音乐，6是图片
        self.element_click(['xpath', '//*[@class="ant-select-item ant-select-item-option" and @title=%s]' % (repr(data))])
        self.sleep(2)

    """通过输入文件名称选择素材"""

    def res_find_filename(self, data):
        self.type(['class', 'ant-input'], data)
        self.sleep(2)
        self.element_click(['xpath', '//*[@class="ant-input-suffix"]'])
        self.sleep(2)

    """预览素材"""

    def res_preview(self):
        #第8个div后面的数字代表要预览的素材
        #self.click(['xpath', '//*[@class="ant-spin-container"]/div/div[1]/div/div/div/div/div/div/div/div[2]/button[1]'])
        self.move_to_element_click(['xpath','//*[@class="ant-tabs-tabpane ant-tabs-tabpane-active"]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div/div/button[1]'])
        self.sleep(20)
        self.element_click(['class', 'ant-modal-close-x'])
        self.sleep(2)

    """删除素材"""
    def res_delete_file(self):
        #第8个div后面的数字代表要预览的素材
        #self.click(['xpath', '//*[@class="ant-spin-container"]/div/div[1]/div/div/div/div/div/div/div/div[2]/button[2]'])
        self.move_to_element_click(['xpath','//*[@class="ant-tabs-tabpane ant-tabs-tabpane-active"]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div/div/button[2]'])
        self.sleep(2)
        #1是取消，2是确定
        self.element_click(['xpath', '//*[@class="ant-btn ant-btn-sm"][1]'])
        self.sleep(2)

    """上传素材"""

    def res_update_file(self, file_path):
        # 进入上传页面
        self.element_click(['xpath','//*[@class="ant-tabs-content ant-tabs-content-top"]/div/div/div[2]/div/div/div/div[1]/div/div[1]/button'])
        self.sleep(5)
        file_names = os.listdir(file_path)
        for file_name in file_names:
            full_file_name = file_path+'\\'+file_name
            self.type(['xpath', '//*[@class="ant-upload ant-upload-select ant-upload-select-picture-card"]/span/input'],full_file_name)
            self.sleep(20)
        # 上传完成关闭窗口
        self.element_click(['class', 'ant-modal-close-x'])
        self.sleep(2)

    """批量操作"""
    def res_all_operate(self):
        # 进入批量操作
        #self.click(['xpath','//*[@class="ant-tabs-content ant-tabs-content-top"]/div/div/div[2]/div/div/div/div[1]/div/div[2]/button'])
        self.element_click(['xpath','//*[@class="ant-tabs-tabpane ant-tabs-tabpane-active"]/div/div[2]/div/div[1]/div/div[1]/div/div[3]/button'])
        self.sleep(2)

    def res_all_operate_cancel(self):
        # 进行取消批量
        self.element_click(['xpath','//*[@class="ant-tabs-tabpane ant-tabs-tabpane-active"]/div/div[2]/div/div[1]/div/div[2]/div/div[1]/button'])
        self.sleep(2)

    def res_all_chose(self):
        # 进行全选
        self.element_click(['xpath','//*[@class="ant-tabs-tabpane ant-tabs-tabpane-active"]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/button'])
        self.sleep(2)
    def res_chose_file(self):
        #选择素材
        views = self.find_elements(['xpath','//*[@class="ant-card ant-card-hoverable contentItem___3YIqr"]/..'])
        for view in views:
            self.move_to_element_click(['xpath','//*[@class="contentItemMaskImg___13phR"]'])
            self.sleep(2)
    def res_all_delete(self):
        # 进行删除
        self.element_click(['xpath','//*[@class="ant-tabs-tabpane ant-tabs-tabpane-active"]/div/div[2]/div/div[1]/div/div[2]/div/div[3]/button'])
        self.sleep(2)

    def res_all_modify(self):
        # 进行修改有效期
        self.element_click(['xpath','//*[@class="ant-tabs-tabpane ant-tabs-tabpane-active"]/div/div[2]/div/div[1]/div/div[2]/div/div[4]/button'])
        self.sleep(2)
    def res_prev_page(self):
        # 点击上一页
        self.element_click(['xpath', '//*[@class="ant-pagination-prev"]'])
        self.sleep(2)
    def res_random_page(self,data):
        # 点击随机页，数字代表哪一页
        self.element_click(['xpath', '//*[@class="ant-pagination-item ant-pagination-item-%d"]' % data])
        self.sleep(2)
    def res_next_page(self):
        # 点击下一页
        self.element_click(['xpath', '//*[@class="ant-pagination-next"]'])
        self.sleep(2)
    def res_prev_five(self):
        # 点击向前五页
        self.move_to_element_click(['xpath', '//*[@class="ant-pagination-jump-prev ant-pagination-jump-prev-custom-icon"]'])
        self.sleep(2)
    def res_next_five(self):
        # 点击向后五页
        self.move_to_element_click(['xpath', '//*[@class="ant-pagination-jump-next ant-pagination-jump-next-custom-icon"]'])
        self.sleep(2)
    def res_all_shear(self):
        # 进行剪切
        self.element_click(['xpath','//*[@class="ant-tabs-tabpane ant-tabs-tabpane-active"]/div/div[2]/div/div[1]/div/div[2]/div/div[5]/button'])
        self.sleep(2)

    """发布素材"""

    def res_release_file(self):
        # 进入发布页面
        #self.click(['xpath','//*[@class="ant-tabs-content ant-tabs-content-top"]/div/div/div[2]/div/div/div/div[1]/div/div[2]/button'])
        self.move_to_element_click(['xpath','//*[@class="ant-tabs-tabpane ant-tabs-tabpane-active"]/div/div[2]/div/div[1]/div/div[1]/div/div[2]/button'])
        self.sleep(2)

    def res_close_page(self):
        # 关闭素材库页面
        self.element_click(['xpath', '//*[@class="anticon anticon-close ant-modal-close-icon"]'])
        self.sleep(2)

    def res_forword_page(self):
        # 返回上一级
        self.element_click(['xpath', '//*[@class="ant-pro-grid-content"]/div/div/div/div[2]/a'])
        self.sleep(2)

    def res_play_model(self):
        # 设置播放方式,包括轮播，插播，兜底
        # self.move_to_element_click(['xpath', '//*[@class="ant-select-selection-item" and  text=%s]' % (repr(data))])
        # self.sleep(2)
        # self.element_click(['xpath', '//*[@class="ant-select-selection-item" and @title="轮播"]'])

        js = "document.querySelectorAll('.ant-select-selector')[1].style.display='block';"
        self.use_js(js)
        sel =self.find_element(['xpath', '//*[@id="root"]/div/section/section/div/main/div/div/div/div[2]/div/div[2]/div[1]/div'])
        Select(sel).select_by_value('兜底')

    def res_setup_model(self,data):
        # 设置方式,包括批量设置，单独设置
        self.move_to_element_click(['xpath', '//*[@class="ant-select-selection-item" and text=%s]' % (repr(data))])
        self.sleep(2)

    def res_setup_playtime(self):
        # 设置播放时间
        self.element_click(['xpath', '//*[@class="ant-collapse-header"]'])
        self.sleep(2)

    def res_playtime_everyday(self):
        # 设置播放时间，每天播放
        self.move_to_element_click(['xpath', '//*[@class="ant-col ant-col-24 weekDayCheckBox___bskxi"]/div/label[1]'])
        self.sleep(2)

    def res_playtime_week(self):
        # 设置播放时间，每天最后一位数字为1，周几播放为（2，3,4,5,6,7，8）
        self.move_to_element_click(['xpath', '//*[@class="ant-col ant-col-24 weekDayCheckBox___bskxi"]/div/label[2]'])
        self.sleep(2)
    def res_playtime_data(self,data,data2):
        # 设置播放日期,data是日期xxxx-xx-xx
        # js_value1 = "document.getElementsByClassName('ant-picker-input')[0].click()"
        # js_value2 = "document.getElementsByClassName('ant-picker-input')[0].value = '2023-09-16'"
        # self.use_js(js_value1)
        # self.use_js(js_value2)
        self.type_enter(['xpath','//*[@class="ant-collapse-content-box"]/div/div[2]/div/div[2]/div/div/input'],data)
        self.sleep(2)
        self.type_enter(['xpath','//*[@class="ant-collapse-content-box"]/div/div[2]/div/div[4]/div/div/input'],data2)
        self.sleep(2)
        #self.move_to_element_click(['xpath','/html/body/div[3]/div/div/div/div/div/div[2]/table/tbody/tr/td[@title=%s]/div'% (repr(data2))])
        #self.move_to_element_click(['xpath', '/html/body/div[3]/div/div/div/div/div/div[2]/table/tbody/tr/td[@title="2023-09-25"]/div' ])

    def res_playtime_other_data(self,data,data2):
        # 添加一个播放时间，data是时间，xx:xx:xx,添加播放时间后，播放日期的定位出现改变
        #number增加一次，//*[@class="ant-collapse-content-box"]/div/div[4]的数字增加2,/html/body/div[4]数字依次增加
        self.element_click(['class', 'anticon anticon-plus-circle'])
        self.type_enter(['xpath','//*[@class="ant-collapse-content-box"]/div/div[4]/div/div[2]/div/div/input'],data)
        self.sleep(2)
        #self.click(['xpath','/html/body/div[3]/div/div/div/div/div[2]/ul/li[2]/button'])
        self.type_enter(['xpath','//*[@class="ant-collapse-content-box"]/div/div[4]/div/div[4]/div/div/input'],data2)
        self.sleep(2)
        #self.click(['xpath','/html/body/div[4]/div/div/div/div/div[2]/ul/li[2]/button'])
    def res_play_button(self):
        # 点击添加按钮，进入选择播放素材
        self.element_click(['xpath', '//*[@class="ant-btn ant-btn-round"]'])
        self.sleep(2)

    def res_play_class(self):
        # 选择素材分类，div后面的数字代表不同类别：1是全部，2是图片,3是视频，4是PDF
        self.element_click(['xpath', '//*[@class="ant-tabs-nav-list"]/div[2]'])
        self.sleep(2)

    def res_play_floder(self):
        # 选择素材文件夹，li后面的数字代表文件夹：1是全部，2是。。。
        self.element_click(['xpath', '//*[@class="ant-menu ant-menu-sub ant-menu-inline"]/li[2]'])
        self.sleep(2)
    def res_play_jigou(self,data):
        # 选择机构,显示素材
        #self.move_to_element_click(['xpath', '//*[@class="ant-select-tree-list-holder-inner"]'[2]])
        self.element_click(['xpath', '//*[@id="rcDialogTitle0"]/div[2]/div/div[1]/div/div'])
        self.sleep(2)
        # li=self.find_elements(['xpath', '//*[@class="ant-select-tree-treenode ant-select-tree-treenode-switcher-open"]'])
        # s=li[2]
        self.move_to_element_click(['xpath', '//*[@class="ant-select-selection-item" and text()="%s"]' % (repr(data))])
        self.sleep(5)

    def res_play_inputname(self,data):
        # 输入名称，点击搜索
        self.type(['class', 'ant-input'],data)
        self.sleep(2)
        self.element_click(['xpath', '//*[@class="anticon anticon-search ant-input-search-icon"]'])
        self.sleep(2)

    def res_play_view(self):
        #选择素材，点击添加后，点击确定，定位子元素的父级元素
        views = self.find_elements(['xpath','//div[@class="ant-col releaseAddMask___1bOcZ"]/..'])
        for view in views:
            view.click()
            self.sleep(2)
        self.element_click(['xpath', '//*[@class="ant-modal-body"]/div/div/div/div[2]/div/div[2]/button'])

    def res_play_device_jigou(self,data):
        # 选择机构,显示设备
        self.element_click(['xpath', '//*[@id="rc_select_2"]'])
        self.sleep(2)
        self.move_to_element_click(['xpath', '//*[@class="ant-select-selection-item" and text()="%s"]' % (repr(data))])
        self.sleep(2)
    def res_play_device_fenbian(self,data):
        # 选择分辨率,显示设备
        self.sleep(2)
        self.move_to_element_click(['xpath', '//*[@class="ant-select-selection-item" and text()="%s"]' % (repr(data))])
        self.sleep(2)
    def res_play_device_sys(self,data):
        # 选择分辨率,显示设备
        self.sleep(2)
        self.move_to_element_click(['xpath', '//*[@class="ant-select-selection-item" and text()="%s"]' % (repr(data))])
        self.sleep(2)
    def res_play_device_inputname(self,data):
        # 输入名称，点击搜索
        self.type(['class', 'ant-input'],data)
        self.sleep(2)
        self.element_click(['xpath', '//*[@class="ant-btn ant-btn-icon-only ant-input-search-button"]'])
        self.sleep(2)
    def res_play_device_allchose(self,data):
        # 全选设备
        self.type(['class', 'ant-btn'],data)
        self.sleep(2)
    def res_play_device_chose(self):
        # 选择设备,tr后面的数字代表选择的是哪个设备
        self.element_click(['xpath', '//*[@class="ant-table-tbody"]/tr[3]/td[1]/label/span/input'])
        self.sleep(2)
    def res_play_device_prev(self):
        # 选择设备,点击上一页
        self.element_click(['xpath', '//*[@class="ant-pagination-prev"]'])
        self.sleep(2)
    def res_play_device_random(self,data):
        # 选择设备,点击随机页，数字代表哪一页
        self.element_click(['xpath', '//*[@class="ant-pagination-item ant-pagination-item-%d"]' % data])
        self.sleep(2)
    def res_play_device_next(self):
        # 选择设备,点击下一页
        self.element_click(['xpath', '//*[@class="ant-pagination-next"]'])
        self.sleep(2)
    def res_play_submit(self):
        # 点击确定
        self.element_click(['xpath', '//*[@class="ant-btn ant-btn-primary"]'])
        self.sleep(2)

    """素材审核页面操作"""
    def res_check_page(self):
        #进入素材审核页面
        self.element_click(['xpath', '//*[@class="ant-tabs-nav-wrap"]/div/div[2]'])

    def res_check_choose_oz(self,data):
        # 选择机构
        self.element_click(['xpath', '//*[@class="dev___1QLCE"]/div/div/span[1]'])
        self.move_to_element_click(['xpath', '//*[@class="ant-select-selection-item" and text()="%s"]' % (repr(data))])

    def res_check_file(self,data):
        # 根据文件类型选择素材
        self.element_click(['xpath', '//*[@class="ant-col ant-col-12 headRight___3VujF"]/div/div/span[1]'])
        # 1是文件类型，2是WORD，3是PDF，4是视频，5是音乐，6是图片
        self.element_click(['xpath', '//*[@class="ant-select-item ant-select-item-option" and @title=%s]' % (repr(data))])
        self.sleep(2)
    def res_check_find_filename(self, data):
        #输入信息，点击搜索待审核素材
        self.type(['class', 'ant-input'], data)
        self.sleep(2)
        self.element_click(['xpath', '//*[@class="ant-input-suffix"]'])
        self.sleep(2)

    def res_check_view(self,number):
        #选择素材，点击审核，定位子元素的父级元素
        views = self.find_elements(['xpath','//div[@class="ant-card ant-card-hoverable itemBox___13pi3"]/..'])
        #views = self.find_elements(['xpath', '//div[@class="ant-card ant-card-hoverable itemBox___13pi3"]'])
        for view in views:
            if view == views[number]:
                self.element_click(['xpath', '//button[@class="ant-btn buttonAudit___3A97h"]'])
                self.sleep(2)

    def res_check_open_filename(self):
        # 是否公开素材
        self.element_click(['xpath', '//*[@class="ant-modal-body"]/div[1]/div/button'])
    def res_check_pass(self,data):
        # 输入通过原因，并通过
        self.type(['class', 'ant-input auditText___vIKyM'], data)
        self.sleep(2)
        self.element_click(['xpath', '//*[@class="ant-btn ant-btn-primary auditButtomPass___3PUbE"]'])
    def res_check_fail(self,data):
        # 输入驳回原因，并驳回
        self.type(['class', 'ant-input auditText___vIKyM'], data)
        self.sleep(2)
        self.element_click(['xpath', '//*[@class="ant-btn auditButtomReject___3jYg8"]'])
    def res_check_reason(self,data):
        # 输入审核原因，并通过
        self.type(['class', 'ant-input auditText___vIKyM'], data)
        self.sleep(2)
        self.element_click(['xpath', '//*[@class="ant-btn ant-btn-primary auditButtomPass___3PUbE"]'])
    def res_check_cancel(self):
        # 取消审核
        self.element_click(['xpath', '//*[@class="ant-btn auditButtomReject___3jYg8"]'])
    def res_check_all_file(self):
        # 选择全部待审核素材
        self.element_click(['xpath', '//*[@class="ant-row header___3_dF9"]/div/button[1]'])

    def res_check_allfile_pass(self):
        # 批量通过素材
        self.element_click(['xpath', '//*[@class="ant-row header___3_dF9"]/div/button[2]'])

    def res_check_allfile_fail(self):
        # 批量驳回素材
        self.element_click(['xpath', '//*[@class="ant-row header___3_dF9"]/div/button[3]'])
    def res_check_prev_five(self):
        # 选择节目,点击向前五页
        self.move_to_element_click(['xpath', '//*[@class="ant-pagination-jump-prev ant-pagination-jump-prev-custom-icon"]'])
        self.sleep(2)
    def res_check_next_five(self):
        # 选择节目,点击向后五页
        self.move_to_element_click(['xpath', '//*[@class="ant-pagination-jump-next ant-pagination-jump-next-custom-icon"]'])
        self.sleep(2)
