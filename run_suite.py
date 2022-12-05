import unittest, app
from script.Open_Account_TestCase import OpenAccountCase
from script.Inve_Product_TestCase import Inve_ProductCase
from script.Reg_Login_TestCase import RegLoginCase
from BeautifulReport import BeautifulReport
# 创建测试套件
suite = unittest.TestSuite()

# 将测试用例代码添加到测试套件中
suite.addTest(unittest.makeSuite(OpenAccountCase))
suite.addTest(unittest.makeSuite(Inve_ProductCase))
suite.addTest(unittest.makeSuite(RegLoginCase))


# 定义测试报告路径
reportFile = "./report/mini_report.html"

# 运行测试套件
runner =BeautifulReport(suite)
runner.report(description='P2P金融项目',filename=reportFile)





