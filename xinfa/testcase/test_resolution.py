import unittest

from selenium import webdriver

from xinfa_web.page.login_page import Login_Page
from xinfa_web.page.system_page import System_Page


class Test_Rseolution(unittest.TestCase):
    def setUp(self) :
        self.driver=webdriver.Chrome()
        self.url = "http://192.168.11.4:8005/page/bank/user/login"
        self.name='admin'
        self.password='BanK2131'
        self.username = "admin"
        self.s=['testtest','720','720']
        self.m=['newtest','1720','1720']
    def test_data(self):
        lg = Login_Page(self.driver)
        lg.open_url(self.url)
        lg.input_name(self.name)
        lg.input_password(self.password)
        lg.get_code()
        lg.input_code()
        lg.sleep(5)
        #测试分辨率
        nos=System_Page(self.driver)
        nos.new_sys()
        nos.input_rln(self.s)
        nos.sleep(5)
        nos.refresh()
        nos.sleep(5)
        nos.new_sys()
        nos.sleep(5)
        nos.edit_rln(self.m)


if __name__ == '__main__':
    unittest.main()