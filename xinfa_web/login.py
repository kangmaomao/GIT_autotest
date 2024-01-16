import ddddocr as ddddocr

from selenium import webdriver

import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#打开浏览器输入url
url = "http://sx.mzydz.com/page/adpublish/login"
service = Service(executable_path='D:\\Python\\xinfa\\driver\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get(url)
time.sleep(2)
#定位账号
name = driver.find_element(by=By.ID,value='userName')
#定位密码
password = driver.find_element(by=By.ID,value='password')
#定位登录按钮
login = driver.find_element(by=By.XPATH,value='//*[@id="userNameLoginDiv"]/form/button')
#输入账号
name.clear()
name.send_keys("13526821875")
#输入密码
password.clear()
password.send_keys("kang@986786192")

#验证码处理-使用OCR自动识别
driver.maximize_window()
yzm=driver.find_element(by=By.XPATH,value='//*[@class="ant-form-item-control"]/span/div/div[2]/img')
yzm.screenshot('D:\\Python\\xinfa\\image\\a.png')
ocr = ddddocr.DdddOcr()
with open("D:\\Python\\xinfa\\image\\a.png","rb") as fp:
    image=fp.read()
catch = ocr.classification(image)
#使用image_to_string识别验证码并输入验证码
driver.find_element(by=By.ID,value='code').send_keys(catch)
time.sleep(2)
login.click()
time.sleep(2)


#发布节目
driver.find_element(by=By.XPATH,value='//*[@class="side-menu-1yx2u"]/ul/li[4]/a').click()
time.sleep(2)
# element = driver.find_element(by=By.XPATH,value='//*[@class="text-my-3qpbA"]/div[1]')
element = driver.find_element(by=By.XPATH,value='//*[@id="programBox8227"]')
ActionChains(driver).move_to_element(element).perform()
driver.find_element(by=By.XPATH,value='//*[@id="programBox8227"]/div[1]/div/div[2]/div[1]/div').click()
time.sleep(2)
driver.find_element(by=By.XPATH,value='//*[@class="ant-table-tbody"]/tr/td/span/label/span/input').click()
time.sleep(2)
driver.find_element(by=By.XPATH,value='//*[@class="ant-modal-footer"]/div/button[2]').click()
time.sleep(3600)
while True:
    #删除节目
    driver.find_element(by=By.XPATH,value='//*[@class="ant-tabs-nav ant-tabs-nav-animated"]/div/div[3]').click()
    time.sleep(2)
    driver.find_element(by=By.XPATH,value='//*[@class="ant-table-tbody"]/tr/td[9]/div/button[2]').click()
    time.sleep(2)
    driver.find_element(by=By.XPATH,value='//*[@class="ant-btn ant-btn-primary ant-btn-sm"]').click()
    time.sleep(5)
    #发布节目
    driver.find_element(by=By.XPATH,value='//*[@class="ant-tabs-nav ant-tabs-nav-animated"]/div/div[1]').click()
    time.sleep(2)
    # element = driver.find_element(by=By.XPATH,value='//*[@class="text-my-3qpbA"]/div[1]')
    element = driver.find_element(by=By.XPATH,value='//*[@id="programBox8227"]')
    ActionChains(driver).move_to_element(element).perform()
    driver.find_element(by=By.XPATH,value='//*[@id="programBox8227"]/div[1]/div/div[2]/div[1]/div').click()
    time.sleep(2)
    driver.find_element(by=By.XPATH,value='//*[@class="ant-table-tbody"]/tr/td/span/label/span/input').click()
    time.sleep(2)
    driver.find_element(by=By.XPATH,value='//*[@class="ant-modal-footer"]/div/button[2]').click()
    time.sleep(3600)



