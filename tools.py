"""
    工具类
"""

import json

# 参数化函数-登录注册模块
import app


# def readimgverify_code(filename):
#     case_data = []  # 最终要返回的列表
#     file = app.BASE_DIR + '\\data\\' + filename
#     with open(file, encoding='utf-8') as f:
#         temp_data = json.load(f)  # 读取json文件
#         for item in temp_data['get_img_verify_code']:
#             case_data.append((item['type'], item['statusCode']))  # 以元组的方式添加到列表中
#     return case_data  # 将列表返回出去
#
#
# def read_invest_data(filename):
#     case_data = []
#     file = app.BASE_DIR + "\\data\\" + filename
#     with open(file, encoding='utf-8') as f:
#         temp_data = json.load(f)
#         for item in temp_data['test_investment_data']:
#             case_data.append((item['loan_type'], item['amount_search'], item['statuscode']))
#     return case_data


def read_data(filename, method_name, params_names):
    """
    通用获取测试数据文件方法
    :param filename:数据文件名
    :param method_name:数据文件中的方法名key,如[test_investment_data]
    :param params_names:json数据文件中一组测试数据中所有的参数组成的字符串
    :return:数据列表
    """
    case_data = []  # 最终返回的列表
    # 文件名拼接
    file = app.BASE_DIR + "\\data\\" + filename
    with open(file, encoding='utf-8') as f:
        temp_data = json.load(f)
        for item in temp_data[f'{method_name}']:  # 拿到全部json文件里的数据
            params_data = []
            for params in params_names.split(","):  # 将传入的实参.进行分割
                params_data.append(item[params])
            case_data.append(tuple(params_data))  # 将列表转换成元组,然后插入到最终返回的列表中
    return case_data


if __name__ == '__main__':
    print(read_data("invest_data.json", "test_investment_data", "loan_type,amount_search,statuscode"))
