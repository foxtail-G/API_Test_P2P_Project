"""
    登录注册模块
"""
import app


class Login_API:
    def __init__(self):
        self.get_image_code_URL = app.BASE_URL + '/common/public/verifycode1/'  # 获取图⽚验证码
        self.get_sms_code_URL = app.BASE_URL + '/member/public/sendSms/'  # 获取短信验证码
        self.reg_user = app.BASE_URL + '/member/public/reg'  # 注册用户
        self.login_user = app.BASE_URL + '/member/public/login'  # 登录账号
        self.login_islogin = app.BASE_URL + '/member/public/islogin'  # 是否登录成功

    def get_image_code(self, resp, parameter):
        """
        获取图⽚验证码
        :return:
        """
        return resp.get(url=self.get_image_code_URL + parameter)

    def get_sms_code(self, resp, parameter, cookie):
        """
        获取短信验证码
        :return:
        """
        return resp.post(url=self.get_sms_code_URL, params=parameter, cookies=cookie)

    def register_user(self, resp, parameter, cookie):
        """
        注册账号
        :return:
        """
        return resp.post(url=self.reg_user, params=parameter, cookies=cookie)

    def login_user_info(self, resp, parameter):
        """
        登录账号
        :return:
        """
        return resp.post(url=self.login_user, params=parameter)

    def login_user_islogin(self, resp, parameter, cookie):
        """
        是否登录成功
        :return:
        """
        return resp.post(url=self.login_islogin, params=parameter, cookies=cookie)
