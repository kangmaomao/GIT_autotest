import unittest

from parameterized import parameterized
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from utils import read_file
from xinfa.page.login_page import Login_Page


class Test_Login(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path='D:\\Python\\xinfa\\driver\\chromedriver.exe')
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service,options=options)
    path = "D:\\Python\\xinfa\\testdata\\test.xls"
    data=read_file.Read_file.read_excel_rows(path)
    @parameterized.expand(data)
    def test_login(self, url,name, password):
        lg = Login_Page(self.driver)
        lg.open_url(url)
        lg.login(name, password)
        lg.sleep(1)

    def tearDown(self):
        self.driver.quit()


# if __name__ == '__main__':
#     unittest.main()
