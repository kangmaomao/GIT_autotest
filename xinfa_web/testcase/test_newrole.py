import unittest

from selenium import webdriver

from xinfa_web.page.login_page import Login_Page
from xinfa_web.page.organizational_page_jigoulist import Organizational_Page_JigouList


class Test_Newrole(unittest.TestCase):
    def setUp(self) :
        self.driver=webdriver.Chrome()
        self.url = "http://192.168.11.4:8005/page/bank/user/login"
        self.name='admin'
        self.password='BanK2131'
        self.d= ['test74', 'test74', '13526821877', 'Test123456', '', '']
    def test_data(self):
        lg = Login_Page(self.driver)
        lg.open_url(self.url)
        lg.input_name(self.name)
        lg.input_password(self.password)
        lg.get_code()
        lg.input_code()
        lg.sleep(5)
        #测试增加用户
        nor=Organizational_Page_JigouList(self.driver)
        nor.new_oz()
        nor.input_user(self.d)
if __name__ == '__main__':
    unittest.main()