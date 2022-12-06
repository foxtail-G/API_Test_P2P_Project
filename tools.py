"""
    工具类
"""

import json

# 参数化函数-登录注册模块
import app


def readimgverify_code(filename):
    case_data = []  # 最终要返回的列表
    file = app.BASE_DIR + '\\data\\' + filename
    with open(file, encoding='utf-8') as f:
        temp_data = json.load(f)  # 读取json文件
        for item in temp_data['get_img_verify_code']:
            case_data.append((item['type'], item['statusCode']))  # 以元组的方式添加到列表中
    return case_data  # 将列表返回出去


def read_invest_data(filename):
    case_data = []
    file = app.BASE_DIR + "\\data\\" + filename
    with open(file, encoding='utf-8') as f:
        temp_data = json.load(f)
        for item in temp_data['test_investment_data']:
            if item['loan_type'] != "":
                case_data.append((item['loan_type'], item['statuscode']))
            else:
                case_data.append(("", item['statuscode']))
            if item['amount_search'] != "":
                case_data.append((item['loan_type'], item['amount_search'], item['statuscode']))
    return case_data
