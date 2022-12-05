import app


class inve_api:
    def __init__(self):
        self.inve_ProductDetail_url = app.BASE_URL + '/common/loan/loaninfo'  # 获取投资产品详情
        self.inve_Product_query_url = app.BASE_URL + '/loan/loan/loansearch'  # 投资产品查询
        self.inve_Product_list_url = app.BASE_URL + '/loan/loan/listtender'  # 投资产品列表
        self.inve_Product_inveData_url = app.BASE_URL + '/loan/tender/investdata'  # 投资数据

    def get_inve_product_detail(self, resp, parameter):
        return resp.post(url=self.inve_ProductDetail_url, params=parameter)

    def get_inve_product_query(self, resp):
        return resp.post(url=self.inve_Product_query_url)

    def get_inve_product_list(self, resp, parameter):
        return resp.post(url=self.inve_Product_list_url, params=parameter)

    def get_inve_data(self, resp, parameter):
        return resp.post(url=self.inve_Product_inveData_url, params=parameter)
