import unittest

from selenium import webdriver

from xinfa_web.page.dest_top_page import Dest_Top_Page
from xinfa_web.page.login_page import Login_Page


class Test_Modity_Uesrinfo(unittest.TestCase):
    def setUp(self) :
        self.driver=webdriver.Chrome()
        self.url = "http://192.168.11.4:8005/page/bank/user/login"
        self.name='admin'
        self.password='BanK2131'
        self.username = "admin"
    def test_data(self):

        lg = Login_Page(self.driver)
        lg.open_url(self.url)
        lg.input_name(self.name)
        lg.input_password(self.password)
        lg.get_code()
        lg.input_code()
        lg.sleep(5)
        nom=Dest_Top_Page(self.driver)
        #nom.user_info(self.username)
        #测试首页消息
        nom.sleep(2)
        nom.look_all_info()
        nom.view_read()
        nom.sleep(5)
        """ 
        nom.read_info()
        nom.sleep(2)
        nom.delete_info()
        nom.sleep(5)
        nom.read_all_info()
        nom.sleep(5)
        nom.delete_all_info()
        nom.sleep(2)
        """



if __name__ == '__main__':
    unittest.main()