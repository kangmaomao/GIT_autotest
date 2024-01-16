import logging
from logging.handlers import TimedRotatingFileHandler


class MyLogger(object):

    @staticmethod
    def create_logger():
        my_logger = logging.getLogger("my_logger")
        my_logger.setLevel("DEBUG")
        # 控制台处理器
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel("INFO")
        my_logger.addHandler(stream_handler)
        # 使用时间滚动的文件处理器
        log_file_handler = TimedRotatingFileHandler(filename='log.log', when='D', interval=1, backupCount=10)
        log_file_handler.setLevel("INFO")
        my_logger.addHandler(log_file_handler)

        formatter = logging.Formatter('%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s')
        stream_handler.setFormatter(formatter)
        log_file_handler.setFormatter(formatter)

        return my_logger