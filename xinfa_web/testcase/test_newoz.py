import unittest

from selenium import webdriver

from login_page import Login_Page
from organizational_page_jigoulist import Organizational_Page_JigouList
class Test_newoz(unittest.TestCase):
    def setUp(self) :
        self.driver=webdriver.Chrome()
        self.url = "http://192.168.11.4:8005/page/bank/user/login"
        self.name='admin'
        self.password='BanK2131'
        self.s = ['test', '630', 'cesi', '', '', 'test']
    def test_data(self):
        lg = Login_Page(self.driver)
        lg.open_url(self.url)
        lg.input_name(self.name)
        lg.input_password(self.password)
        lg.get_code()
        lg.input_code()
        lg.sleep(5)
        #测试添加机构信息
        noz=Organizational_Page_JigouList(self.driver)
        noz.new_oz()
        noz.input_oz(self.s)
        noz.sleep(5)
if __name__ == '__main__':
    unittest.main()