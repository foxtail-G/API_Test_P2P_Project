import json

# 参数化函数-登录注册模块
import app


def read_img_verify_code(filename):
    case_data = []  # 最终要返回的列表
    file = app.BASE_DIR + '\\data\\' + filename
    with open(file, encoding='utf-8') as f:
        temp_data = json.load(f)  # 读取json文件
        for item in temp_data['get_img_verify_code']:
            case_data.append((item['type'], item['statusCode']))  # 以元组的方式添加到列表中
    print(file)
    return case_data  # 将列表返回出去
