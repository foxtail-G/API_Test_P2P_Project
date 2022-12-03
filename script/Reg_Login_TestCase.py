"""
    测试类
"""
import random
import unittest, requests, warnings, logging
from api.loginAPI import Login_API
from requests import utils


class RegLoginCase(unittest.TestCase):
    def setUp(self) -> None:
        self.login_api = Login_API()  # 实例化注册登录模块
        self.session = requests.Session()
        self.cookie = None
        warnings.simplefilter("ignore", ResourceWarning)

    def tearDown(self) -> None:
        pass

    def test00_images_code(self):
        """
        获取图⽚验证码，整数参数.获取成功
        :return:
        """
        resp = self.login_api.get_image_code(self.session, str(random.randint(0, 9)))
        self.assertEqual(resp.status_code, 200, "获取图⽚验证码，整数参数 失败")

    def test01_images_code(self):
        """
        获取图⽚验证码，小数参数.获取成功
        :return:
        """
        resp = self.login_api.get_image_code(self.session, str(random.uniform(1, 10)))
        self.assertEqual(resp.status_code, 200, "获取图⽚验证码，小数参数 失败")

    def test02_images_code(self):
        """
        获取图⽚验证码，字母参数.获取失败
        :return:
        """
        resp = self.login_api.get_image_code(self.session, "abacdfo")
        self.assertEqual(resp.status_code, 400, "获取图⽚验证码，字母参数 失败")

    def test01_sms_code(self):
        """
        获取短信验证码成功
        :return:
        """
        data = {
            "phone": 13266707774,
            "imgVerifyCode": 8888,
            "type": "reg"
        }
        # 获取图片验证码,获取cookie
        resp_image = self.login_api.get_image_code(self.session, str(random.randint(0, 9)))
        # requests.utils.dict_from_cookiejar(resp_image.cookies) 将cookie存到字典中
        # 发送获取短信验证码
        resp = self.login_api.get_sms_code(self.session, data, requests.utils.dict_from_cookiejar(resp_image.cookies))
        logging.info(f"获取短信验证码结果:{resp.json()}")

    def test02_sms_code(self):
        """
        获取短信验证码失败-验证码错误
        :return:
        """
        data = {
            "phone": 13266707774,
            "imgVerifyCode": 6666,
            "type": "reg"
        }
        # 获取图片验证码,获取cookie
        resp_image = self.login_api.get_image_code(self.session, str(random.randint(0, 9)))

        # requests.utils.dict_from_cookiejar(resp_image.cookies) 将cookie存到字典中
        # 发送获取短信验证码
        resp = self.login_api.get_sms_code(self.session, data, requests.utils.dict_from_cookiejar(resp_image.cookies))
        self.assertEqual(resp.status_code, 200)  # 断言响应状态码
        self.assertEqual(resp.json()['status'], 100)  # 断言返回代码
        logging.info(f"获取短信验证码失败-验证码错误:{resp.json()}")

    def test03_sms_code(self):
        """
        获取短信验证码失败-手机号错误
        :return:
        """
        data = {
            "phone": 1326670,
            "imgVerifyCode": 8888,
            "type": "reg"
        }
        # 获取图片验证码,获取cookie
        resp_image = self.login_api.get_image_code(self.session, str(random.randint(0, 9)))

        # requests.utils.dict_from_cookiejar(resp_image.cookies) 将cookie存到字典中
        # 发送获取短信验证码
        resp = self.login_api.get_sms_code(self.session, data, requests.utils.dict_from_cookiejar(resp_image.cookies))
        self.assertEqual(resp.status_code, 200)  # 断言响应状态码
        self.assertEqual(resp.json()['status'], 100)  # 断言返回代码
        logging.info(f"获取短信验证码失败-手机号错误:{resp.json()}")

    def test04_sms_code(self):
        """
        获取短信验证码失败-注册类型错误
        :return:
        """
        data = {
            "phone": 13266707774,
            "imgVerifyCode": 8888,
            "type": "xxxxx"
        }
        # 获取图片验证码,获取cookie
        resp_image = self.login_api.get_image_code(self.session, str(random.randint(0, 9)))

        # 发送获取短信验证码
        resp = self.login_api.get_sms_code(self.session, data, requests.utils.dict_from_cookiejar(resp_image.cookies))
        self.assertEqual(resp.status_code, 200)  # 断言响应状态码
        self.assertEqual(resp.json()['status'], 100)  # 断言返回代码
        logging.info(f"获取短信验证码失败-注册类型错误:{resp.json()}")

    def test01_user_reg_success(self):
        """
        注册账号-成功
        :return:
        """
        data = {
            "phone": int("13422222" + str(random.randint(200, 299))),
            "password": "a123456",
            "verifycode": 8888,
            "phone_code": 666666,
            "dy_server": "no"
        }
        # 获取图片验证码,获取cookie
        resp_image = self.login_api.get_image_code(self.session, str(random.randint(0, 9)))
        cookie = requests.utils.dict_from_cookiejar(resp_image.cookies)
        print(cookie)
        # 注册账号
        resp = self.login_api.reg_user(self.session, data, cookie)
        # self.assertEqual(resp.status_code, 200)  # 断言响应状态码
        self.assertEqual(resp.json()['description'], '注册成功')  # 断言返回代码
        logging.info(f"注册账号-成功:{resp.json()}")
