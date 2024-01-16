import unittest

from ddt import ddt
from parameterized import parameterized
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from xinfa_web.page.login_page import Login_Page
from xinfa_web.utils import read_file


@ddt
class Test_Login(unittest.TestCase):
    def setUp(self):
        service = Service(executable_path='D:\\Python\\xinfa\\driver\\chromedriver.exe')
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service,options=options)
        self.url = "http://192.168.11.4:8005/page/bank/user/login"
    path = "D:\\Python\\xinfa\\testdata\\test.xls"
    data = read_file.Read_file.read_excel_rows(path)
    @parameterized.expand(*data)
    def test_login(self, url,name, password):
        lg = Login_Page(self.driver)
        lg.open_url(url)
        lg.login(name, password)
        lg.sleep(1)


    def tearDown(self):
        self.driver.quit()


# if __name__ == '__main__':
#     unittest.main()
