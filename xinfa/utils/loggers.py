import logging
import time
import os


class Logger(object):
    @staticmethod
    def getLogger():
        # 创建一个记器
        logs = logging.getLogger("file_logs")
        logs.handlers.clear()
        # 设置日志级别为level，只有日志级别大于level的日志才会输出。DEBUG<INFO<WARING<ERROR<CRITICAL
        logs.setLevel("INFO")
        # 创建formatter
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s ")
        # 创建屏幕输出到控制台
        streamHandler = logging.StreamHandler()
        # 设置日志输出级别
        streamHandler.setLevel("DEBUG")
        # 创建log文件，设置输出等级
        # 根目录
        PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # log文件命名：xxxx_xxxx_xx.log
        time_now = time.strftime('%Y_%m%d_%H', time.localtime()) + '.log'
        fileHandler = logging.FileHandler(os.path.join(PROJECT_ROOT, "D:\\Python\\xinfa\\logs", time_now), 'a', encoding='utf-8')
        # 设置日志输出级别
        fileHandler.setLevel("DEBUG")
        # 用formatter渲染这两个Handler
        streamHandler.setFormatter(formatter)
        fileHandler.setFormatter(formatter)
        # 将这两个Handler加入logger内
        logs.addHandler(streamHandler)
        logs.addHandler(fileHandler)

        return logs
