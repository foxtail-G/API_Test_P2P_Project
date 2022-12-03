"""
    测试类
"""
import unittest, requests, logging, warnings
from api.loginAPI import Login_API


class RegLoginCase(unittest.TestCase):
    def setUp(self) -> None:
        self.login_api = Login_API()  # 实例化注册登录模块
        self.session = requests.Session()
        warnings.simplefilter("ignore", ResourceWarning)

    def tearDown(self) -> None:
        pass

    def test00_images_code(self):
        """
        获取图⽚验证码，整数参数
        :return:
        """
        resp = self.login_api.get_image_code(self.session, "1")
        self.assertEqual(resp.status_code, 200)

    def test01_images_code(self):
        """
        获取图⽚验证码，小数参数
        :return:
        """
        pass

    def test02_images_code(self):
        """
        获取图⽚验证码，字母参数
        :return:
        """
        pass
