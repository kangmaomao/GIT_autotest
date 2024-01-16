from selenium.common.exceptions import NoSuchElementException
import time
import os, sys
sys.path.append(os.getcwd())
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from xinfa.utils import loggers

# 创建logger实例
log = loggers.Logger.getLogger()

class BasePage(object):

    """测试基类"""
    def __init__(self, driver):
        self.driver = driver
    def find_file_list(self,path):
        names = os.listdir(path)
        return names
    @staticmethod
    def isdisplayed(element):
        """元素是否显示"""
        value = element.is_displayed()
        return value

    @staticmethod
    def sleep(secondes):
        """强制等待"""
        time.sleep(secondes)
        #print('Sleep for %d seconds' % secondes)
        log.info('强制睡眠等待 %d 秒' % secondes)
    def open_url(self,url):
        """输入URL，并最大化显示窗口"""
        self.driver.get(url)
        self.driver.maximize_window()
    def forward(self):
        """浏览器前进"""
        self.driver.forward()
        #print("Click forward on current page.")

        log.info("点击前进到下一个页面")
    def back(self):
        """浏览器后退"""
        self.driver.back()

        # print("Click back on current page.")
        log.info("点击返回上一个页面")
    def wait(self,seconds):
        """隐式等待"""
        self.driver.implicitly_wait(seconds)
        #print("wait for %d seconds." % seconds)
        log.info("隐式等待 %d 秒" % seconds)

    def display_wait(self, selector):
        """显示等待"""
        # self.driver是driver对象，10是最长等待时间，0.5是每0.5秒去查询对应的元素。until后面跟的等待具体条件，EC是判断条件，检查元素是否存在于页面的 DOM 上。
        # WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.ID, "name")))
        by = selector[0]
        value = selector[1]
        element = None
        if by in ['id', 'name', 'class', 'tag', 'link', 'plink', 'css', 'xpath']:
            # noinspection PyBroadException
            try:
                if by == 'id':
                    WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.ID, value)))
                elif by == 'name':
                    WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.NAME, value)))
                elif by == 'class':
                    WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
                elif by == 'tag':
                    WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.TAG_NAME, value)))
                elif by == 'link':
                    WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
                elif by == 'plink':
                    WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, value)))
                elif by == 'css':
                    WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
                elif by == 'xpath':
                    WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, value)))
                else:
                    log.info('没有发现元素')
                log.info("元素等待成功 ,by %s via value :%s " % (by, value))
            except NoSuchElementException as e:
                log.error("没有等待到元素显示 %s " % e)
                self.get_img()  # 调用截图
        else:
            log.info('请输入有效的类型来等待元素')
    def close(self):
        """关闭当前窗口"""
        try:
            self.driver.close()
            #print("Closing and quit the browser.")
            log.info("关闭当前窗口")
        except NameError as e:
            #print("Faile to quit the browser with %s" %e)
            log.error("关闭当前窗口失败 %s" % e)
    def get_img(self):
        """截图"""
        file_path = os.path.dirname(os.path.abspath('D:\\Python\\xinfa\\image\\Screenshots'))+ '\\Screenshots\\'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            #print("Had take screenshot and save to folder : /screenshots")
            log.info("截图并保存到文件夹 : /screenshots")
        except NameError as e:
            #print("Failed to take screenshot! %s" % e)
            log.error("获取截图失败! %s" % e)
            self.get_img()
    def find_element(self, selector):
        """定位元素"""
        by = selector[0]
        value = selector[1]
        element = None
        if by in ['id', 'name', 'class', 'tag', 'link', 'plink', 'css', 'xpath']:
            # noinspection PyBroadException
            try:
                if by == 'id':
                    element = self.driver.find_element(By.ID,value)
                elif by == 'name':
                    element = self.driver.find_element(By.NAME,value)
                elif by == 'class':
                    element = self.driver.find_element(By.CLASS_NAME,value)
                elif by == 'tag':
                    element = self.driver.find_element(By.TAG_NAME,value)
                elif by == 'link':
                    element = self.driver.find_element(By.LINK_TEXT,value)
                elif by == 'plink':
                    element = self.driver.find_element(By.PARTIAL_LINK_TEXT,value)
                elif by == 'css':
                    element = self.driver.find_element(By.CSS_SELECTOR,value)
                elif by == 'xpath':
                    element = self.driver.find_element(By.XPATH,value)
                else:
                    #print('Not find the element')
                    log.info('没有发现定位元素')
                #print("Had  find the element! ,by %s via value :%s " % (by, value))
                log.info("元素定位成功 ,by: %s , value :%s " % (by, value))
                # log.info('元素定位成功。定位方式：%s，使用的值%s：' % (by, value))
                return element
            except NoSuchElementException as e:
                log.error("NoSuchElementException %s " % e)
                self.get_img()  # 调用截图
        else:
            #print('Please enter a valid type of targeting elements')
            log.info('请输入有效的类型来定位元素')

    def find_elements(self, selector):
        """定位一组元素"""
        by = selector[0]
        value = selector[1]
        elements = None
        if by in ['id', 'name', 'class', 'tag', 'link', 'plink', 'css', 'xpath']:
            # noinspection PyBroadException
            try:
                if by == 'id':
                    elements = self.driver.find_elements(By.ID,value)
                elif by == 'name':
                    elements = self.driver.find_elements(By.NAME,value)
                elif by == 'class':
                    elements = self.driver.find_elements(By.CLASS_NAME,value)
                elif by == 'tag':
                    elements = self.driver.find_elements(By.TAG_NAME,value)
                elif by == 'link':
                    elements = self.driver.find_elements(By.LINK_TEXT,value)
                elif by == 'plink':
                    elements = self.driver.find_elements(By.PARTIAL_LINK_TEXT,value)
                elif by == 'css':
                    elements = self.driver.find_elements(By.CSS_SELECTOR,value)
                elif by == 'xpath':
                    elements = self.driver.find_elements(By.XPATH,value)
                else:
                    #print('Not find the element')
                    log.info('没有发现定位元素')
                #print("Had  find the element! ,by %s via value :%s " % (by, value))
                log.info("元素定位成功 ,by %s , value :%s " % (by, value))
                # log.info('元素定位成功。定位方式：%s，使用的值%s：' % (by, value))
                return elements
            except NoSuchElementException as e:
                log.error("NoSuchElementException %s " % e)
                self.get_img()  # 调用截图
        else:
            #print('Please enter a valid type of targeting elements')
            log.info('请输入有效的类型来定位元素')
    def type(self, selector, value):
        """输入内容"""
        element = self.find_element(selector)
        #element.clear()
        #print('clear input_box')
        log.info('清除输入框')
        # noinspection PyBroadException
        try:
            element.send_keys(value)
            #print('input is：%s' % value)
            log.info('输入的值是：%s' % value)
        except BaseException:
            #print('Failed to type in input box')
            log.error('无法在输入框中输入')
            self.get_img()
    def delete(self,selector):
        """删除文本框"""
        element = self.find_element(selector)
        element.send_keys(Keys.CONTROL,'a')
        element.send_keys(Keys.DELETE)
    def type_enter(self,selector,value):
        """输入内容，并按enter确认"""
        try:
            element = self.find_element(selector)
            element.send_keys(value)
            time.sleep(1)
            element.send_keys(Keys.ENTER)
        except Exception as e:
            #print("Failed to type_and_enter with %s" % e)
            log.error("无法在输入框中输入并点击 %s" % e)
            self.get_img()
            raise
    def element_click(self, selector):
        """点击元素"""
        element = self.find_element(selector)
        # noinspection PyBroadException
        try:
            element.click()
            #print('"The element \' %s \' was clicked." % element.text')
            log.info("这个元素%s已经被点击." % element.text)
        except BaseException:
            display = self.isdisplayed(element)
            if display is True:
                self.sleep(3)
                element.click()
                #print('The element was clicked')
                log.info('这个元素已经点击成功')
            else:
                self.get_img()
                #print('Failed to click the element')
                log.error('不能点击此元素')
    def right_click(self,selector):
        """鼠标右击元素"""
        element = self.find_element(selector)
        try:
            ActionChains(self.driver).context_click(element).perform()
           # print("The element \' %s \' was clicked." % element.text)
            log.info("这个元素 %s已经被右键点击.." % element.text)
        except NameError as e:
            #print("Failed to right_click the element with %s" % e)
            log.error("不能右击此元素 %s" % e)
            self.get_img()
    def double_click(self,selector):
        """鼠标双击"""
        element = self.find_element(selector)
        try:
            ActionChains(self.driver).double_click(element).perform()
        except Exception as e:
            #print("Failed to double_click the element with %s" % e)
            log.error("不能双击此元素 %s" % e)
            self.get_img()
            raise
    def move_to_element(self,selector):
        """鼠标移到元素上"""
        try:
            element = self.find_element(selector)
            ActionChains(self.driver).move_to_element(element).perform()
        except Exception as e:
           # print("Failed to move_to_element the element with %s" % e)
            log.error("鼠标移动到此元素上失败 %s" % e)
            self.get_img()
            raise
    def move_to_element_click(self,selector):
        """鼠标移到元素上并点击"""
        try:
            element = self.find_element(selector)
            ActionChains(self.driver).move_to_element(element).click().perform()
        except Exception as e:
            # print("Failed to move_to_element_click the element with %s" % e)
            log.error("鼠标移动到此元素上并点击失败 %s" % e)
            self.get_img()
            raise
    def drag_and_drop(self, element_selector,ta_selector):
        """拖拽"""
        try:
            element_drag = self.find_element(element_selector)
            taget_drop = self.find_element(ta_selector)
            ActionChains(self.driver).drag_and_drop(element_drag,taget_drop).perform()
        except Exception as e:
           # print("Failed to drag_and_drop the element with %s" % e)
            log.error("拖拽此元素失败 %s" % e)
            self.get_img()
            raise
    def refresh(self):
        """刷新"""
        self.driver.refresh()
    def submit_file(self,selector):
        """submit提交"""
        try:
            element = self.find_element(selector)
            element.submit()
        except Exception as e:
           # print("Failed to submit the element with %s" % e)
            log.error("提交此元素的数据失败 %s" % e)
            self.get_img()
    def get_attribute(self,selector,attribute):
        """获取元素属性"""
        try:
            element = self.find_element(selector)
            return element.get_attribute(attribute)
        except Exception as e:
            #print("Failed to get_attribute  with %s" % e)
            log.error("获取元素属性失败 %s" % e)
            self.get_img()
            raise
    def get_text(self,selector):
        """获取元素的文本信息"""
        try:
            return self.find_element(selector).text
        except Exception as e:
            #print("Failed to get_text  with %s" % e)
            log.error("获取文本信息失败 %s" % e)
            self.get_img()

    def getWinMessage(self,selector):
        time.sleep(2)
        msg = self.find_element(selector).text  # 获取网页提示的内容
        log.info("网页提示信息为：" + msg)
        #self.quit()  # 关闭游览器
        return msg

    def dismiss_alert(self):
        """弹窗 alert——取消"""
        self.driver.switch_to.alert.dismiss()

    def accept_alert(self):
        """弹窗 alert——确定"""
        self.driver.switch_to.alert.accept()
    def input_clear(self,selector):
        """清除文本框"""
        element = self.find_element(selector)
        try:
            element.clear()
            #print("Clear text in input box before typing.")
            log.info("在输入数据前清空输入框.")
        except NameError as e:
            #print("Failed to clear in input box with %s" % e)
            log.error("在输入数据前清空输入框失败 %s" % e)
            self.get_img()

    def is_exist(self,selector):
        """元素是否存在"""
        num=self.find_elements(selector)
        if len(num) != 0:
            log.info("元素存在")
            return 1
        else:
            log.error("元素不存在")
            return 0

    def use_js(self, js):
        """调用js"""
        # noinspection PyBroadException
        try:
            self.driver.execute_script(js)
            #print('successful，js contents is：%s' % js)
            log.info('调用js成功：%s' % js)
        except BaseException:
            log.error('js错误')
            #print('js error')
    def switch_menue(self, parentelement, secelement, targetelement):
        """三级菜单切换"""
        self.sleep(3)
        # noinspection PyBroadException
        try:
            self.driver.switch_to_default_content()
            self.element_click(parentelement)
            log.info('成功点击一级菜单：%s' % parentelement)
            self.element_click(secelement)
            log.info('成功点击二级菜单：%s' % secelement)
            self.element_click(targetelement)
            log.info('成功点击三级菜单：%s' % targetelement)
        except BaseException:
            log.error('切换菜单报错')
    def switch_ifarme(self, selector):
        """切换ifarme"""
        element = self.find_element(selector)
        # noinspection PyBroadException
        try:
            self.driver.switch_to.frame(element)
           # print('Successful to switch_to_frame! ')
            log.info('切换到frame成功! ')
        except BaseException:
            #print('Failed to  switch_to_frame')
            log.error('切换到frame失败!')
    def quit_iframe(self):
        """退出当前iframe"""
        self.driver.switch_to_default_content()
    def get_title(self):
        """获取title"""
        title = self.driver.title
        #print('Current page title is:%s' % title)
        log.info('当前页面的title是:%s' % title)
        return title

    def quit(self):
        """关闭浏览器"""
        self.driver.quit()
       # print('quit the browser')
        log.info('关闭浏览器')

    def findFilePath(rootPath, sheet, name):
        """
        查找某个文件夹下的所有文件路径，不论有多少层级的子文件夹
        #rootPath为根文件夹路径
        root, dirs, files文件夹路径, 文件夹名字, 文件名
        """
        rootPath = os.path.join(rootPath, sheet[1:])

        for root, dirs, files in os.walk(rootPath):
            for file in files:
                while name in file:
                    print(file)
                    tu_path = os.path.join(rootPath, file)
                    return tu_path