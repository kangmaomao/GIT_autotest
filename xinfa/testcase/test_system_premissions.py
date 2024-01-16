import unittest

from selenium import webdriver

from xinfa.page.login_page import Login_Page
from xinfa.page.system_page import System_Page


class Test_System_Permissions(unittest.TestCase):
    def setUp(self) :
        self.driver=webdriver.Chrome()
        self.url = "http://192.168.11.4:8005/page/bank/user/login"
        self.name='admin'
        self.password='BanK2131'
        self.username = "admin"
        self.s=['testtest','test','50']
        self.m= ['newtesttest', 'newtest', '52']
        lg = Login_Page(self.driver)
        lg.open_url(self.url)
        lg.input_name(self.name)
        lg.input_password(self.password)
        lg.get_code()
        lg.input_code()
        lg.sleep(5)
    def test_data(self):

        #测试添加系统权限
        nos=System_Page(self.driver)
        nos.new_sys()
        nos.sleep(5)
        #nos.input_syspms(self.s)
        #nos.sleep(5)
        nos.edit_syspms(self.m)
        nos.sleep(2)
        nos.delete_syspms()




if __name__ == '__main__':
    unittest.main()