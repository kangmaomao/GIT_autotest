import unittest
from parameterized import parameterized
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from xinfa.page.login_page import Login_Page
from xinfa.page.program_page import Program_Page


class Test_Resource(unittest.TestCase):
    def setUp(self) :
        service = Service(executable_path='D:\\Python\\xinfa\\driver\\chromedriver.exe')
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service,options=options)
        self.url = "http://192.168.11.4:8005/page/bank/user/login"
        self.n=5
        self.s1="test922"
        self.s2="节目D"
        self.ss="202309071724.png"
    @parameterized.expand([('admin','BanK2131')])
    def test_data(self,name,password):
        lg = Login_Page(self.driver)
        lg.open_url(self.url)
        lg.login(name,password)
        lg.sleep(5)
        nop = Program_Page(self.driver)
        nop.new_pro()
        #复制节目
        # nop.pro_copy_file(self.n,self.s1,self.s2)
        #审核节目
        # nop.pro_check_page()
        # nop.sleep(2)
        # nop.pro_check_view(self.n)
        # nop.sleep(20)
        #发布历史
        # nop.pro_history_page()
        # nop.sleep(2)
        # nop.pro_history_reback(self.ss)
        # nop.sleep(10)
        nop.pro_all_program_cancel()
        nop.pro_chose_file(self.n)





if __name__ == '__main__':
    unittest.main()