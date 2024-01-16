import unittest

from selenium import webdriver

from xinfa.page.login_page import Login_Page
from xinfa.page.system_page import System_Page


class Test_Terminal(unittest.TestCase):
    def setUp(self) :
        self.driver=webdriver.Chrome()
        self.url = "http://192.168.11.4:8005/page/bank/user/login"
        self.name='admin'
        self.password='BanK2131'
        self.username = "admin"
        self.s=['testtest']
        self.m=['test','测试']
    def test_data(self):
        lg = Login_Page(self.driver)
        lg.open_url(self.url)
        lg.input_name(self.name)
        lg.input_password(self.password)
        lg.get_code()
        lg.input_code()
        lg.sleep(5)
        #测试添加机构类型
        nos=System_Page(self.driver)
        nos.new_sys()
        nos.sleep(5)
        nos.edit_Approvalsettings()


if __name__ == '__main__':
    unittest.main()