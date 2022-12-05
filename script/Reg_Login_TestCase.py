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

    def test01_RegUser__success(self):
        """
        注册账号-成功
        :return:
        """
        phone = int("13422222" + str(random.randint(200, 299)))

        # 获取图片验证码,获取cookie
        resp_image = self.login_api.get_image_code(self.session, str(random.randint(0, 9)))
        cookie = requests.utils.dict_from_cookiejar(resp_image.cookies)

        # 获取短信验证码
        data = {
            "phone": phone,
            "imgVerifyCode": 8888,
            "type": "reg"
        }
        resp_sms = self.login_api.get_sms_code(self.session, data, cookie)

        # 注册账号
        data = {
            "phone": phone,
            "password": "a123456",
            "verifycode": 8888,
            "phone_code": 666666,
            "dy_server": "no"
        }
        resp = self.login_api.register_user(self.session, data, cookie)
        self.assertEqual(resp.status_code, 200)  # 断言响应状态码
        self.assertEqual(resp.json()['description'], '注册成功')  # 断言返回代码
        logging.info(f"注册账号-成功:{resp.json()}")

    def test02_RegUser_ImgCodeError(self):
        """
        注册账号失败--图⽚验证码错误
        :return:
        """
        phone = int("13422222" + str(random.randint(200, 299)))

        # 获取图片验证码,获取cookie
        resp_image = self.login_api.get_image_code(self.session, str(random.randint(0, 9)))
        cookie = requests.utils.dict_from_cookiejar(resp_image.cookies)

        # 获取短信验证码
        data = {
            "phone": phone,
            "imgVerifyCode": 1111,
            "type": "reg"
        }
        resp_sms = self.login_api.get_sms_code(self.session, data, cookie)

        # 注册账号
        data = {
            "phone": phone,
            "password": "a123456",
            "verifycode": 1111,
            "phone_code": 666666,
            "dy_server": "no"
        }
        resp = self.login_api.register_user(self.session, data, cookie)
        self.assertEqual(resp.status_code, 200)  # 断言响应状态码
        self.assertEqual(resp.json()['description'], '验证码错误!')  # 断言返回代码
        logging.info(f"注册账号失败--图⽚验证码错误:{resp.json()}")

    def test03_RegUser_SMSCodeError(self):
        """
        注册账号失败--短信验证码错误
        :return:
        """
        phone = int("13422222" + str(random.randint(200, 299)))

        # 获取图片验证码,获取cookie
        resp_image = self.login_api.get_image_code(self.session, str(random.randint(0, 9)))
        cookie = requests.utils.dict_from_cookiejar(resp_image.cookies)

        # 获取短信验证码
        data = {
            "phone": phone,
            "imgVerifyCode": 6666,
            "type": "reg"
        }
        resp_sms = self.login_api.get_sms_code(self.session, data, cookie)

        # 注册账号
        data = {
            "phone": phone,
            "password": "a123456",
            "verifycode": 6666,
            "phone_code": 33333,
            "dy_server": "no"
        }
        resp = self.login_api.register_user(self.session, data, cookie)
        self.assertEqual(resp.status_code, 200)  # 断言响应状态码
        self.assertEqual(resp.json()['description'], '验证码错误!')  # 断言返回代码
        logging.info(f"注册账号失败--短信验证码错误:{resp.json()}")

    def test04_RegUser_SMSCodeError(self):
        """
        注册账号失败--⼿机已存在
        :return:
        """
        phone = 13266707774  # 存在的手机号

        # 获取图片验证码,获取cookie
        resp_image = self.login_api.get_image_code(self.session, str(random.randint(0, 9)))
        cookie = requests.utils.dict_from_cookiejar(resp_image.cookies)

        # 获取短信验证码
        data = {
            "phone": phone,
            "imgVerifyCode": 8888,
            "type": "reg"
        }
        resp_sms = self.login_api.get_sms_code(self.session, data, cookie)

        # 注册账号
        data = {
            "phone": phone,
            "password": "a123456",
            "verifycode": 8888,
            "phone_code": 666666,
            "dy_server": "no"
        }
        resp = self.login_api.register_user(self.session, data, cookie)
        self.assertEqual(resp.status_code, 200)  # 断言响应状态码
        self.assertEqual(resp.json()['description'], '手机已存在!')  # 断言返回代码
        logging.info(f"注册账号失败--⼿机已存在:{resp.json()}")

    def test05_RegUser_PwdNotNull(self):
        """
        注册账号失败--密码不能为空
        :return:
        """
        phone = int("13422222" + str(random.randint(200, 299)))

        # 获取图片验证码,获取cookie
        resp_image = self.login_api.get_image_code(self.session, str(random.randint(0, 9)))
        cookie = requests.utils.dict_from_cookiejar(resp_image.cookies)

        # 获取短信验证码
        data = {
            "phone": phone,
            "imgVerifyCode": 8888,
            "type": "reg"
        }
        resp_sms = self.login_api.get_sms_code(self.session, data, cookie)

        # 注册账号
        data = {
            "phone": phone,
            "password": None,
            "verifycode": 8888,
            "phone_code": 666666,
            "dy_server": "no"
        }
        resp = self.login_api.register_user(self.session, data, cookie)
        self.assertEqual(resp.status_code, 200)  # 断言响应状态码
        self.assertEqual(resp.json()['description'], '密码不能为空')  # 断言返回代码
        logging.info(f"注册账号失败--密码不能为空:{resp.json()}")

    def test06_RegUser_NotTerms(self):
        """
        注册账号失败--不同意条款
        :return:
        """
        phone = int("13422222" + str(random.randint(200, 299)))

        # 获取图片验证码,获取cookie
        resp_image = self.login_api.get_image_code(self.session, str(random.randint(0, 9)))
        cookie = requests.utils.dict_from_cookiejar(resp_image.cookies)

        # 获取短信验证码
        data = {
            "phone": phone,
            "imgVerifyCode": 8888,
            "type": "reg"
        }
        resp_sms = self.login_api.get_sms_code(self.session, data, cookie)

        # 注册账号
        data = {
            "phone": phone,
            "password": "a123456",
            "verifycode": 8888,
            "phone_code": 666666,
            "dy_server": "off"
        }
        resp = self.login_api.register_user(self.session, data, cookie)
        self.assertEqual(resp.status_code, 200)  # 断言响应状态码
        self.assertEqual(resp.json()['description'], '请同意我们的条款')  # 断言返回代码
        logging.info(f"注册账号失败--不同意条款:{resp.json()}")

    def test01_RegUser_login_success(self):
        """
        登录账号成功
        :return:
        """
        data = {
            "keywords": 13266707774,
            "password": "123456a"
        }
        resp = self.login_api.login_user_info(self.session, data)
        self.assertEqual(resp.status_code, 200)  # 断言响应状态码
        self.assertEqual(resp.json()['description'], '登录成功')  # 断言返回代码
        logging.info(f"登录账号成功:{resp.json()}")

    def test02_RegUser_login_UserNotExist(self):
        """
        登录账号-用户不存在
        :return:
        """
        data = {
            "keywords": 133222,
            "password": "123456a"
        }
        resp = self.login_api.login_user_info(self.session, data)
        self.assertEqual(resp.status_code, 200)  # 断言响应状态码
        self.assertEqual(resp.json()['description'], '用户不存在')  # 断言返回代码
        logging.info(f"登录账号-用户不存在:{resp.json()}")

    def test03_RegUser_login_PwdNotnull(self):
        """
        登录账号-密码不能为空
        :return:
        """
        data = {
            "keywords": 13266707774,
            "password": None,
        }
        resp = self.login_api.login_user_info(self.session, data)
        self.assertEqual(resp.status_code, 200)  # 断言响应状态码
        self.assertEqual(resp.json()['description'], '密码不能为空')  # 断言返回代码
        logging.info(f"登录账号-密码不能为空:{resp.json()}")

    def test04_RegUser_login_PwdNotnull(self):
        """
        登录账号-密码错误1次
        :return:
        """
        data = {
            "keywords": 13266707774,
            "password": "bbbb",
        }
        resp = self.login_api.login_user_info(self.session, data)
        self.assertEqual(resp.status_code, 200)  # 断言响应状态码
        self.assertEqual(resp.json()['description'], '密码错误1次,达到3次将锁定账户')  # 断言返回代码
        logging.info(f"登录账号-密码错误1次:{resp.json()}")

    def test05_RegUser_login_PwdNotnull(self):
        """
        登录账号-密码错误2次
        :return:
        """
        data = {
            "keywords": 13266707774,
            "password": "bbbb",
        }
        resp = self.login_api.login_user_info(self.session, data)
        self.assertEqual(resp.status_code, 200)  # 断言响应状态码
        self.assertEqual(resp.json()['description'], '密码错误2次,达到3次将锁定账户')  # 断言返回代码
        logging.info(f"登录账号-密码错误2次:{resp.json()}")

    def test06_RegUser_login_PwdError3(self):
        """
        登录账号-连续执行密码错误3次
        :return:
        """
        data = {
            "keywords": 13266707774,
            "password": "bbbb",
        }
        resp = ''
        for i in range(3):
            resp = self.login_api.login_user_info(self.session, data)
        self.assertEqual(resp.status_code, 200)  # 断言响应状态码
        self.assertEqual(resp.json().get('description'), "由于连续输入错误密码达到上限，账号已被锁定，请于1.0分钟后重新登录")  # 断言返回代码
        logging.info(f"登录账号-连续执行密码错误3次:{resp.json()}")

    def test07_RegUser_login_isLogin(self):
        """
        是否登录检查-登录成功
        :return:
        """
        data = {
            "keywords": 13266707774,
            "password": "123456a"
        }
        resp_login = self.login_api.login_user_info(self.session, data)

        resp = self.login_api.login_user_islogin(self.session, data,
                                                 requests.utils.dict_from_cookiejar(resp_login.cookies))
        self.assertEqual(resp.status_code, 200)  # 断言响应状态码
        self.assertEqual(resp.json().get('description'), "OK")  # 断言返回代码
        logging.info(f"是否登录检查-登录成功:{resp.json()}")

    def test08_RegUser_login_NotLogin(self):
        """
        是否登录检查-未登录
        :return:
        """
        data = {
            "keywords": 13266707774,
            "password": "123"
        }

        resp = self.login_api.login_user_islogin(self.session, data)
        self.assertEqual(resp.status_code, 200)  # 断言响应状态码
        self.assertEqual(resp.json().get('description'), "您未登陆！")  # 断言返回代码
        logging.info(f"是否登录检查-未登录:{resp.json()}")
