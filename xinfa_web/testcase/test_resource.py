import unittest
from parameterized import parameterized
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from xinfa_web.page.login_page import Login_Page
from xinfa_web.page.resource_page import Resource_Page


class Test_Resource(unittest.TestCase):
    def setUp(self) :
        service = Service(executable_path='D:\\Python\\xinfa\\driver\\chromedriver.exe')
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service,options=options)
        self.url = "http://192.168.11.4:8005/page/bank/user/login"

        self.s ='D:\\Python\\xinfa\\image\\Screenshots'
        self.sr="待审核"
        self.tr="PDF"
        self.da="2023-09-19"
        self.da2="2023-09-25"
        self.number=2
    @parameterized.expand([('admin','BanK2131')])
    def test_data(self,name,password):
        lg = Login_Page(self.driver)
        lg.open_url(self.url)
        lg.login(name,password)
        #print('name={} password={} expected={}'.format(name, password, expected))
        lg.sleep(5)
        # #上传素材
        # nos=Resource_Page(self.driver)
        # nos.new_res()
        # nos.sleep(5)
        # # nos.res_update_file(self.s)
        # nos.res_find_auditing(self.sr)
        # nos.sleep(5)
        # nos.res_find_filetype(self.tr)
        # nos.sleep(5)
        #发布素材
        nos=Resource_Page(self.driver)
        nos.new_res()
        nos.sleep(5)
        nos.res_release_file()
        nos.sleep(5)
        nos.res_play_model()
        # nos.res_setup_playtime()
        # nos.res_playtime_data(self.da,self.da2)
        # nos.sleep(2)
        # nos.res_play_button()
        # nos.sleep(2)
        # nos.res_play_floder()
        # nos.res_play_class()
        # nos.res_play_view()
        # nos.res_play_device_random(self.number)
        nos.sleep(20)



if __name__ == '__main__':
    unittest.main()