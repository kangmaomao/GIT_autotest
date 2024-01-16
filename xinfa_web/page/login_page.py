import time
from webbrowser import Chrome


from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.expected_conditions import visibility_of

from base_page import BasePage
from xinfa_web.utils import loggers

# 创建logger实例
log = loggers.Logger.getLogger()

class Login_Page(BasePage):

    def input_name(self, name):
        # 输入账号
        self.type(['id', 'userName'], name)


    def input_password(self, password):
        # 输入密码
        self.type(['id', 'password'], password)


    def get_code(self):
        # 验证码处理-使用OCR自动识别
        yzm = self.find_element(['xpath', '//*[@id="rc-tabs-0-panel-account"]/div[3]/div[2]/img'])
        yzm.screenshot('D:\\Python\\xinfa\\image\\a.png')

    def input_code(self):
        # 使用image_to_string识别验证码并输入验证码
        ocr = ddddocr.DdddOcr()
        with open("D:\\Python\\xinfa\\image\\a.png", "rb") as fp:
            image = fp.read()
        catch = ocr.classification(image)
        self.type(['id', 'code', ], catch)
        self.sleep(2)
        self.element_click(['xpath', '//*[@type="submit"]'])

        # message1 = self.find_element(['id', "logo"])
        # #message = self.get_text(['class',"ziDingYi___D-vy0"])
        # #message2 = "信息发布平台"
        # if visibility_of(message1):
        #     log.info("查询到信息，登录成功")
        # else:
        #     log.error("没有查询到信息，登录失败")
        #     self.sleep(2)
        #     self.delete(['xpath', '//*[@class="ant-input"]'])
        #     self.get_code()
        #     self.input_code()
        #     self.sleep(5)
        self.sleep(2)
        flag = self.is_exist(['id', "logo"])
        # el = self.find_element('xpath', '//*[@class="ant-message-custom-content ant-message-info"]')
        if flag != 0:
            log.info("查询到信息科技管理系统信息，登录成功")
        else:
            log.info("没有查询到信息科技管理系统信息，登录失败")
            el = self.get_text(['xpath', '//*[@class="ant-message-notice-content"]/div'])
            if el == "账户或密码错误":
                log.info("账号密码错误，退出")
                self.quit()
            else:
                self.sleep(2)
                self.delete(['xpath', '//*[@class="ant-input"]'])
                self.get_code()
                self.input_code()
                self.sleep(5)

        """
        message1=self.get_text(['class',"ziDingYi___D-vy0"])
        message2="信息发布平台"
        if message1 == message2:
            pass
        else:
            self.sleep(2)
            self.refresh()
            #self.clear(['xpath','//*[@class="ant-input"]'])
            #self.input_name("admin")
            self.input_password("BanK2131")
            self.get_code()
            self.input_code()
        """

    def login(self, name, password):
        # 输入账号密码
        Login_Page.input_name(self, name)
        Login_Page.input_password(self, password)
        Login_Page.get_code(self)
        Login_Page.input_code(self)
