"""
    全局变量名称
"""
import os, logging
from logging import handlers

# 项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 基础URL
BASE_URL = 'http://user-p2p-test.itheima.net'

# 请求头
HEADERS_FROM = 'Content-Type:application/x-www-form-urlencoded'
HEADERS_OpenAccount = "Content-Typemultipart/form-data"



def ini_configLog(defaultfilename="P2PAPIlog"):
    """
    初始化日志系统配置
    :param defaultfilename:
    :return:
    """
    # 1.初始化日志对象
    logger = logging.getLogger()
    # 2.设置日志级别
    logger.setLevel(logging.INFO)
    # 3.创建控制台日志处理器和文件处理器
    sh = logging.StreamHandler()
    filename = BASE_DIR + f"{os.sep}log{os.sep}{defaultfilename}.log"
    fh = logging.handlers.TimedRotatingFileHandler(
        filename,
        when='M',
        interval=5,
        backupCount=3,
        encoding='utf-8'
    )
    # 4.设置日志格式,创建格式化器
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt)

    # 5.将格式化器设置到日志中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

    # 6.将日志处理器添加到日志对象
    logger.addHandler(sh)
    logger.addHandler(fh)

