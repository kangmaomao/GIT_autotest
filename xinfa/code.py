import pytesseract
from PIL import Image, ImageEnhance
from page_object.page.basePage import BasePage
from page_object.utils.functions import Functions as Fun
from page_object.locator.loginPageLoc import LoginPageLoc as Loc


class GetCode(BasePage):

    def remove(self,string):
        """字符串去除空格或换行"""

        str = string.replace(" ", "")
        str = str.replace("", "")
        str = str.replace('\n', "")
        return str

    def getCodeImg(self):
        """获取验证码"""

        # 步骤①：
        basePath = Fun().upPath() + "/utils/img/"
        imgPath = basePath + "code.png"
        savePath = basePath + "saveCode.png"
        # 定位图片元素
        imgElement = self.webDriverWait(Loc.codeImg_loc)
        # 点击验证码图片
        imgElement.element_click()
        # print(f"点击【{next(iter(Fun()))}】次验证码图片")
        # 截取当前页面的图并放到目录里
        self.driver.save_screenshot(imgPath)

        # 步骤②：
        # 获取验证码x,y轴，x&y代表左上角的坐标点
        imgLocation = imgElement.location
        print(f"图片坐标点：{imgLocation}")
        # 获取验证码长、宽
        imgSize = imgElement.size
        print(f"图片长、宽：{imgSize}")
        # 获取浏览器的长、宽
        windowSize = self.driver.get_window_size()
        print(f"浏览器长、宽：{windowSize}")
        # 打开截图
        openImg = Image.open(imgPath)
        # 获取保存截图的长、宽(宽：2700, 高：1950)
        screenImgSize = openImg.size
        print(f"保存截图的长、宽：{screenImgSize}")

        # 步骤③：截取截图的验证码图片
        # 图片左边距占据整个浏览器的百分比
        left = imgLocation['x']/windowSize['width']
        # 图片上边距占据整个浏览器的百分比
        top = imgLocation['y']/windowSize['height']
        # 图片右边距占据整个浏览器的百分比
        right = (imgLocation['x'] + imgSize['width'])/windowSize['width']
        # 图片下边距占据整个浏览器的百分比
        bottom = (imgLocation['y'] + imgSize['height'])/windowSize['height']

        # 需要截取的坐标
        screenLocation = (
            left * screenImgSize[0],
            top * screenImgSize[1]+150,
            right * screenImgSize[0],
            bottom * screenImgSize[1]+150
        )
        # 打开截图并截取区域并保存
        img = openImg.crop(screenLocation)
        img = img.convert('L')  # 转换模式：L | RGB

        # enhancer = ImageEnhance.Color(img)
        # enhancer = enhancer.enhance(0)
        # enhancer = ImageEnhance.Brightness(enhancer)
        # enhancer = enhancer.enhance(2)
        # enhancer = ImageEnhance.Contrast(enhancer)      # 增强对比度
        # enhancer = enhancer.enhance(8)
        # enhancer = ImageEnhance.Sharpness(enhancer)
        # img = enhancer.enhance(20)

        img = ImageEnhance.Contrast(img)  # 增强对比度
        img = img.enhance(2.0)
        img.save(savePath)

        # 步骤④：获得code验证码
        code = pytesseract.image_to_string(img).strip()
        print(f"提取的验证码为：【{self.remove(code)}】")
        return self.remove(code)


    def getCode(self):
        """获取4位数验证码"""

        # 循环前获取code字数
        code = self.getCodeImg()
        print(f"验证码位数：【{len(code)}】位")
        while len(code) != 4:
            # 重新获取验证码
            code = self.getCodeImg()
            print(f"验证码位数：【{len(code)}】位")
            if len(code) != 4:
                print("验证码不是4位数！")
        print(f"输出4位验证码为：{code}")
        return code


    def checkCode(self):
        """判断验证码是否正确"""

        try:
            errorMsg = self.get_text(Loc.errorMsg_loc)
            if errorMsg == "验证码错误":
                self.inputCodeAction()
        except:
            print("验证码正确，进入首页！")


    def inputCodeAction(self):
        """输入验证码登录"""

        code = self.getCode()
        self.el_clear_sendKeys(Loc.code_loc, code)
        self.el_click(Loc.loginButton_loc)
        self.checkCode()