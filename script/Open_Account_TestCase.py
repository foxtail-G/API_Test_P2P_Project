"""
    开通测试模块测试类
"""
import unittest, requests, warnings, logging

from requests import utils
from api.loginAPI import Login_API
from api.openAccountAPI import Open_Account_API


class OpenAccountCase(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.Session()
        self.openacc = Open_Account_API()
        self.login_api = Login_API()
        warnings.simplefilter("ignore", ResourceWarning)

    def test01_account_certification(self):
        """
        实名认证-成功
        :return:
        """
        # 登录账号
        data = {
            "keywords": 13266707774,
            "password": "123456a"
        }
        resp_login = self.login_api.login_user_info(self.session, data)

        data = {
            "realname": "李欣欣",
            "card_id": 372522196209260937,
        }
        resp = self.openacc.account_certification(self.session, data,
                                                  requests.utils.dict_from_cookiejar(resp_login.cookies))

        # 断言
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json().get('description'), "提交成功!")  # 断言返回代码
        logging.info(f"实名认证-成功:{resp.json()}")

    def test02_account_certification_nameNotNull(self):
        """
        实名认证-姓名不能为空
        :return:
        """
        # 登录账号
        data = {
            "keywords": 13266707774,
            "password": "123456a"
        }
        resp_login = self.login_api.login_user_info(self.session, data)

        data = {
            "realname": None,
            "card_id": 372522196209260937,
        }
        resp = self.openacc.account_certification(self.session, data,
                                                  requests.utils.dict_from_cookiejar(resp_login.cookies))

        # 断言
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json().get('description'), "姓名不能为空!")  # 断言返回代码
        logging.info(f"实名认证-姓名不能为空:{resp.json()}")

    def test03_account_certification_CaridNotNull(self):
        """
        实名认证-身份证号不能为空
        :return:
        """
        # 登录账号
        data = {
            "keywords": 13266707774,
            "password": "123456a"
        }
        resp_login = self.login_api.login_user_info(self.session, data)

        data = {
            "realname": "张三",
            "card_id": None,
        }
        resp = self.openacc.account_certification(self.session, data,
                                                  requests.utils.dict_from_cookiejar(resp_login.cookies))

        # 断言
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json().get('description'), "姓名不能为空!")  # 断言返回代码
        logging.info(f"实名认证-身份证号不能为空:{resp.json()}")

    def test01_get_certificationInfo(self):
        """
        获取认证信息-成功
        :return:
        """
        # 登录账号
        data = {
            "keywords": 13266707774,
            "password": "123456a"
        }
        resp_login = self.login_api.login_user_info(self.session, data)

        resp = self.openacc.account_info(self.session,
                                         requests.utils.dict_from_cookiejar(resp_login.cookies))

        # 断言
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json().get('realname_status'), "1")  # 断言返回代码
        logging.info(f"获取认证信息-成功:{resp.json()}")
