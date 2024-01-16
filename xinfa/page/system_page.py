from base_page import BasePage

class System_Page(BasePage):
    def new_sys(self):
        # 进入系统设置，li后面的数字是系统设置所在位置
        self.element_click(['xpath', '//*[@id="root"]/div/section/aside/div/ul/li[12]'])
        self.sleep(2)

    """系统设置中的分辨率列表模块功能操作
    注意：新打开页面第一次点击系统设置时，各个模块的中间定位tabs后面的数字都是1，也就是“rc-tabs-1-tab-1”，第二个点击系统设置时“rc-tabs-2-tab-1”，其他列表同理
    """
    """新增分辨率"""
    def input_rln(self,data):
        #新增分辨率resolution，输入新增分辨率的值
        #self.click(['id','rc-tabs-1-tab-1'])
        self.element_click(['class', 'ant-btn'])
        self.sleep(2)
        form_in_modal_name=data[0]
        form_in_modal_width=data[1]
        form_in_modal_height=data[2]
        self.type(['id','form_in_modal_name'],form_in_modal_name)
        self.type(['id','form_in_modal_width'],form_in_modal_width)
        self.type(['id','form_in_modal_height'],form_in_modal_height)
        self.element_click(['xpath', '//*[@class="ant-modal-body"]/button'])

    """编辑分辨率
    注意：先新增分辨率后在修改分辨率，同一个定位会出现两个位置，会冲突，先刷新，在定位
    """
    def edit_rln(self,data):

        #tr后面的数字代表要修改哪个分辨率的数据
        #self.click(['id','rc-tabs-1-tab-1'])
        self.element_click(['xpath', '//*[@class="ant-table-tbody"]/tr[3]/td[4]/span/a[1]'])
        self.sleep(2)
        form_in_modal_name=data[0]
        form_in_modal_width=data[1]
        form_in_modal_height=data[2]
        self.element_click(['css', '#form_in_modal_name'])
        self.sleep(2)
        self.delete(['css','#form_in_modal_name'])
        self.sleep(2)
        self.type(['id','form_in_modal_name'],form_in_modal_name)
        self.sleep(2)
        self.element_click(['xpath', '//*[@id="form_in_modal_width"]'])
        self.delete(['xpath','//*[@id="form_in_modal_width"]'])
        self.sleep(2)
        self.type(['id','form_in_modal_width'],form_in_modal_width)
        self.sleep(2)
        self.element_click(['xpath', '//*[@id="form_in_modal_height"]'])
        self.delete(['xpath','//*[@id="form_in_modal_height"]'])
        self.sleep(2)
        self.type(['id','form_in_modal_height'],form_in_modal_height)
        self.element_click(['xpath', '//*[@class="ant-modal-body"]/button'])


    """删除分辨率"""
    def delete_rln(self):
        self.element_click(['id', 'rc-tabs-1-tab-1'])
        #tr后面的数字代表要删除哪个分辨率的数据，button后面的数字，1是取消，2是确定
        self.element_click(['xpath', '//*[@class="ant-table-tbody"]/tr[2]/td[4]/span/a[2]'])
        self.element_click(['xpath', '//*[@class="ant-modal-confirm-btns"]/button[1]'])



    """新增机构结构"""
    def input_instn(self,data,json):
        #新增机构结构institution，输入新增机构结构
        self.element_click(['id', 'rc-tabs-1-tab-2'])
        self.element_click(['class', 'ant-btn'])
        self.sleep(2)
        form_in_modal_name=data[0]
        self.type(['id','form_in_modal_name'],form_in_modal_name)
        self.element_click(['id', 'form_in_modal_parentId'])
        # 可以根据需求添加哪个机构，修改text机构名称
        self.move_to_element_click(['xpath','//*[@class="ant-select-tree-title" and text()="%s"]' % (repr(json))])
        self.sleep(2)
        self.element_click(['xpath', '//*[@class="ant-modal-body"]/button'])

    """编辑机构结构"""
    def edit_instn(self,data):
        #编辑机构结构institution，修改机构结构数据
        self.element_click(['id', 'rc-tabs-1-tab-2'])
        #tr后面的数字代表要修改哪个机构的数据
        self.element_click(['xpath', '//*[@class="ant-table-tbody"]/tr[3]/td[3]/span/a[1]'])
        self.sleep(2)
        form_in_modal_name=data[0]
        form_in_modal_details=data[1]
        self.element_click(['xpath', '//*[@id="form_in_modal_name"]'])
        self.delete(['xpath','//*[@id="form_in_modal_name"]'])
        self.type(['id','form_in_modal_name'],form_in_modal_name)
        self.element_click(['xpath', '//*[@id="form_in_modal_details"]'])
        self.delete(['xpath','//*[@id="form_in_modal_details"]'])
        self.type(['id', 'form_in_modal_details'], form_in_modal_details)
        self.sleep(2)
        self.element_click(['xpath', '//*[@class="ant-modal-body"]/button'])

    """删除机构结构"""
    def delete_instn(self):
        self.element_click(['id', 'rc-tabs-1-tab-2'])
        #tr后面的数字代表要删除哪个机构的数据，button后面的数字，1是取消，2是确定
        self.element_click(['xpath', '//*[@class="ant-table-tbody"]/tr[3]/td[3]/span/a[2]'])
        self.element_click(['xpath', '//*[@class="ant-modal-confirm-btns"]/button[1]'])


    """新增系统权限"""
    def input_syspms(self,data,json1,json2):
        #新增系统权限System permissions，输入新增系统权限数据
        self.element_click(['id', 'rc-tabs-1-tab-3'])
        self.sleep(2)
        self.element_click(['class', 'ant-btn'])
        self.sleep(2)
        normal_login_menuName=data[0]
        normal_login_menuUrl = data[1]
        normal_login_menuOrder = data[2]
        self.type(['id','normal_login_menuName'],normal_login_menuName)
        self.type(['id','normal_login_menuUrl'],normal_login_menuUrl)
        self.type(['id','normal_login_menuOrder'],normal_login_menuOrder)
        self.element_click(['id', 'normal_login_caiDan'])
        # 可以根据需求添加哪个系统权限，修改text名称（菜单和按钮）来选择菜单属性
        self.move_to_element_click(['xpath','//*[@class="ant-select-tree-title" and text()="%s"]' % (repr(json1))])
        self.sleep(2)
        self.element_click(['id', 'normal_login_shangji'])
        # 可以根据需求添加哪个系统权限，修改text名称，来选择上级机构
        self.move_to_element_click(['xpath','//*[@class="ant-select-tree-title" and text()="%s"]' % (repr(json2))])
        self.sleep(2)
        self.element_click(['xpath', '//*[@type="submit"]'])

    """编辑系统权限"""
    def edit_syspms(self,data,json1,json2):
        #编辑系统权限System permissions，修改系统权限数据
        self.element_click(['id', 'rc-tabs-1-tab-3'])
        self.sleep(2)
        #tr后面的数字代表要展开哪个权限机构列表
        self.element_click(['xpath', '//*[@class="ant-table-tbody"]/tr/td/button'])
        self.sleep(2)
        #tr后面的数字代表要修改哪个系统权限的数据
        self.element_click(['xpath', '//*[@class="ant-table-tbody"]/tr[2]/td[6]/span/a[1]'])
        self.sleep(2)
        normal_login_menuName=data[0]
        normal_login_menuUrl = data[1]
        normal_login_menuOrder = data[2]
        self.element_click(['xpath', '//*[@id="normal_login_menuName"]'])
        self.delete(['xpath','//*[@id="normal_login_menuName"]'])
        self.type(['id','normal_login_menuName'],normal_login_menuName)
        self.sleep(2)
        self.element_click(['xpath', '//*[@id="normal_login_menuUrl"]'])
        self.delete(['xpath','//*[@id="normal_login_menuUrl"]'])
        self.type(['id','normal_login_menuUrl'],normal_login_menuUrl)
        self.sleep(2)
        self.element_click(['xpath', '//*[@id="normal_login_menuOrder"]'])
        self.delete(['xpath','//*[@id="normal_login_menuOrder"]'])
        self.type(['id','normal_login_menuOrder'],normal_login_menuOrder)
        self.sleep(2)
        # 定位到元素菜单类型
        self.element_click(['xpath', '//*[@class="ant-select-selection-item" and text()="%s"]' % (repr(json1))])
        # 可以根据需求添加哪个系统权限，修改text名称（菜单和按钮）来选择菜单属性
        self.move_to_element_click(['xpath','//*[@class="ant-select-tree-title" and text()="%s"]' % (repr(json1))])
        self.sleep(2)
        # 定位到元素上级机构
        self.element_click(['xpath', '//*[@class="ant-select-selection-item" and text()="%s"]' % (repr(json2))])
        # 可以根据需求添加哪个系统权限，修改text名称，来选择上级机构
        self.move_to_element_click(['xpath','//*[@class="ant-select-tree-title" and text()="%s"]' % (repr(json2))])
        self.sleep(2)
        self.element_click(['xpath', '//*[@type="submit"]'])

    """删除系统权限"""
    def delete_syspms(self):
        self.element_click(['id', 'rc-tabs-1-tab-3'])
        #tr后面的数字代表要展开哪个权限机构列表
        self.element_click(['xpath', '//*[@class="ant-table-tbody"]/tr/td/button'])
        #tr后面的数字代表要删除系统权限的数据，button后面的数字，1是取消，2是确定
        self.element_click(['xpath', '//*[@class="ant-table-tbody"]/tr[2]/td[6]/span/a[2]'])
        self.element_click(['xpath', '//*[@class="ant-modal-confirm-btns"]/button[2]'])


    """修改系统配置"""

    def edit_sysconf(self, data):
        # 修改系统配置system configuration，输入修改系统配置数据
        self.element_click(['id', 'rc-tabs-1-tab-4'])
        self.sleep(2)
        #输入外网地址和端口，内网地址和端口，账号，秘钥key
        normal_login_imgServerUrl = data[0]
        normal_login_imgServerPort = data[1]
        normal_login_innerImgServerUrl = data[2]
        normal_login_innerImgServerPort = data[3]
        normal_login_imgServerAccessKey = data[4]
        normal_login_imgServerSecretKey = data[5]
        self.element_click(['xpath', '//*[@id="normal_login_imgServerUrl"]'])
        self.delete(['xpath','//*[@id="normal_login_imgServerUrl"]'])
        self.type(['id', 'normal_login_imgServerUrl'], normal_login_imgServerUrl)
        self.sleep(2)
        self.element_click(['xpath', '//*[@id="normal_login_imgServerPort"]'])
        self.delete(['xpath','//*[@id="normal_login_imgServerPort"]'])
        self.type(['id', 'normal_login_imgServerPort'], normal_login_imgServerPort)
        self.sleep(2)
        self.element_click(['xpath', '//*[@id="normal_login_innerImgServerUrl"]'])
        self.delete(['xpath','//*[@id="normal_login_innerImgServerUrl"]'])
        self.type(['id', 'normal_login_innerImgServerUrl'], normal_login_innerImgServerUrl)
        self.sleep(2)
        self.element_click(['xpath', '//*[@id="normal_login_innerImgServerPort"]'])
        self.delete(['xpath','//*[@id="normal_login_innerImgServerPort"]'])
        self.type(['id', 'normal_login_innerImgServerPort'], normal_login_innerImgServerPort)
        self.sleep(2)
        self.element_click(['xpath', '//*[@id="normal_login_imgServerAccessKey"]'])
        self.delete(['xpath','//*[@id="normal_login_imgServerAccessKey"]'])
        self.type(['id', 'normal_login_imgServerAccessKey'], normal_login_imgServerAccessKey)
        self.sleep(2)
        self.element_click(['xpath', '//*[@id="normal_login_imgServerSecretKey"]'])
        self.delete(['xpath','//*[@id="normal_login_imgServerSecretKey"]'])
        self.type(['id', 'normal_login_imgServerSecretKey'], normal_login_imgServerSecretKey)
        self.sleep(2)
        self.element_click(['xpath', '//*[@type="submit"]'])



    """编辑终端类型"""
    def edit_TerminalType(self,data):
        #编辑终端类型Terminal Type，修改终端类型数据
        self.element_click(['id', 'rc-tabs-1-tab-5'])
        self.sleep(2)
        #tr后面的数字代表要修改哪个终端类型的数据
        self.element_click(['xpath', '//*[@class="ant-table-tbody"]/tr[1]/td[8]/div/a[1]'])
        self.sleep(2)
        #缩略图涉及上传文件，暂时没有好办法解决，待定
        basic_name=data[0]
        basic_path = data[1]
        basic_sort = data[2]
        self.element_click(['xpath', '//*[@id="basic_name"]'])
        self.delete(['xpath','//*[@id="basic_name"]'])
        self.type(['id','basic_name'],basic_name)
        self.sleep(2)
        self.element_click(['xpath', '//*[@id="basic_path"]'])
        self.delete(['xpath','//*[@id="basic_path"]'])
        self.type(['id','basic_path'],basic_path)
        self.sleep(2)
        self.element_click(['xpath', '//*[@id="basic_sort"]'])
        self.delete(['xpath','//*[@id="basic_sort"]'])
        self.type(['id','basic_sort'],basic_sort)
        self.sleep(2)
        self.element_click(['xpath', '//*[@type="submit"]'])

    """删除终端类型"""
    def delete_TerminalType(self):
        self.element_click(['id', 'rc-tabs-1-tab-5'])
        #tr后面的数字代表要删除终端类型的数据，button后面的数字，1是取消，2是确定
        self.element_click(['xpath', '//*[@class="ant-table-tbody"]/tr[1]/td[8]/div/a[2]'])
        self.element_click(['xpath', '//*[@class="ant-popover-buttons"]/button[2]'])


    """设置审批设置"""
    def edit_Approvalsettings(self):
        self.element_click(['id', 'rc-tabs-1-tab-6'])
        self.sleep(2)
        #编辑审批设置Approval Settings，div后面的数字代表设置哪个审批，1是节目审批设置，2是素材审核设置
        self.element_click(['xpath', '//*[@class="ant-row"]/div[1]/button'])
        self.sleep(2)
        self.element_click(['xpath', '//*[@class="ant-row"]/div[2]/button'])


    """设备注册页面添加设备数量"""
    def registration_device(self):
        self.element_click(['id', 'rc-tabs-1-tab-7'])
        self.sleep(2)
        #添加设备数量
        self.element_click(['xpath', '//*[@class="ant-row"]/div/button'])
        self.sleep(2)
        #手机扫码授权数量，输入授权码
        self.type(['class','ant-input'])


    """新增软件版本"""
    def input_softversion(self,data,json1,json2):
        #新增软件版本Software version，输入新增软件版本数据
        self.element_click(['id', 'rc-tabs-1-tab-8'])
        self.sleep(2)
        self.element_click(['class', 'ant-btn headerButton___2_DYG'])
        self.sleep(2)
        basic_title=data[0]
        basic_appVersion = data[1]
        basic_versionCode = data[2]
        basic_details = data[3]
        self.type(['id','basic_title'],basic_title)
        self.type(['id','basic_appVersion'],basic_appVersion)
        self.type(['id','basic_versionCode'],basic_versionCode)
        self.type(['id','basic_details'],basic_details)
        self.element_click(['id', 'basic_systemType'])
        # 可以根据需求添加哪个系统，修改text名称（Android和Windows）来选择系统
        self.move_to_element_click(['xpath','//*[@class="ant-select-item-option-content" and text()="%s"]' % (repr(json1))])
        self.sleep(2)
        self.element_click(['id', 'basic_deviceSoftType'])
        # 可以根据需求添加哪个软件类型，修改text名称（双面屏(单面屏)，厅堂营销，公告公示，精准营销，打卡分享，周边商户，
        # 全息贵金属，幸运大转盘，透明展示柜，拼接数据屏(单面屏)），来选择软件类型
        self.move_to_element_click(['xpath','//*[@class="ant-select-item-option-content" and text()="%s"]' % (repr(json2))])

        #上传软件包暂时不会实现，后续更新
        self.sleep(2)
        self.element_click(['xpath', '//*[@type="submit"]'])

    """编辑软件版本"""
    def edit_softversion(self,data):
        #编辑软件版本Software version，修改软件版本数据
        self.element_click(['id', 'rc-tabs-1-tab-8'])
        self.sleep(2)
        #tr后面的数字代表要修改哪个软件版本的数据
        self.element_click(['xpath', '//*[@class="ant-table-tbody"]/tr[2]/td[9]/span/a[2]'])
        self.sleep(2)
        basic_title=data[0]
        basic_appVersion = data[1]
        basic_details = data[2]
        self.element_click(['xpath', '//*[@id="basic_title"]'])
        self.delete(['xpath','//*[@id="basic_title"]'])
        self.type(['id','basic_title'],basic_title)
        self.sleep(2)
        self.element_click(['xpath', '//*[@id="basic_appVersion"]'])
        self.delete(['xpath','//*[@id="basic_appVersion"]'])
        self.type(['id','basic_appVersion'],basic_appVersion)
        self.sleep(2)
        self.element_click(['xpath', '//*[@id="basic_details"]'])
        self.delete(['xpath','//*[@id="basic_details"]'])
        self.type(['id','basic_details'],basic_details)
        self.sleep(2)
        self.element_click(['xpath', '//*[@type="submit"]'])

    """更新到设备"""
    def update_device(self):
        self.element_click(['id', 'rc-tabs-1-tab-8'])
        self.sleep(2)
        #tr后面的数字代表要修改哪个软件版本的数据
        self.element_click(['xpath', '//*[@class="ant-table-tbody"]/tr[2]/td[9]/span/a[1]'])
        self.sleep(2)
    """在更新设备页面操作"""
    """根据机构搜索设备"""
    def search_oz(self,json1,json2):
        self.element_click(['xpath', '//*[@class="ant-select-selection-item" and text()="%s"]' % (repr(json1))])
        self.sleep(2)
        # 可以根据需求选择哪个机构，修改text机构名称
        self.move_to_element_click(['xpath','//*[@class="ant-select-tree-title" and text()="%s"]' % (repr(json2))])
    """根据终端类型搜索设备"""
    def search_terminal(self,json1,json2):
        self.element_click(['xpath', '//*[@class="ant-select-selection-item" and text()="%s"]' % (repr(json1))])
        self.sleep(2)
        #可以根据需求添加哪个软件类型，修改text名称（双面屏(单面屏)，厅堂营销，公告公示，精准营销，打卡分享，周边商户，
        # 全息贵金属，幸运大转盘，透明展示柜，拼接数据屏(单面屏)），来选择软件类型
        self.move_to_element_click(['xpath', '//*[@class="ant-select-item-option-content" and text()="%s"]' % (repr(json2))])
    """根据分辨率搜索设备"""
    def search_rln(self):
        self.element_click(['xpath', '//*[@id="rc_select_31"]'])
        self.sleep(2)
        # 可以根据需求选择哪个分辨率，修改rc_select_31_list_5最后一位数字
        self.move_to_element_click(['xpath','//*[@aria-activedescendant="rc_select_31_list_5"]'])
    """根据输入名称搜索设备"""
    def input_devicename(self,data):
        self.type(['class','ant-input'],data)
        self.sleep(2)
        #点击搜索
        self.element_click(['class', 'ant-input-suffix'])
    """全选设备"""
    def choose_all(self):
        self.element_click(['xpath', '//*[@class="ant-table-thead"]/tr/th[1]/div/label/span'])
    """单选设备"""
    def choose_one(self):
        #tr后面的数字代表要选择哪个设备
        self.element_click(['xpath', '//*[@class="ant-table-tbody"]/tr[1]/td[1]/label/span'])
    def choose_two(self):
        #tr后面的数字代表要选择哪个设备
        self.element_click(['xpath', '//*[@class="ant-table-tbody"]/tr[2]/td[1]/label/span'])
    def choose_three(self):
        #tr后面的数字代表要选择哪个设备
        self.element_click(['xpath', '//*[@class="ant-table-tbody"]/tr[2]/td[1]/label/span'])
    def choose_four(self):
        # tr后面的数字代表要选择哪个设备
        self.element_click(['xpath', '//*[@class="ant-table-tbody"]/tr[4]/td[1]/label/span'])
    def choose_five(self):
        #tr后面的数字代表要选择哪个设备
        self.element_click(['xpath', '//*[@class="ant-table-tbody"]/tr[5]/td[1]/label/span'])
    def choose_six(self):
        #tr后面的数字代表要选择哪个设备
        self.element_click(['xpath', '//*[@class="ant-table-tbody"]/tr[6]/td[1]/label/span'])
    def choose_seven(self):
        #tr后面的数字代表要选择哪个设备
        self.element_click(['xpath', '//*[@class="ant-table-tbody"]/tr[7]/td[1]/label/span'])
    """选择上一页设备"""
    def choose_previous(self):
        #tr后面的数字代表要选择哪个设备
        self.element_click(['xpath', '//*[@class="ant-pagination-prev"]'])
    """选择下一页设备"""
    def choose_next(self):
        #tr后面的数字代表要选择哪个设备
        self.element_click(['xpath', '//*[@class="ant-pagination-next"]'])
    """发布软件版本"""
    def update_soft(self):
        self.element_click(['id', 'rc-tabs-1-tab-8'])
        self.sleep(2)
        #tr后面的数字代表要修改哪个软件版本的数据
        self.element_click(['xpath', '//*[@class="ant-table-tbody"]/tr[2]/td[9]/span/a[3]'])

    """删除软件版本"""
    def delete_softversion(self):
        self.element_click(['id', 'rc-tabs-1-tab-8'])
        self.sleep(2)
        #tr后面的数字代表要修改哪个软件版本的数据
        self.element_click(['xpath', '//*[@class="ant-table-tbody"]/tr[2]/td[9]/span/a[4]'])
        self.sleep(2)
        self.element_click(['xpath', '//*[@class="ant-popover-buttons"]/button[2]'])
    """只有一个删除按钮的"""
    def delete_softversion2(self):
        self.element_click(['id', 'rc-tabs-1-tab-8'])
        self.sleep(2)
        #tr后面的数字代表要修改哪个软件版本的数据
        self.element_click(['xpath', '//*[@class="ant-table-tbody"]/tr[9]/td[9]/span/a'])
        self.sleep(2)
        self.element_click(['xpath', '//*[@class="ant-popover-buttons"]/button[2]'])

