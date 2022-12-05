import app


class Open_Account_API:
    def __init__(self):
        self.account_certification_url = app.BASE_URL + '/member/realname/approverealname'  # 实名认证
        self.certification_info_url = app.BASE_URL + '/member/member/getapprove'  # 获取认证信息
        self.open_account_url = app.BASE_URL + '/trust/trust/register'  # 开户
        self.open_account3_url = app.BASE_URL + '/trust/trust/register'  # 开户第三方

    def account_certification(self, resp, parameter, cookie):
        return resp.post(url=self.account_certification_url, params=parameter,
                         cookies=cookie, files={'x': 'y'})

    def account_info(self, resp, cookie):
        return resp.post(url=self.certification_info_url, cookies=cookie, files={'x': 'y'})
