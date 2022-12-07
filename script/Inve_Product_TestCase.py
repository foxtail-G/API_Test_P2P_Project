import warnings

import requests, unittest, logging

from api.inveAPI import inve_api
from parameterized import parameterized

from tools import read_data


class Inve_ProductCase(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.Session()
        self.inveapi = inve_api()
        warnings.simplefilter("ignore", ResourceWarning)

    def test01_invest_product_detail_success(self):
        """
        获取投资产品详情-成功
        :return:
        """
        data = {
            "id": 56
        }
        resp = self.inveapi.get_inve_product_detail(self.session, data)
        self.assertEqual(resp.status_code, 200)
        logging.info(f"获取投资产品详情-成功:{resp.json()}")

    def test01_invest_product_query_success(self):
        """
        投资产品查询-成功
        :return:
        """

        resp = self.inveapi.get_inve_product_query(self.session)
        self.assertEqual(resp.status_code, 200)
        logging.info(f"投资产品查询-成功 {resp.json()}")

    @parameterized.expand(read_data("invest_data.json", "test_investment_data", "loan_type,amount_search,statuscode"))
    def test01_get_invest_list(self, loan_type, amount_search, statuscode):
        """
        投资产品
        :param para:
        :return:
        """
        data = {
            "loan_type": loan_type,
            "amount_search": amount_search,
            "statuscode": statuscode
        }
        resp = self.inveapi.get_inve_product_list(self.session,data)
        self.assertEqual(resp.status_code, int(statuscode))
        print(resp.json())

    # def test01_invest_product_list(self):
    #     """
    #     获取 投资产品列表 无参数成功
    #     :return:
    #     """
    #     data = {}
    #
    #     resp = self.inveapi.get_inve_product_list(self.session, data)
    #     self.assertEqual(resp.status_code, 200)
    #     logging.info(f"获取 投资产品列表 无参数成功 {resp.json()}")
    #
    # def test01_invest_product_listall(self):
    #     """
    #     获取产品列表 - 全部标和信用标 - 成功
    #     :return:
    #     """
    #     data = {"loan_type": "1"}
    #
    #     resp = self.inveapi.get_inve_product_list(self.session, data)
        #     self.assertEqual(resp.status_code, 200)
    #     self.assertEqual(resp.json().get('page'), 1)  # 断言返回代码
    #     logging.info(f"获取产品列表 - 全部标和信用标 - 成功 {resp.json()}")
    #
    # def test01_invest_product_list3(self):
    #     """
    #     获取产品列表 - 天标 - 成功
    #     :return:
    #     """
    #     data = {"loan_type": "3"}
    #
    #     resp = self.inveapi.get_inve_product_list(self.session, data)
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertEqual(resp.json().get('page'), 1)  # 断言返回代码
    #     logging.info(f"获取产品列表 - 天标 - 成功 {resp.json()}")
    #
    # def test01_invest_product_list4(self):
    #     """
    #     获取产品列表 - 担保标 - 成功
    #     :return:
    #     """
    #     data = {"loan_type": "4"}
    #
    #     resp = self.inveapi.get_inve_product_list(self.session, data)
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertEqual(resp.json().get('page'), 1)  # 断言返回代码
    #     logging.info(f"获取产品列表 - 担保标 - 成功 {resp.json()}")
    #
    # def test01_invest_product_list5(self):
    #     """
    #     获取产品列表 - 抵押标 - 成功
    #     :return:
    #     """
    #     data = {"loan_type": "5"}
    #
    #     resp = self.inveapi.get_inve_product_list(self.session, data)
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertEqual(resp.json().get('page'), 1)  # 断言返回代码
    #     logging.info(f"获取产品列表 - 抵押标 - 成功 {resp.json()}")
    #
    # def test01_invest_product_list6(self):
    #     """
    #     获取产品列表 - 流转标 - 成功
    #     :return:
    #     """
    #     data = {"loan_type": "6"}
    #
    #     resp = self.inveapi.get_inve_product_list(self.session, data)
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertEqual(resp.json().get('page'), 1)  # 断言返回代码
    #     logging.info(f"获取产品列表 - 流转标 - 成功 {resp.json()}")
    #
    # def test01_invest_product_price_0_2000(self):
    #     """
    #     成功获取产品列表 - 金额0-2000元
    #     :return:
    #     """
    #     data = {"loan_type": "1", "amount_search": "0-2000"}
    #
    #     resp = self.inveapi.get_inve_product_list(self.session, data)
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertEqual(resp.json().get('page'), 1)  # 断言返回代码
    #     logging.info(f"成功获取产品列表 - 金额0-2000元 {resp.json()}")
    #
    # def test01_invest_product_price_2000_5000(self):
    #     """
    #     成功获取产品列表 - 金额2000-5000元
    #     :return:
    #     """
    #     data = {"loan_type": "1", "amount_search": "2000-5000"}
    #
    #     resp = self.inveapi.get_inve_product_list(self.session, data)
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertEqual(resp.json().get('page'), 1)  # 断言返回代码
    #     logging.info(f"成功获取产品列表 - 金额2000-5000元 {resp.json()}")

    def test01_invest_data(self):
        """
        成功投资数据
        :return:
        """
        data = {"id": "1000", "depositCertificate": -1, "amount": 1000}

        resp = self.inveapi.get_inve_data(self.session, data)
        self.assertEqual(resp.status_code, 200)
        print(resp.json())
        # self.assertEqual(resp.json().get('page'), 1)  # 断言返回代码
        logging.info(f"成功投资数据 {resp.json()}")
