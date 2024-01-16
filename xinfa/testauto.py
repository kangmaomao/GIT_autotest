import pywinauto.application
from pywinauto.application import Application
path =r"D:\文件\岫岩农商行\岫岩互动桌面\start.exe"
app = Application(backend="uia") #实例化
app.start(path)   #启动程序
app.connect(path)