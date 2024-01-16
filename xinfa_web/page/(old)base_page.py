import os
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BasePage(object):
    """
        定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """
    '''--初始化--'''
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    '''--定义open方法--'''
    def open(self, url):
        self.driver.maximize_window()
        self.driver.get(url)

    '''--quit browser and end testing--'''
    def quit_browser(self):
        self.driver.quit()

    '''--浏览器前进操作--'''
    def forward(self):
        self.driver.forward()
        print("Click forward on current page.")

    '''--浏览器后退操作--'''
    def back(self):
        self.driver.back()
        print("Click back on current page.")

    '''--隐式等待--'''
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        print("wait for %d seconds." % seconds)

    '''--点击关闭当前窗口--'''
    def close(self):
        try:
            self.driver.close()
            print("Closing and quit the browser.")
        except NameError as e:
            print("Failed to quit the browser with %s" % e)

    '''--保存图片--'''
    def get_windows_img(self):
        """
            在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹‘.\Screenshots’下
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/Screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            print("Had take screenshot and save to folder : /Screenshots")
        except NameError as e:
            print("Failed to take screenshot! %s" % e)
            self.get_windows_img()

    '''--重写定位元素方法--'''

    def find_element(self, selector):
        """
             这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
             submit_btn = "id=>su"
             login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
             如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
            :param selector:
            :return: element
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element(By.ID,selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.driver.find_element(By.ID,selector_value)
                print("Had find the element \" %s \" successful "
                      "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                print("NoSuchElementException: %s" % e)
                self.get_windows_img()  # take screenshot
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element(By.NAME,selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element(By.CLASS_NAME,selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element(By.LINK_TEXT,selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element(By.PARTIAL_LINK_TEXT,selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element(By.TAG_NAME,selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element(By.XPATH,selector_value)
                print("Had find the element \" %s \" successful "
                      "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                print("NoSuchElementException: %s" % e)
                self.get_windows_img()
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element(By.CSS_SELECTOR,selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")
        return element

    '''--输入--'''
    def input_text(self, selector, text):
        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            print("Had type \" %s \" in inputBox" % text)
        except NameError as e:
            print("Failed to type in input box with %s" % e)
            self.get_windows_img()

    '''--清除文本框--'''
    def clear(self, selector):
        el = self.find_element(selector)
        try:
            el.clear()
            print("Clear text in input box before typing.")
        except NameError as e:
            print("Failed to clear in input box with %s" % e)
            self.get_windows_img()

    '''--点击元素--'''
    def click(self, selector):
        el = self.find_element(selector)
        try:
            el.click()
            print("The element \" %s \" was clicked." % el.text)
        except NameError as e:
            print("Failed to click the element with %s" % e)

    '''--获取网页标题--'''
    def get_page_title(self):
        print("Current page title is %s" % self.driver.title)
        return self.driver.title

    '''--重写send_keys方法--'''
    def send_keys(self, loc, value, clear_first=True, clik_first=True):
        try:
            if clik_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            print("未找到%s" % loc)

    '''--重写跳转iframe方法'''
    def turn_switch_to_iframe(self, iframe="xpath=>//*[@id=\"iframe\"]"):
        element = self.find_element(iframe)
        self.driver.switch_to.frame(element)
        self.sleep(1)
        print("--------------------找到了iframe元素！--------------------")

    '''--切回父级iframe--'''
    def turn_back_iframe(self):
        self.driver.switch_to.default_content()

    """--多选、单选元素获取方法--"""
    def select_by_text(self, selectByText):
        if selectByText is not "":
            select_by_text = self.find_element("xpath=>//*[text()=\"%s\"]" % selectByText)
            select_by_text.click()
        else:
            print("Not find the selectByText, get the default value!")
            pass

    '''--全选输入框中的内容后退格删除--'''
    def delete_by_select_all(self, loc):
        self.find_element(loc).send_keys(Keys.CONTROL + 'a')  # 全选
        self.find_element(loc).send_keys(Keys.BACKSPACE)  # 退格删除

    '''--可以点击页面中没有展示出的元素进行点击操作（需要滑动时使用）--'''
    def click_double_confirm(self, confirmElement):
        confirm_element = self.find_element(confirmElement)
        action = ActionChains(self.driver)
        action.move_to_element(confirm_element)
        action.click_and_hold(confirm_element)
        action.click(confirm_element)
        action.perform()

    '''--静态方法--'''
    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        print("Sleep for %d seconds" % seconds)

